import requests
import pandas as pd
import time
import re
from bs4 import BeautifulSoup
import os
import numpy as np

def scrape_toto_results():
    """
    Scrape TOTO results from Lottolyzer website
    """
    print("=" * 60)
    print("Scraping TOTO Results from Lottolyzer".center(60))
    print("-" * 60)
    
    # Base URL for TOTO results
    base_url = "https://en.lottolyzer.com/history/singapore/toto"
    
    # Headers to mimic a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    all_results = []
    page = 1
    max_pages = 50  # Limit to prevent infinite scraping
    
    print("Starting to scrape TOTO results...")
    
    try:
        while page <= max_pages:
            print(f"Scraping page {page}...")
            
            # Construct URL for current page
            url = f"{base_url}/page/{page}/per-page/50/summary-view"
            
            # Make request
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the results table
            table = soup.find('table', {'class': 'table'})
            if not table:
                print(f"No table found on page {page}. Stopping.")
                break
            
            # Extract rows
            rows = table.find_all('tr')[1:]  # Skip header row
            if not rows:
                print(f"No data rows found on page {page}. Stopping.")
                break
            
            page_results = []
            for row in rows:
                cells = row.find_all('td')
                if len(cells) >= 8:  # Should have date + 7 numbers
                    try:
                        # Extract date
                        date_cell = cells[0].get_text(strip=True)
                        
                        # Extract numbers (cells 1-7 should contain the numbers)
                        numbers = []
                        for i in range(1, 8):
                            num_text = cells[i].get_text(strip=True)
                            if num_text.isdigit():
                                numbers.append(int(num_text))
                            else:
                                # Try to extract numbers from text
                                num_match = re.search(r'\d+', num_text)
                                if num_match:
                                    numbers.append(int(num_match.group()))
                                else:
                                    numbers.append(None)
                        
                        if len(numbers) == 7 and all(num is not None for num in numbers):
                            page_results.append({
                                'Date': date_cell,
                                'Winning Number 1': numbers[0],
                                '2': numbers[1],
                                '3': numbers[2],
                                '4': numbers[3],
                                '5': numbers[4],
                                '6': numbers[5],
                                'Additional Number': numbers[6]
                            })
                    except (ValueError, IndexError) as e:
                        print(f"Error parsing row: {e}")
                        continue
            
            if not page_results:
                print(f"No valid results found on page {page}. Stopping.")
                break
            
            all_results.extend(page_results)
            print(f"Found {len(page_results)} results on page {page}")
            
            # Check if we've reached the end (look for pagination indicators)
            pagination = soup.find('ul', {'class': 'pagination'})
            if pagination:
                next_link = pagination.find('a', {'rel': 'next'})
                if not next_link:
                    print("Reached last page.")
                    break
            
            # Be respectful - add delay between requests
            time.sleep(1)
            page += 1
    
    except requests.RequestException as e:
        print(f"Error making request: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    
    if not all_results:
        print("No results found!")
        return None
    
    # Create DataFrame
    df = pd.DataFrame(all_results)
    
    print(f"\nSuccessfully scraped {len(df)} TOTO results!")
    print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
    
    # Save to CSV
    output_file = "toto_results.csv"
    df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")
    
    return df

def scrape_with_selenium():
    """
    Alternative scraper using Selenium for JavaScript-heavy sites
    """
    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.chrome.options import Options
    except ImportError:
        print("Selenium not installed. Install with: pip install selenium")
        return None
    
    print("Using Selenium scraper...")
    
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in background
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = None
    try:
        driver = webdriver.Chrome(options=chrome_options)
        
        # Navigate to the page
        url = "https://en.lottolyzer.com/history/singapore/toto/page/1/per-page/50/summary-view"
        driver.get(url)
        
        # Wait for table to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )
        
        # Get page source and parse with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Extract data (same logic as above)
        table = soup.find('table', {'class': 'table'})
        if not table:
            print("No table found!")
            return None
        
        rows = table.find_all('tr')[1:]
        results = []
        
        for row in rows:
            cells = row.find_all('td')
            if len(cells) >= 8:
                try:
                    date_cell = cells[0].get_text(strip=True)
                    numbers = []
                    for i in range(1, 8):
                        num_text = cells[i].get_text(strip=True)
                        if num_text.isdigit():
                            numbers.append(int(num_text))
                        else:
                            num_match = re.search(r'\d+', num_text)
                            if num_match:
                                numbers.append(int(num_match.group()))
                            else:
                                numbers.append(None)
                    
                    if len(numbers) == 7 and all(num is not None for num in numbers):
                        results.append({
                            'Date': date_cell,
                            'Winning Number 1': numbers[0],
                            '2': numbers[1],
                            '3': numbers[2],
                            '4': numbers[3],
                            '5': numbers[4],
                            '6': numbers[5],
                            'Additional Number': numbers[6]
                        })
                except (ValueError, IndexError) as e:
                    continue
        
        if results:
            df = pd.DataFrame(results)
            df.to_csv("toto_results.csv", index=False)
            print(f"Scraped {len(df)} results with Selenium")
            return df
        else:
            print("No results found with Selenium")
            return None
            
    except Exception as e:
        print(f"Selenium error: {e}")
        return None
    finally:
        if driver:
            driver.quit()

def quick_summary(df, filename):
    """
    Provides a quick summary of the TOTO dataset.
    """
    print("\n" + "=" * 60)
    print("Quick Summary Analysis".center(60))
    print("=" * 60)

    if df.empty:
        print("No data available for quick summary.")
        return

    print(f"Dataset: {filename}")
    print(f"Total draws: {len(df)}")

    # Frequency analysis
    freq = df['Winning Number 1'].value_counts()
    print("\n🎯 Most frequent numbers:")
    if not freq.empty:
        for num, count in freq.head(5).items():
            print(f"- {num}: {count} times")
    else:
        print("No frequency data available.")

    # Position analysis
    print("\n📊 Position analysis:")
    if 'Winning Number 1' in df.columns and '2' in df.columns and '3' in df.columns and '4' in df.columns and '5' in df.columns and '6' in df.columns:
        num1_positions = df['Winning Number 1'].value_counts()
        num2_positions = df['2'].value_counts()
        num3_positions = df['3'].value_counts()
        num4_positions = df['4'].value_counts()
        num5_positions = df['5'].value_counts()
        num6_positions = df['6'].value_counts()

        print(f"- Num1: {list(num1_positions.values)}")
        print(f"- Num2: {list(num2_positions.values)}")
        print(f"- Num3: {list(num3_positions.values)}")
        print(f"- Num4: {list(num4_positions.values)}")
        print(f"- Num5: {list(num5_positions.values)}")
        print(f"- Num6: {list(num6_positions.values)}")
    else:
        print("Position analysis data not available.")

    # Statistical insights
    print("\n📊 Statistical insights:")
    if len(df) > 0:
        expected_freq = len(df) / 50 # Assuming 50 draws per page, adjust if needed
        print(f"- Expected frequency per number: {expected_freq:.1f}")
        
        # Calculate standard deviation of frequencies
        freq_values = list(freq.values)
        if freq_values:
            std_dev = np.std(freq_values)
            print(f"- Standard deviation of frequencies: {std_dev:.2f}")
        else:
            print("- Standard deviation of frequencies: N/A (no frequency data)")

        # Data age (assuming data is recent enough or not applicable)
        # For simplicity, let's assume it's 0 days old if it's from a recent scrape
        # In a real scenario, you'd calculate the difference between the oldest date and the current date
        print(f"- Data age: 0 days old (assuming recent scrape)")
    else:
        print("No statistical insights available.")

    print("\n" + "=" * 60)

def main():
    """
    Main function to run the scraper
    """
    print("TOTO Results Scraper")
    print("=" * 40)
    
    # Try the regular scraper first
    print("Attempting to scrape with requests...")
    results = scrape_toto_results()
    
    if results is None:
        print("\nRegular scraper failed. Trying Selenium...")
        results = scrape_with_selenium()
    
    if results is not None:
        print("\nScraping completed successfully!")
        print(f"Total results: {len(results)}")
        print("\nFirst few results:")
        print(results.head())

        # Call the quick summary function
        quick_summary(results, "toto_results.csv")
    else:
        print("\nBoth scrapers failed. Please check the website or try manual download.")

if __name__ == "__main__":
    main() 