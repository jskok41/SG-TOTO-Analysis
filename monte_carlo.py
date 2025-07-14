import pandas as pd
import numpy as np



def monte_carlo_simulation(num_draws=100000):
    
    print("Generating random values...")

    draws = []

    for _ in range(num_draws):
        # Step 1: pick 6 unique numbers from 1-49
        winning_nums = np.random.choice(range(1, 50), size=6, replace=False)
        winning_nums.sort()

        # Step 2: pick 7th additional number, distinct from first 6
        remaining_nums = set(range(1, 50)) - set(winning_nums)
        additional_num = np.random.choice(list(remaining_nums), size=1)[0]

        # Step 3: Combine into a single draw record
        draw = list(winning_nums) + [additional_num]
        draws.append(draw)

    # Step 4: Build DataFrame with same columns as your real data
    column_names = ['Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Num6', 'Num7']
    df_simulated = pd.DataFrame(draws, columns=column_names)

    print("Generating file...")

    df_simulated.to_csv("simulated_draws.csv", index=False)

    print("File generated!")



def main():
    monte_carlo_simulation(1000000)


if __name__ == "__main__":
    main()