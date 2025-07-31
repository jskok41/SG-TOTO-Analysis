import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def backtest(results):

    predicted_numbers = getNum()
    print("Start backtest")
    print(f"Testing for: {predicted_numbers}")
    
    # Backtesting
    c_3 = 0
    c_4 = 0
    c_5 = 0
    c_6 = 0
    matches = []
    winners = 0

    for idx, row in results.iterrows():
        matched = [num for num in row if num in predicted_numbers]
        match_count = len(matched)
        if (match_count >= 3):
            winners += 1
        matches.append(match_count)

        match(match_count):
            case 3:
                c_3 += 1
            case 4:
                c_4 += 1
            case 5:
                c_5 += 1
            case 6:
                c_6 += 1

        print(f"Draw {idx}: Matched {match_count} numbers: {matched}")

    avg_hits = np.mean(matches)
    print(f"\nAverage correct predictions per draw: {avg_hits:.2f}")
    print(f"Number of winning draws (3 or more hits): {winners}")

    print("3 correct: ", c_3)
    print("4 correct: ", c_4)
    print("5 correct: ", c_5)
    print("6 correct: ", c_6)

    


def backtest_with_position_ranges(results, position_ranges):

    # Keep only Num1–Num6
    expected_cols = ['Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Num6']

    if not all(col in results.columns for col in expected_cols):
        raise ValueError("CSV must contain columns: Num1 to Num6 (at least)")
    
    results = results[expected_cols]

    print("Testing position-based number ranges:")
    for i, (low, high) in enumerate(position_ranges):
        print(f"  Position {i+1} (Num{i+1}): {low} to {high}")

    correct_positions = []
    opp_positions = []

    correct_3 = 0
    correct_4 = 0
    correct_5 = 0
    correct_6 = 0

    opp_3 = 0
    opp_4 = 0
    opp_5 = 0
    opp_6 = 0

    for idx, row in results.iterrows():
        correct = 0
        opp = 0
        for i, num in enumerate(row):
            low, high = position_ranges[i]
            if low <= num <= high:
                correct += 1
            else:
                opp += 1
        correct_positions.append(correct)
        opp_positions.append(opp)
        
        match(correct):
            case 3:
                correct_3 += 1
            case 4:
                correct_4 += 1
            case 5:
                correct_5 += 1
            case 6:
                correct_6 += 1
        
        match(opp):
            case 3:
                opp_3 += 1
            case 4:
                opp_4 += 1
            case 5:
                opp_5 += 1
            case 6:
                opp_6 += 1

        print(f"Draw {idx}: {correct} correct → {list(row)}")

    avg_correct = np.mean(correct_positions)
    avg_opp = np.mean(opp_positions)
    print(f"\nAverage correct positions per draw: {avg_correct:.2f}")

    print("3 correct: ", correct_3)
    print("4 correct: ", correct_4)
    print("5 correct: ", correct_5)
    print("6 correct: ", correct_6)

    print(f"\nAverage opp positions per draw: {avg_opp:.2f}")
    print("3 opp: ", opp_3)
    print("4 opp: ", opp_4)
    print("5 opp: ", opp_5)
    print("6 opp: ", opp_6)

    # Plot
    plt.hist(correct_positions, bins=range(0, 8), align='left',
             rwidth=0.8, color='cornflowerblue')
    plt.xticks(range(0, 7))
    plt.xlabel('Correct Positions per Draw')
    plt.ylabel('Frequency')
    plt.title('Backtest: Position-Based Number Ranges')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # Plot
    plt.hist(opp_positions, bins=range(0, 8), align='left',
             rwidth=0.8, color='red')
    plt.xticks(range(0, 7))
    plt.xlabel('Opp Positions per Draw')
    plt.ylabel('Frequency')
    plt.title('Backtest: Position-Based Number Ranges')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    return {
        "position_ranges": position_ranges,
        "average_correct_positions": avg_correct,
        "match_counts": correct_positions
    }



def getNum():

    predicted_numbers = []

    while (len(predicted_numbers) < 6):
        try:
            num = input("Enter a number to backtest: ")
            num = int(num)

            if (1 <= num <= 49):
                if (num not in predicted_numbers):
                    predicted_numbers.append(num)
                else:
                    print("Number already in list! Try again")
            else:
                print("Number not in range 1-49! Try again")  
        except ValueError:
            print("Invalid input. Please enter an integer number.")

    return predicted_numbers    



def main():
    print("main")



if __name__ == "__main":
    main()