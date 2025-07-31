#!/usr/bin/env python3
"""
Automated TOTO Data Update and Analysis Script
This script can be run manually or scheduled to automatically update TOTO data
"""

import os
import sys
import time
from datetime import datetime
import pandas as pd

# Import our modules
try:
    from scraper_final import scrape_toto_results_final
    from clean_data import load_data, clean_data
    from summary_analysis import analyze_and_compare
    SCRAPER_AVAILABLE = True
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Make sure all required packages are installed:")
    print("pip install requests beautifulsoup4 pandas matplotlib numpy scipy seaborn")
    SCRAPER_AVAILABLE = False

def check_data_freshness():
    """
    Check if the current data is fresh (less than 7 days old)
    """
    if not os.path.exists("toto_results.csv"):
        return False, "No data file found"
    
    try:
        # Get file modification time
        mtime = os.path.getmtime("toto_results.csv")
        last_modified = datetime.fromtimestamp(mtime)
        days_old = (datetime.now() - last_modified).days
        
        if days_old > 7:
            return False, f"Data is {days_old} days old"
        else:
            return True, f"Data is {days_old} days old"
    except Exception as e:
        return False, f"Error checking file: {e}"

def update_data():
    """
    Update TOTO data if needed
    """
    print("=" * 60)
    print("Automated TOTO Data Update".center(60))
    print("=" * 60)
    
    if not SCRAPER_AVAILABLE:
        print("❌ Scraper not available. Cannot update data.")
        return False
    
    # Check if data needs updating
    is_fresh, status = check_data_freshness()
    print(f"📊 Current data status: {status}")
    
    if is_fresh:
        print("✅ Data is fresh. No update needed.")
        return True
    
    print("🔄 Updating TOTO data...")
    
    try:
        # Backup existing data if it exists
        if os.path.exists("toto_results.csv"):
            backup_name = f"toto_results_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            os.rename("toto_results.csv", backup_name)
            print(f"📦 Backed up existing data to {backup_name}")
        
        # Download fresh data
        results = scrape_toto_results_final()
        
        if results is not None:
            print(f"✅ Successfully updated data: {len(results)} draws")
            return True
        else:
            print("❌ Failed to update data")
            # Restore backup if available
            if os.path.exists(backup_name):
                os.rename(backup_name, "toto_results.csv")
                print("🔄 Restored previous data")
            return False
            
    except Exception as e:
        print(f"❌ Error during update: {e}")
        return False

def run_analysis():
    """
    Run comprehensive analysis on current data
    """
    print("\n" + "=" * 60)
    print("Running Analysis".center(60))
    print("=" * 60)
    
    if not os.path.exists("toto_results.csv"):
        print("❌ No data file found. Run update first.")
        return False
    
    try:
        # Load and clean data
        results, cols = load_data("toto_results.csv")
        if results is None:
            print("❌ Failed to load data")
            return False
        
        clean_results = clean_data(results)
        if clean_results is None:
            print("❌ Failed to clean data")
            return False
        
        print(f"✅ Loaded {len(clean_results)} draws for analysis")
        
        # Run summary analysis
        analysis_results = analyze_and_compare()
        
        if analysis_results:
            print("✅ Analysis completed successfully")
            return True
        else:
            print("❌ Analysis failed")
            return False
            
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        return False

def generate_report():
    """
    Generate a simple text report
    """
    if not os.path.exists("toto_results.csv"):
        return False
    
    try:
        results, cols = load_data("toto_results.csv")
        clean_results = clean_data(results)
        
        # Create report
        report = []
        report.append("TOTO ANALYSIS REPORT")
        report.append("=" * 50)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Data draws: {len(clean_results)}")
        report.append("")
        
        # Frequency analysis
        all_numbers = []
        for col in clean_results.columns:
            all_numbers.extend(clean_results[col].tolist())
        
        from collections import Counter
        freq = Counter(all_numbers)
        
        report.append("MOST FREQUENT NUMBERS:")
        for num, count in freq.most_common(10):
            report.append(f"  {num}: {count} times")
        
        report.append("")
        report.append("LEAST FREQUENT NUMBERS:")
        for num, count in sorted(freq.items())[:10]:
            report.append(f"  {num}: {count} times")
        
        # Save report
        report_text = "\n".join(report)
        with open("toto_report.txt", "w") as f:
            f.write(report_text)
        
        print("📄 Report saved to toto_report.txt")
        return True
        
    except Exception as e:
        print(f"❌ Error generating report: {e}")
        return False

def main():
    """
    Main function for automated updates
    """
    print("🤖 TOTO Automated Update and Analysis")
    print("=" * 50)
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "update":
            success = update_data()
            sys.exit(0 if success else 1)
        
        elif command == "analyze":
            success = run_analysis()
            sys.exit(0 if success else 1)
        
        elif command == "report":
            success = generate_report()
            sys.exit(0 if success else 1)
        
        elif command == "full":
            print("🔄 Running full update and analysis...")
            update_success = update_data()
            if update_success:
                analysis_success = run_analysis()
                report_success = generate_report()
                sys.exit(0 if all([update_success, analysis_success, report_success]) else 1)
            else:
                sys.exit(1)
        
        else:
            print(f"❌ Unknown command: {command}")
            print("Available commands: update, analyze, report, full")
            sys.exit(1)
    
    # Interactive mode
    print("Choose operation:")
    print("1. Update data only")
    print("2. Run analysis only")
    print("3. Generate report only")
    print("4. Full update and analysis")
    print("0. Exit")
    
    choice = input("Choice: ")
    
    if choice == "1":
        update_data()
    elif choice == "2":
        run_analysis()
    elif choice == "3":
        generate_report()
    elif choice == "4":
        print("🔄 Running full update and analysis...")
        update_success = update_data()
        if update_success:
            run_analysis()
            generate_report()
    elif choice == "0":
        print("Goodbye!")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main() 