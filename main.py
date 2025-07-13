import clean_data
import toto_analysis



def main():


    # Loads data from CSV file
    results, column_names = clean_data.load_data()

    # Checks if any errors occured when loading data
    if results is None or column_names is None:
        return
    
    # Cleans results 
    clean_results = clean_data.clean_data(results)

    print("=" * 60)
    print("Main Menu".center(60))
    print("-" * 60, "\n")


    while True:
        choice = input("What data do you want to look at?\n" \
        "1. Individual bar chart\n" \
        "2. Grouped bar chart\n"
        "3. Overall frequency \n" \
        "4. Confidence interval chart \n" \
        

        "7. Monte carlo \n" \
        "0. End\n" \
        "===========================\n" \
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
                toto_analysis.confidence_interval_all_positions(clean_results)

            case _:
                print("Invalid choice! Try again")


            # case "7":
            #     monte_carlo_simulation()


            # case "4":
            #     backtest_prediction(clean_results, strategy='most')
            # case "5":
            #     backtest_prediction(clean_results, strategy='least')



if __name__ == "__main__":
    main()