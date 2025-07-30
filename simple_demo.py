#!/usr/bin/env python3
"""
Simple Demo script for TOTO Number Analysis
This script demonstrates the data processing without generating plots.
"""

import clean_data
import monte_carlo
import pandas as pd

def main():
    print("=" * 60)
    print("TOTO Number Analysis - Simple Demo".center(60))
    print("=" * 60)
    
    # Generate simulated data
    print("\n1. Generating simulated TOTO data...")
    monte_carlo.monte_carlo_simulation(1000)
    print("   ✓ Simulated data generated successfully!")
    
    # Load the data
    print("\n2. Loading and analyzing data...")
    results, column_names = clean_data.load_data('simulated_draws.csv')
    
    if results is None or column_names is None:
        print("   ✗ Failed to load data!")
        return
    
    print(f"   ✓ Loaded {len(results)} draws")
    print(f"   ✓ Columns: {column_names}")
    
    # Show sample data
    print("\n3. Sample data (first 5 rows):")
    print(results.head())
    
    # Basic statistics
    print("\n4. Basic statistics:")
    print(f"   - Total number of draws: {len(results)}")
    print(f"   - Number of columns: {len(column_names)}")
    
    # Number frequency analysis
    print("\n5. Number frequency analysis:")
    all_numbers = []
    for col in column_names:
        all_numbers.extend(results[col].tolist())
    
    number_counts = pd.Series(all_numbers).value_counts().sort_index()
    print("   Most frequent numbers:")
    print(number_counts.head(10))
    print("\n   Least frequent numbers:")
    print(number_counts.tail(10))
    
    # Position analysis
    print("\n6. Position analysis:")
    for i, col in enumerate(column_names, 1):
        pos_avg = results[col].mean()
        pos_std = results[col].std()
        print(f"   Position {i} ({col}): Avg={pos_avg:.1f}, Std={pos_std:.1f}")
    
    # Summary statistics
    print("\n7. Summary statistics:")
    print(f"   - Average number across all positions: {pd.Series(all_numbers).mean():.1f}")
    print(f"   - Standard deviation: {pd.Series(all_numbers).std():.1f}")
    print(f"   - Range: {pd.Series(all_numbers).min()} to {pd.Series(all_numbers).max()}")
    
    print("\n" + "=" * 60)
    print("Demo completed successfully!".center(60))
    print("=" * 60)
    print("\nThe analysis shows:")
    print("- Number frequency distributions")
    print("- Position-specific patterns")
    print("- Statistical insights for TOTO number selection")

if __name__ == "__main__":
    main()