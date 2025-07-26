import clean_data
import toto_analysis
import monte_carlo
import backtest
from random import randint



def main():

    while True:

        print("=" * 60)
        print("Main Menu".center(60))
        print("-" * 60, "\n")

        choice = input("Which data do you want to look at?\n" \
        "1. Past Data\n" \
        "2. Monte carlo simulated data\n" \
        "3. Generate new simulated data\n" \
        "0. Exit\n" \
        "------------------------------------------------------------\n" \
        "Choice: ")

        match choice:
            case "0":
                break
            case "1":
                file = "toto_results.csv"
                menu2(file)
            case "2":
                file = "simulated_draws.csv"
                menu2(file)
            case "3":
                monte_carlo.monte_carlo_simulation(100000)
                file = "simulated_draws.csv"
                menu2(file)
            case _:
                print("Invalid choice! Try again")



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
            "0. Back \n" \
            "------------------------------------------------------------\n" \
            "Choice: ")

        match choice:
            case "0":
                break
            case "1":
                toto_analysis.individual_bar_chart(clean_results, column_names)
            case "2":
                toto_analysis.grouped_bar_chart(clean_results, column_names)
            case "3":
                toto_analysis.overall_frequency_chart(clean_results)
            case "4":
                toto_analysis.confidence_interval(clean_results)
            case "5":            
                backtest.backtest(clean_results)
            case "6":
                position_ranges = [[1, 5],
                                   [7, 16],
                                   [16, 25],
                                   [25, 34],
                                   [35, 44],
                                   [40, 49]]

                backtest.backtest_with_position_ranges(clean_results, position_ranges)
            case _:
                print("Invalid choice! Try again")



if __name__ == "__main__":
    main()