# TOTO Number Analysis 🎯
A data analysis project exploring number frequency, patterns, and trends in Singapore TOTO lottery draws using Python. This project aims to gain insights from historical TOTO results through statistical techniques and data visualization.

---

## 📊 Project Overview
The goal of this project is to explore whether there is a smarter way to select our TOTO numbers that would give us a statistical advantage over just randomly selecting them.
We will be doing this through:
- Analysing the frequency of winning numbers.
- Visualising trends over time.
- Identifying number distribution and repetition patterns.
- Exploring and evaluating basic prediction strategies.

---

## 🧰 Tech Stack
- **Language**:
    - Python 3

- **Libraries**:
    - Pandas (For data manipulation and cleaning)
    - Matplotlib / Seaborn (For visualizing frequency and trends)
    - SciPy (For statistical calculations)

---

## 📁 Project Structure
```
toto-number-analysis/
├── toto_results.csv    # Historical TOTO draw data (input)
├── toto_analysis.py    # Main script with menu and analysis functions
├── README.md           # Project documentation
└── requirements.txt    # Python package dependencies
```

---

## ▶️ How to Use
1. **Clone the repository**:
    ```bash
    git clone https://github.com/cyuanjun/toto-number-analysis.git
    ```

2. **Change directory**:
    ```bash
    cd toto-number-analysis
    ```

3. **Create/Activate virtual environment (Optional)**:
    
    - #### Windows:
        - Creating virtual environment
        ```bash
        python -m venv toto_number_analysis_venv
        ```

        - Activating virtual environment
        ```
        toto_number_analysis\Scripts\activate
        ```
    - #### Mac:
        - Creating virtual environment
        ```bash
        python3 -m venv toto_number_analysis
        ```

        - Activating virtual environment
        ```
        source toto_number_analysis/bin/activate
        ```

    - #### Deactivating virtual environment (Windows/Mac)
        - Same for Windows / Mac
        ```bash
        deactivate
        ```

4. **Install necessary libraries from requirements.txt file into virtual environment**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Running the script**:
    ```bash
    python toto_analysis.py
    ```

6. **Navigate with command-line-interface**:
    - Select the option that you want by typing into the command-line
    ```
    What data do you want to look at?
    1. Individual bar chart
    2. Grouped bar chart
    3. Overall frequency
    4. Backtest (Most Frequent)
    5. Backtest (Least Frequent)
    6. Confidence interval chart
    7. Monte carlo
    0. End
    ===========================
    Choice:
    ```

---
## ℹ️ 0. Information
- **Winning numbers** will be represented by:
    - Num1 - Num6 (Sorted in ascending order)
- **Additional number** will be represented by:
    - Num7

---

## 🧾 1. Getting Dataset
- For this project, I will be using data from a csv file downloaded from [this](https://en.lottolyzer.com/history/singapore/toto/page/1/per-page/50/summary-view)
 website, which contains past TOTO draw data starting from 2008.
 - To get the latest dataset, click on the CSV icon above the table on the left side and complete the capcha to download the file.

 ![CSV download guide](images/Picture1.png)
 - Ensure that the downloaded csv file is placed in the **"toto-number-analysis"** folder that you have cloned, and rename it to **"toto_results.csv"**.

---

## 🧹 2. Loading / Cleaning Data
- **2.1 Loading Data** - *load_data() functon*
    - To load data from the csv file, we will be using the ***"read_csv()"*** function within a ***"try except"*** block.
    - This allows us to catch potential errors such as:
        - ***FileNotFoundError*** - No file with that name is found
        - ***KeyError*** - Missing column

- **2.2 Cleaning Data** - *clean_data() function*
    - "Garbage in garbage out". Since we are using data from a third party and we do not know whether the data is clean or not, we have to clean the data to prevent bugs and ensure accuracy. To do so, we first have to identify what are some parameters the data has to satisfy.
    - For this dataset, we need to check for:
        - ***Missing values*** 
            - All TOTO draws have 6 numbers and 1 additional number
        - ***Incorrect data type***
            - All data should be integers
        - ***Range of values (Values have to be between 1 and 49)***
            - All values have to be between 1 and 49
        - ***Duplicate values in the same row***
            - The same number cannot appear twice in one draw
        - ***Order of values for Num1 - Num6***
            - Facilitates use of data later when performing analysis

---

## 📈 3. Data Analysis
- After loading and cleaning the dataset, we can finally start with analysing the data.
- **3.1 Invividual Bar Chart**
    - We first start by looking at the frequency at which each number appears for Num1 - Num7 by plotting them on a bar chart to see if there are any patterns.
    - **3.1.1 Num1 Frequency**
    
    ![CSV download guide](images/Num1_Freq.png)

    - **3.1.2 Num2 Frequency**

    ![CSV download guide](images/Num2_Freq.png)

    - **3.1.3 Num3 Frequency**

    ![CSV download guide](images/Num3_Freq.png)

    - **3.1.4 Num4 Frequency**

    ![CSV download guide](images/Num4_Freq.png)

    - **3.1.5 Num5 Frequency**

    ![CSV download guide](images/Num5_Freq.png)

    - **3.1.6 Num6 Frequency**

    ![CSV download guide](images/Num6_Freq.png)

    - **3.1.7 Num7 Frequency**
    
    ![CSV download guide](images/Num7_Freq.png)



































































## -
## -
## -
## -
## -
## -
## -
## -
## -
## -
## -
## -
## -
## -



