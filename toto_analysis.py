# Importing relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import seaborn as sns
from collections import defaultdict



# Plot value counts for each column indivudually (Num1 - Num7)
def individual_bar_chart(results, column_names, return_fig=False):
    
    # Loop for each number (Num1 - Num7)
    for name in column_names:

        # Get results for selected row, count the number of times it appears, and sort them numerically
        counts = results[name].value_counts().sort_index()

        # Add missing numbers if any (count = 0)
        full_counts = pd.Series(index=range(1, 50), dtype=int).add(counts, fill_value=0)

        # Plot bar chart
        fig, ax = plt.subplots(figsize=(10, 4))
        full_counts.plot(kind='bar', ax=ax)
        plt.xticks(ticks=np.arange(49), labels=np.arange(1, 50), rotation=90)
        plt.xlabel('Value')
        plt.ylabel('Count')
        plt.title(f'{name} Counts')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        if return_fig:
            return fig
        else:
            plt.show()



# Plot value counts for each column together (Num1 - Num6)
def grouped_bar_chart(results, column_names, return_fig=False):
    
    # Define empty dataset to store Num1 - Num6
    datasets = []

    # Loop for each number from Num1 - Num6
    for name in column_names[:6]:

        # Get results for selected row, count the number of times it appears, and sort them numerically
        counts = results[name].value_counts().sort_index()
        
        # Add missing numbers if any (count = 0)
        full_counts = pd.Series(index=range(1, 50), dtype=int).add(counts, fill_value=0)

        # Add counts into dataset
        datasets.append(full_counts)

    # Combine into 1 dataframe
    df_combined = pd.concat(datasets, axis=1)
    df_combined.columns = column_names[:6]
    df_combined = df_combined.fillna(0)

    # Define variables for bar chart
    n_categories = 49
    n_datasets = df_combined.shape[1]
    bar_width = 0.12
    indices = np.arange(n_categories)
    colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'orange']

    # Plot bar chart
    fig, ax = plt.subplots(figsize=(18, 8))

    # Loop through and plot each column shifted horizontally to group by number (each number contains Num1 - Num6 counts)
    for i, col in enumerate(df_combined.columns):
        ax.bar(indices + i * bar_width, df_combined[col], width=bar_width, label=col, color=colors[i])

    # Center x-ticks
    ax.set_xticks(indices + bar_width * (n_datasets - 1) / 2)
    ax.set_xticklabels(df_combined.index, rotation=90)

    ax.set_xlabel('Value')
    ax.set_ylabel('Count')
    ax.set_title('Grouped Bar Chart: Frequency of Each Number (Num1–Num6)')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.legend()
    plt.tight_layout()
    
    if return_fig:
        return fig
    else:
        plt.show()



# Plot total number of times value appear between Num1 - Num7
def overall_frequency_chart(results, return_fig=False):

    # Add all numbers from Num1 - Num7 into 1 dataset
    all_numbers = pd.concat([results[col] for col in results.columns])
    
    # Get results for selected row, count the number of times it appears, and sort them numerically
    counts = all_numbers.value_counts().sort_index()

    # Add missing numbers if any (count = 0)
    full_counts = pd.Series(index=range(1, 50), dtype=int).add(counts, fill_value=0).astype(int)

    # testing
    print(full_counts)

    # Plot overall frequency
    fig, ax = plt.subplots(figsize=(12, 5))
    full_counts.plot(kind='bar', ax=ax, color='steelblue')
    plt.xticks(ticks=np.arange(49), labels=np.arange(1, 50), rotation=90)
    plt.xlabel('Number')
    plt.ylabel('Total Count')
    plt.title('Overall Frequency of Numbers (Num1 to Num7)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    if return_fig:
        return fig
    else:
        plt.show()



# Plot 95% confidence interval 
def confidence_interval(results, return_fig=False):

    # 95% confidence interval
    z = norm.ppf(0.975)

    # Loop for each column
    for col in results.columns:
        print(f"Confidence Interval for {col} (Sorted by %)".center(84))
        num_series = results[col]
        total_trials = len(num_series)

        counts = num_series.value_counts().sort_index()
        full_counts = pd.Series(0, index=range(1, 50)).add(counts, fill_value=0).astype(int)

        # Collect data rows for this column
        data_rows = []

        # Loop for each number from 1-49 and calculate values
        # p : proportion
        # p_pct : percentage
        # se : standard error
        # ci_lower: confidence interval lower
        # ci_upper: confidence interval upper
        for number in range(1, 50):
            count = full_counts[number]
            p = count / total_trials
            se = np.sqrt(p * (1 - p) / total_trials)
            ci_lower = max(0, p - z * se)
            ci_upper = min(1, p + z * se)

            p_pct = p * 100
            ci_lower_pct = ci_lower * 100
            ci_upper_pct = ci_upper * 100
            ci_width = ci_upper_pct - ci_lower_pct

            # Store values in list
            data_rows.append((number, count, p, p_pct, ci_lower_pct, ci_upper_pct, ci_width))

        # Sort by percentage descending
        data_rows.sort(key=lambda x: x[3], reverse=True)

        # Print header
        print(f"{'Number':>6} | {'Count':>6} | {'Proportion':>10} | {'%':>6} | {'95% CI Lower':>12} | {'95% CI Upper':>12} | {'CI Width':>12}")
        print("-" * 84)

        # loop through list and print results
        for row in data_rows:
            number, count, p, p_pct, ci_lower_pct, ci_upper_pct, ci_width = row
            print(f"{number:6d} | {count:6d} | {p:10.4f} | {p_pct:5.1f}% | {ci_lower_pct:11.1f}% | {ci_upper_pct:11.1f}% | {ci_width:11.1f}%")

        print("-" * 84)

    # Create visualization for confidence intervals
    if return_fig:
        fig, ax = plt.subplots(figsize=(15, 8))
        
        # Use the first column for visualization
        col = results.columns[0]
        num_series = results[col]
        total_trials = len(num_series)
        counts = num_series.value_counts().sort_index()
        full_counts = pd.Series(0, index=range(1, 50)).add(counts, fill_value=0).astype(int)
        
        numbers = []
        proportions = []
        ci_lowers = []
        ci_uppers = []
        
        for number in range(1, 50):
            count = full_counts[number]
            p = count / total_trials
            se = np.sqrt(p * (1 - p) / total_trials)
            ci_lower = max(0, p - z * se)
            ci_upper = min(1, p + z * se)
            
            numbers.append(number)
            proportions.append(p * 100)
            ci_lowers.append(ci_lower * 100)
            ci_uppers.append(ci_upper * 100)
        
        # Plot confidence intervals
        ax.errorbar(numbers, proportions, yerr=[np.array(proportions) - np.array(ci_lowers), 
                                               np.array(ci_uppers) - np.array(proportions)], 
                   fmt='o', capsize=5, capthick=2, elinewidth=2, markersize=6)
        ax.set_xlabel('Number')
        ax.set_ylabel('Percentage (%)')
        ax.set_title(f'95% Confidence Intervals for {col}')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        
        return fig
