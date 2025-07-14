# Importing relevant libraries
import pandas as pd



# Load data from csv file and catch errors if there are any
def load_data(file):

    print("=" * 60)
    print("Loading data".center(60))
    print("-" * 60, "\n")
    # Use try except to handle errors
    try:
        # Open file containing past toto results
        df = pd.read_csv(file)

        # Rename columns if using past data
        column_names = ['Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Num6', 'Num7']

        if (file == "toto_results.csv"):
            results_columns = ['Winning Number 1', '2', '3', '4', '5', '6', 'Additional Number']
            results = df[results_columns]
            results.columns = column_names
        else:
            results = df[column_names]

        print("Data loaded sucessfully from: ", file, "\n")
        return results, column_names
    
    # Handles FileNotFoundError when file is not found
    except FileNotFoundError:
        print("Error! CSV file not found!")
        print("Download CSV file from 'https://en.lottolyzer.com/history/singapore/toto'")
        return None, None
    
    # Handles KeyError when there is a missing column
    except KeyError as e:
        print(f"Error! Missing column: {e}")
        return None, None
    
    # Handles any other exceptions and prints it out
    except Exception as e:
        print(f"UnknownError! {e}")
        return None, None
    


def clean_data(results):
    print("=" * 60)
    print("Cleaning data".center(60))
    print("-" * 60, "\n")
    print("Cleaning data...")

    # Ensure all values are numeric
    results_numeric = results.map(pd.to_numeric, errors="coerce")

    # Check for NaN (missing values)
    mask_nan = results_numeric.isnull().any(axis=1)

    # Check for values that are not integers
    mask_non_integer = (results_numeric % 1 != 0).any(axis=1)

    # Check if values are out of range (1-49)
    mask_out_of_range = ~results_numeric.isin(
        range(1, 50)
    ).all(axis=1)

    # Check for duplicate values in each row
    mask_duplicates = results_numeric.apply(
        lambda row: row.duplicated().any(), axis=1
    )

    # Check if numbers are in increasing order from num1-num6
    mask_not_increasing = ~results_numeric[["Num1", "Num2", "Num3", "Num4", "Num5", "Num6"]].apply(
        lambda row: all(row.iloc[i] < row.iloc[i+1] for i in range(5)), axis=1
    )

    # Combine all invalid rows
    mask_invalid = mask_nan | mask_non_integer | mask_out_of_range | mask_duplicates | mask_not_increasing

    # Print results 
    print(f"Rows with missing values:\n{results_numeric[mask_nan]}\n")
    print(f"Rows with non-integer values:\n{results_numeric[mask_non_integer]}\n")
    print(f"Rows with out-of-range values:\n{results_numeric[mask_out_of_range]}\n")
    print(f"Rows with duplicate values:\n{results_numeric[mask_duplicates]}\n")
    print(f"Rows with non-increasing values from Num1-Num6:\n{results_numeric[mask_not_increasing]}\n")

    # Getting clean results
    clean_results = results_numeric[~mask_invalid].astype(int)

    num_clean_results = len(clean_results)
    total_results = len(results)

    print(f"Total clean rows: {num_clean_results} / {total_results}\n")

    # Check if all results are clean
    if num_clean_results == total_results:
        print("Dataset is clean! Ready for analysis!")
        return clean_results
    
    while True:
        choice = input("Errors found in dataset! \n" \
        "1. Skip rows with errors \n" \
        "0. Exit \n"
        "Enter choice: ")

        if choice == "1":
            return clean_results
        elif choice == "0":
            return None
        
        print("Invalid input! Please enter 1 or 0!")



def main():

    file = "toto_results.csv"

    # Loads data from CSV file
    results, column_names = load_data(file)

    # Checks if any errors occured when loading data
    if results is None or column_names is None:
        return
    
    # Cleans results 
    clean_results = clean_data(results)
    print(clean_results)



if __name__ == "__main__":
    main()