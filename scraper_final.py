import requests
import pandas as pd
import time
import re
from bs4 import BeautifulSoup
import json
import os

def scrape_toto_results_final():
    """
    Final scraper that handles the actual website format
    """
    print("=" * 60)
    print("Final TOTO Results Scraper".center(60))
    print("-" * 60)
    
    url = "https://en.lottolyzer.com/history/singapore/toto/page/1/per-page/50/summary-view"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        print(f"Scraping URL: {url}")
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        print(f"Status Code: {response.status_code}")
        print(f"Content Length: {len(response.content)}")
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table
        table = soup.find('table')
        if not table:
            print("No table found!")
            return None
        
        rows = table.find_all('tr')
        print(f"Found {len(rows)} rows in table")
        
        if len(rows) <= 2:  # Need at least header + data
            print("Not enough data rows")
            return None
        
        # Extract results
        results = []
        for row in rows[2:]:  # Skip the two header rows
            cells = row.find_all('td')
            if len(cells) >= 4:  # Need at least Draw, Date, Winning No., Addl No.
                try:
                    # Extract draw number
                    draw_text = cells[0].get_text(strip=True)
                    
                    # Extract date
                    date_text = cells[1].get_text(strip=True)
                    
                    # Extract winning numbers (comma-separated)
                    winning_text = cells[2].get_text(strip=True)
                    
                    # Extract additional number
                    additional_text = cells[3].get_text(strip=True)
                    
                    # Parse winning numbers
                    winning_numbers = []
                    if winning_text:
                        # Split by comma and clean up
                        numbers = [num.strip() for num in winning_text.split(',')]
                        for num in numbers:
                            if num.isdigit():
                                winning_numbers.append(int(num))
                    
                    # Parse additional number
                    additional_number = None
                    if additional_text and additional_text.isdigit():
                        additional_number = int(additional_text)
                    
                    # Validate we have the right number of numbers
                    if len(winning_numbers) == 6 and additional_number is not None:
                        # Sort the winning numbers (as per TOTO rules)
                        winning_numbers.sort()
                        
                        results.append({
                            'Date': date_text,
                            'Winning Number 1': winning_numbers[0],
                            '2': winning_numbers[1],
                            '3': winning_numbers[2],
                            '4': winning_numbers[3],
                            '5': winning_numbers[4],
                            '6': winning_numbers[5],
                            'Additional Number': additional_number
                        })
                        
                        print(f"Parsed: {date_text} - {winning_numbers} + {additional_number}")
                
                except Exception as e:
                    print(f"Error parsing row: {e}")
                    continue
        
        if results:
            print(f"\nSuccessfully extracted {len(results)} results!")
            df = pd.DataFrame(results)
            df.to_csv("toto_results.csv", index=False)
            print("Results saved to toto_results.csv")
            
            # Show sample of results
            print("\nFirst few results:")
            print(df.head())
            
            return df
        else:
            print("No valid results extracted")
            return None
            
    except Exception as e:
        print(f"Error: {e}")
        return None

def scrape_multiple_pages():
    """
    Scrape multiple pages to get more historical data
    """
    print("\n" + "=" * 60)
    print("Scraping Multiple Pages".center(60))
    print("-" * 60)
    
    all_results = []
    page = 1
    max_pages = 35  # Should cover several years of data
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    while page <= max_pages:
        print(f"\nScraping page {page}...")
        
        url = f"https://en.lottolyzer.com/history/singapore/toto/page/{page}/per-page/50/summary-view"
        
        try:
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table')
            
            if not table:
                print(f"No table found on page {page}. Stopping.")
                break
            
            rows = table.find_all('tr')
            if len(rows) <= 2:
                print(f"No data rows found on page {page}. Stopping.")
                break
            
            page_results = []
            for row in rows[2:]:  # Skip header rows
                cells = row.find_all('td')
                if len(cells) >= 4:
                    try:
                        date_text = cells[1].get_text(strip=True)
                        winning_text = cells[2].get_text(strip=True)
                        additional_text = cells[3].get_text(strip=True)
                        
                        # Parse winning numbers
                        winning_numbers = []
                        if winning_text:
                            numbers = [num.strip() for num in winning_text.split(',')]
                            for num in numbers:
                                if num.isdigit():
                                    winning_numbers.append(int(num))
                        
                        # Parse additional number
                        additional_number = None
                        if additional_text and additional_text.isdigit():
                            additional_number = int(additional_text)
                        
                        if len(winning_numbers) == 6 and additional_number is not None:
                            winning_numbers.sort()
                            
                            page_results.append({
                                'Date': date_text,
                                'Winning Number 1': winning_numbers[0],
                                '2': winning_numbers[1],
                                '3': winning_numbers[2],
                                '4': winning_numbers[3],
                                '5': winning_numbers[4],
                                '6': winning_numbers[5],
                                'Additional Number': additional_number
                            })
                    
                    except Exception as e:
                        continue
            
            if not page_results:
                print(f"No valid results on page {page}. Stopping.")
                break
            
            all_results.extend(page_results)
            print(f"Found {len(page_results)} results on page {page}")
            
            # Be respectful - add delay between requests
            time.sleep(1)
            page += 1
            
        except Exception as e:
            print(f"Error on page {page}: {e}")
            break
    
    if all_results:
        print(f"\nTotal results scraped: {len(all_results)}")
        df = pd.DataFrame(all_results)
        df.to_csv("toto_results.csv", index=False)
        print("All results saved to toto_results.csv")
        
        # Show date range
        print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
        
        return df
    else:
        print("No results found across all pages")
        return None

def main():
    """
    Main function to run the final scraper
    """
    print("TOTO Results Scraper - Final Version")
    print("=" * 40)
    
    # Try single page first
    print("Attempting to scrape single page...")
    results = scrape_toto_results_final()
    
    if results is not None and len(results) > 0:
        print(f"\n✅ Successfully scraped {len(results)} results from single page!")
        
        # Ask if user wants to scrape more pages
        print("\nWould you like to scrape more historical data? (y/n)")
        choice = input().lower().strip()
        
        if choice in ['y', 'yes']:
            print("Scraping multiple pages for more historical data...")
            full_results = scrape_multiple_pages()
            if full_results is not None:
                print(f"\n✅ Total results: {len(full_results)}")
                return full_results
        
        return results
    
    else:
        print("\nSingle page scraping failed. Trying multiple pages...")
        results = scrape_multiple_pages()
        
        if results is not None:
            print(f"\n✅ Successfully scraped {len(results)} results!")
            return results
        else:
            print("\n❌ All scraping attempts failed.")
            print("Please manually download the data from:")
            print("https://en.lottolyzer.com/history/singapore/toto")
            return None

if __name__ == "__main__":
    main() 