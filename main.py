import clean_data
import toto_analysis
import monte_carlo
import backtest
from random import randint
import os

# Import scraper functionality
try:
    from scraper_final import scrape_toto_results_final, scrape_multiple_pages
    SCRAPER_AVAILABLE = True
except ImportError:
    SCRAPER_AVAILABLE = False
    print("Warning: Scraper not available. Install required packages: pip install requests beautifulsoup4")

def main():

    while True:

        print("=" * 60)
        print("Main Menu".center(60))
        print("-" * 60, "\n")

        choice = input("Which data do you want to look at?\n" \
        "1. Past Data\n" \
        "2. Monte carlo simulated data\n" \
        "3. Generate new simulated data\n" \
        "4. Download fresh TOTO data\n" \
        "0. Exit\n" \
        "------------------------------------------------------------\n" \
        "Choice: ")

        if choice == "0":
            break
        elif choice == "1":
            file = "toto_results.csv"
            if not os.path.exists(file):
                print(f"❌ {file} not found!")
                print("Use option 4 to download fresh TOTO data first.")
                continue
            menu2(file)
        elif choice == "2":
            file = "simulated_draws.csv"
            if not os.path.exists(file):
                print(f"❌ {file} not found!")
                print("Use option 3 to generate simulated data first.")
                continue
            menu2(file)
        elif choice == "3":
            print("Generating Monte Carlo simulated data...")
            monte_carlo.monte_carlo_simulation(100000)
            file = "simulated_draws.csv"
            menu2(file)
        elif choice == "4":
            if not SCRAPER_AVAILABLE:
                print("❌ Scraper not available. Install required packages:")
                print("pip install requests beautifulsoup4")
                continue
            download_fresh_data()
        else:
            print("Invalid choice! Try again")

def download_fresh_data():
    """
    Download fresh TOTO data using the scraper
    """
    print("=" * 60)
    print("Download Fresh TOTO Data".center(60))
    print("-" * 60)
    
    print("Choose download option:")
    print("1. Quick download (50 recent draws)")
    print("2. Extended download (multiple pages)")
    print("0. Back to main menu")
    
    choice = input("Choice: ")
    
    if choice == "1":
        print("\n🔄 Downloading recent TOTO data...")
        results = scrape_toto_results_final()
        if results is not None:
            print(f"✅ Successfully downloaded {len(results)} draws!")
            print("Data saved to toto_results.csv")
            menu2("toto_results.csv")
        else:
            print("❌ Download failed. Please try again.")
    
    elif choice == "2":
        print("\n🔄 Downloading extended TOTO data...")
        print("This may take a few minutes...")
        results = scrape_multiple_pages()
        if results is not None:
            print(f"✅ Successfully downloaded {len(results)} draws!")
            print("Data saved to toto_results.csv")
            menu2("toto_results.csv")
        else:
            print("❌ Download failed. Please try again.")
    
    elif choice == "0":
        return
    
    else:
        print("Invalid choice!")

def menu2(file):

    # Loads data from CSV file
    results, column_names = clean_data.load_data(file)

    # Checks if any errors occured when loading data
    if results is None or column_names is None:
        return

    while True:

        if (file == "toto_results.csv"):
            # Cleans results (from 3rd party so dk if its clean)
            clean_results = clean_data.clean_data(results)

            print("=" * 60)
            print("Past Results(toto_results.csv)".center(60))
            print("-" * 60)

        else:
            # No need to clean as we generated ourselves and know its clean
            clean_results = results
            print("=" * 60)
            print("Monte Carlo Simulated Results(simulated_results.csv)".center(60))
            print("-" * 60)

        choice = input(
            "Data Analysis\n" \
            "1. Individual bar chart\n" \
            "2. Grouped bar chart\n"
            "3. Overall frequency \n" \
            "4. Confidence interval chart \n" \
            "5. Backtest \n" \
            "6. Backtest with positional ranges \n" \
            "7. Quick summary analysis \n" \
            "0. Back \n" \
            "------------------------------------------------------------\n" \
            "Choice: ")

        if choice == "0":
            break
        elif choice == "1":
            toto_analysis.individual_bar_chart(clean_results, column_names)
        elif choice == "2":
            toto_analysis.grouped_bar_chart(clean_results, column_names)
        elif choice == "3":
            toto_analysis.overall_frequency_chart(clean_results)
        elif choice == "4":
            toto_analysis.confidence_interval(clean_results)
        elif choice == "5":            
            backtest.backtest(clean_results)
        elif choice == "6":
            position_ranges = [[1, 5],
                               [7, 16],
                               [16, 25],
                               [25, 34],
                               [35, 44],
                               [40, 49]]

            backtest.backtest_with_position_ranges(clean_results, position_ranges)
        elif choice == "7":
            quick_summary(clean_results, file)
        else:
            print("Invalid choice! Try again")

def quick_summary(results, file_type):
    """
    Provide a quick summary of the data
    """
    print("=" * 60)
    print("Quick Summary Analysis".center(60))
    print("-" * 60)
    
    print(f"📊 Dataset: {file_type}")
    print(f"📈 Total draws: {len(results)}")
    
    # Overall frequency
    all_numbers = []
    for col in results.columns:
        all_numbers.extend(results[col].tolist())
    
    from collections import Counter
    freq = Counter(all_numbers)
    
    print(f"\n🎯 Most frequent numbers:")
    for num, count in freq.most_common(5):
        print(f"   {num}: {count} times")
    
    print(f"\n📉 Least frequent numbers:")
    for num, count in sorted(freq.items())[:5]:
        print(f"   {num}: {count} times")
    
    # Position analysis
    print(f"\n📍 Position analysis (most common per position):")
    for i, col in enumerate(results.columns[:6]):
        most_common = results[col].value_counts().head(3)
        print(f"   {col}: {list(most_common.index)}")
    
    # Statistical insights
    print(f"\n📊 Statistical insights:")
    print(f"   Expected frequency per number: {len(results) * 7 / 49:.1f}")
    
    # Calculate actual standard deviation
    import numpy as np
    freq_values = list(freq.values())
    std_dev = np.std(freq_values)
    print(f"   Standard deviation of frequencies: {std_dev:.2f}")
    
    # Check data freshness
    import os
    from datetime import datetime
    if file_type == "toto_results.csv" and os.path.exists(file_type):
        mtime = os.path.getmtime(file_type)
        last_modified = datetime.fromtimestamp(mtime)
        days_old = (datetime.now() - last_modified).days
        print(f"   Data age: {days_old} days old")
    
    print(f"\n✅ Summary complete!")

if __name__ == "__main__":
    main()