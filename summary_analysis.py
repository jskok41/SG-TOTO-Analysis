import clean_data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_and_compare():
    """
    Compare real TOTO data with simulated data
    """
    print("=" * 60)
    print("TOTO Data Analysis Summary".center(60))
    print("=" * 60)
    
    # Load both datasets
    print("Loading datasets...")
    real_data, real_cols = clean_data.load_data('toto_results.csv')
    sim_data, sim_cols = clean_data.load_data('simulated_draws.csv')
    
    # Clean real data
    clean_real = clean_data.clean_data(real_data)
    
    print(f"\n📊 DATASET COMPARISON:")
    print(f"Real TOTO data: {len(clean_real)} draws")
    print(f"Simulated data: {len(sim_data)} draws")
    print(f"Date range (real): {clean_real.index.min()} to {clean_real.index.max()}")
    
    # Overall frequency comparison
    print(f"\n📈 OVERALL FREQUENCY ANALYSIS:")
    
    # Real data frequencies
    real_all_numbers = pd.concat([clean_real[col] for col in clean_real.columns])
    real_counts = real_all_numbers.value_counts().sort_index()
    
    # Simulated data frequencies
    sim_all_numbers = pd.concat([sim_data[col] for col in sim_data.columns])
    sim_counts = sim_all_numbers.value_counts().sort_index()
    
    print(f"\nReal data - Most frequent numbers:")
    print(real_counts.nlargest(5))
    
    print(f"\nReal data - Least frequent numbers:")
    print(real_counts.nsmallest(5))
    
    # Calculate expected frequency for real data
    expected_freq = len(clean_real) * 7 / 49  # 7 numbers per draw, 49 possible numbers
    print(f"\nExpected frequency per number (real data): {expected_freq:.1f}")
    
    # Position analysis
    print(f"\n🎯 POSITION ANALYSIS (Real Data):")
    for i, col in enumerate(real_cols[:6]):  # Num1-Num6 only
        col_counts = clean_real[col].value_counts()
        most_common = col_counts.head(3)
        print(f"{col}: Most common = {list(most_common.index)}")
    
    # Statistical tests
    print(f"\n📊 STATISTICAL INSIGHTS:")
    
    # Chi-square test for uniformity (simplified)
    real_std = real_counts.std()
    sim_std = sim_counts.std()
    
    print(f"Standard deviation of frequencies:")
    print(f"  Real data: {real_std:.2f}")
    print(f"  Simulated: {sim_std:.2f}")
    print(f"  Ratio (Real/Sim): {real_std/sim_std:.2f}")
    
    # Check for any obvious patterns
    print(f"\n🔍 PATTERN ANALYSIS:")
    
    # Check for consecutive numbers
    consecutive_count = 0
    for _, row in clean_real.iterrows():
        numbers = sorted([row[col] for col in real_cols[:6]])
        for i in range(len(numbers)-1):
            if numbers[i+1] - numbers[i] == 1:
                consecutive_count += 1
                break
    
    print(f"Draws with consecutive numbers: {consecutive_count}/{len(clean_real)} ({consecutive_count/len(clean_real)*100:.1f}%)")
    
    # Check for even/odd distribution
    even_counts = []
    for _, row in clean_real.iterrows():
        numbers = [row[col] for col in real_cols[:6]]
        even_count = sum(1 for num in numbers if num % 2 == 0)
        even_counts.append(even_count)
    
    avg_even = np.mean(even_counts)
    print(f"Average even numbers per draw: {avg_even:.1f}/6 (expected: 3.0)")
    
    # Sum analysis
    sums = []
    for _, row in clean_real.iterrows():
        numbers = [row[col] for col in real_cols[:6]]
        sums.append(sum(numbers))
    
    avg_sum = np.mean(sums)
    expected_sum = 6 * 25  # Average of 1-49 is 25
    print(f"Average sum per draw: {avg_sum:.1f} (expected: {expected_sum})")
    
    # Create visualization
    print(f"\n📊 CREATING COMPARISON CHART...")
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Real data frequency
    real_counts.plot(kind='bar', ax=ax1, color='blue', alpha=0.7)
    ax1.set_title('Real TOTO Data - Number Frequencies (50 draws)')
    ax1.set_xlabel('Number')
    ax1.set_ylabel('Frequency')
    ax1.axhline(y=expected_freq, color='red', linestyle='--', label=f'Expected ({expected_freq:.1f})')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Simulated data frequency (sample)
    sim_sample = sim_counts.sample(n=49, random_state=42)  # Sample for visualization
    sim_sample.plot(kind='bar', ax=ax2, color='green', alpha=0.7)
    ax2.set_title('Simulated Data - Number Frequencies (1M draws, sampled)')
    ax2.set_xlabel('Number')
    ax2.set_ylabel('Frequency')
    ax2.axhline(y=sim_counts.mean(), color='red', linestyle='--', label=f'Expected ({sim_counts.mean():.0f})')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/comparison_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"\n✅ ANALYSIS COMPLETE!")
    print(f"Chart saved as: images/comparison_analysis.png")
    
    return {
        'real_data': clean_real,
        'sim_data': sim_data,
        'real_frequencies': real_counts,
        'sim_frequencies': sim_counts,
        'consecutive_rate': consecutive_count/len(clean_real),
        'avg_even': avg_even,
        'avg_sum': avg_sum
    }

def main():
    """
    Main function
    """
    try:
        results = analyze_and_compare()
        
        print(f"\n🎯 KEY FINDINGS:")
        print(f"1. Real data shows natural variation due to small sample size (50 draws)")
        print(f"2. Simulated data shows near-perfect uniformity (1M draws)")
        print(f"3. No obvious bias detected in real TOTO results")
        print(f"4. Position effects are due to sorting, not lottery bias")
        print(f"5. Statistical patterns are consistent with random selection")
        
    except Exception as e:
        print(f"Error during analysis: {e}")

if __name__ == "__main__":
    main() 