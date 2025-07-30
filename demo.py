#!/usr/bin/env python3
"""
Demo script for TOTO Number Analysis
This script demonstrates the main functionality without requiring interactive input.
"""

import clean_data
import toto_analysis
import backtest
import monte_carlo

def main():
    print("=" * 60)
    print("TOTO Number Analysis Demo".center(60))
    print("=" * 60)
    
    # Generate simulated data if it doesn't exist
    print("\n1. Generating simulated TOTO data...")
    monte_carlo.monte_carlo_simulation(1000)
    print("   ✓ Simulated data generated successfully!")
    
    # Load and analyze the data
    print("\n2. Loading and analyzing data...")
    results, column_names = clean_data.load_data('simulated_draws.csv')
    
    if results is None or column_names is None:
        print("   ✗ Failed to load data!")
        return
    
    print(f"   ✓ Loaded {len(results)} draws with columns: {column_names}")
    
    # Run different analyses
    print("\n3. Running analyses...")
    
    print("\n   a) Overall frequency analysis:")
    toto_analysis.overall_frequency_chart(results)
    
    print("\n   b) Individual bar chart analysis:")
    toto_analysis.individual_bar_chart(results, column_names)
    
    print("\n   c) Grouped bar chart analysis:")
    toto_analysis.grouped_bar_chart(results, column_names)
    
    print("\n   d) Confidence interval analysis:")
    toto_analysis.confidence_interval(results)
    
    print("\n   e) Backtest analysis:")
    backtest.backtest(results)
    
    print("\n" + "=" * 60)
    print("Demo completed successfully!".center(60))
    print("=" * 60)
    print("\nThe analysis shows:")
    print("- Number frequency distributions")
    print("- Statistical patterns in the data")
    print("- Backtest results for different strategies")
    print("- Confidence intervals for predictions")

if __name__ == "__main__":
    main()