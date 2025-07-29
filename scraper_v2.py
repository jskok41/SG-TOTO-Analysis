import requests
import pandas as pd
import time
import re
from bs4 import BeautifulSoup
import json
import os

def scrape_toto_results_v2():
    """
    Improved scraper with better error handling and debugging
    """
    print("=" * 60)
    print("Improved TOTO Results Scraper".center(60))
    print("-" * 60)
    
    # Try different URL patterns
    urls_to_try = [
        "https://en.lottolyzer.com/history/singapore/toto",
        "https://en.lottolyzer.com/history/singapore/toto/page/1/per-page/50/summary-view",
        "https://en.lottolyzer.com/history/singapore/toto/page/1/per-page/100/summary-view"
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Cache-Control': 'max-age=0'
    }
    
    for url in urls_to_try:
        print(f"\nTrying URL: {url}")
        try:
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            
            print(f"Status Code: {response.status_code}")
            print(f"Content Length: {len(response.content)}")
            
            # Save the HTML for debugging
            with open("debug_page.html", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("Saved HTML to debug_page.html for inspection")
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Try different table selectors
            table_selectors = [
                'table',
                'table.table',
                'table.table-striped',
                '.table',
                '#results-table',
                '[class*="table"]'
            ]
            
            table = None
            for selector in table_selectors:
                table = soup.select_one(selector)
                if table:
                    print(f"Found table with selector: {selector}")
                    break
            
            if not table:
                print("No table found. Looking for any data containers...")
                
                # Look for any divs that might contain results
                data_containers = soup.find_all(['div', 'section'], class_=re.compile(r'results|data|history'))
                print(f"Found {len(data_containers)} potential data containers")
                
                # Look for JSON data in script tags
                scripts = soup.find_all('script')
                for script in scripts:
                    if script.string and ('results' in script.string.lower() or 'data' in script.string.lower()):
                        print("Found script with potential data")
                        print(script.string[:200] + "...")
                
                continue
            
            # Extract data from table
            rows = table.find_all('tr')
            print(f"Found {len(rows)} rows in table")
            
            if len(rows) <= 1:
                print("No data rows found")
                continue
            
            # Print first few rows for debugging
            print("\nFirst few rows:")
            for i, row in enumerate(rows[:3]):
                cells = row.find_all(['td', 'th'])
                cell_texts = [cell.get_text(strip=True) for cell in cells]
                print(f"Row {i}: {cell_texts}")
            
            # Extract results
            results = []
            for row in rows[1:]:  # Skip header
                cells = row.find_all('td')
                if len(cells) >= 7:  # Need at least 7 cells (date + 6 numbers)
                    try:
                        # Extract date (usually first column)
                        date_text = cells[0].get_text(strip=True)
                        
                        # Extract numbers
                        numbers = []
                        for i in range(1, min(8, len(cells))):
                            cell_text = cells[i].get_text(strip=True)
                            # Try to extract number
                            num_match = re.search(r'\d+', cell_text)
                            if num_match:
                                num = int(num_match.group())
                                if 1 <= num <= 49:
                                    numbers.append(num)
                                else:
                                    numbers.append(None)
                            else:
                                numbers.append(None)
                        
                        # Ensure we have exactly 7 numbers
                        while len(numbers) < 7:
                            numbers.append(None)
                        
                        if len(numbers) == 7 and all(num is not None for num in numbers):
                            results.append({
                                'Date': date_text,
                                'Winning Number 1': numbers[0],
                                '2': numbers[1],
                                '3': numbers[2],
                                '4': numbers[3],
                                '5': numbers[4],
                                '6': numbers[5],
                                'Additional Number': numbers[6]
                            })
                    
                    except Exception as e:
                        print(f"Error parsing row: {e}")
                        continue
            
            if results:
                print(f"\nSuccessfully extracted {len(results)} results!")
                df = pd.DataFrame(results)
                df.to_csv("toto_results.csv", index=False)
                print("Results saved to toto_results.csv")
                return df
            else:
                print("No valid results extracted")
                
        except Exception as e:
            print(f"Error with URL {url}: {e}")
            continue
    
    print("\nAll URLs failed. Trying alternative approach...")
    return None

def try_api_endpoint():
    """
    Try to find and use API endpoints
    """
    print("\nTrying to find API endpoints...")
    
    # Common API patterns
    api_urls = [
        "https://en.lottolyzer.com/api/toto/results",
        "https://en.lottolyzer.com/api/singapore/toto",
        "https://en.lottolyzer.com/data/toto.json"
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    
    for url in api_urls:
        try:
            print(f"Trying API: {url}")
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                try:
                    data = response.json()
                    print("Found JSON API endpoint!")
                    print(f"Data keys: {list(data.keys()) if isinstance(data, dict) else 'Not a dict'}")
                    return data
                except json.JSONDecodeError:
                    print("Not JSON data")
        except Exception as e:
            print(f"API error: {e}")
    
    return None

def create_sample_data():
    """
    Create sample data for testing if scraping fails
    """
    print("\nCreating sample data for testing...")
    
    # Generate some realistic sample data
    import random
    from datetime import datetime, timedelta
    
    sample_data = []
    start_date = datetime(2020, 1, 1)
    
    for i in range(100):  # 100 sample draws
        date = start_date + timedelta(days=i*3)  # Every 3 days
        
        # Generate 6 unique numbers
        numbers = sorted(random.sample(range(1, 50), 6))
        
        # Generate additional number
        remaining = [n for n in range(1, 50) if n not in numbers]
        additional = random.choice(remaining)
        
        sample_data.append({
            'Date': date.strftime('%Y-%m-%d'),
            'Winning Number 1': numbers[0],
            '2': numbers[1],
            '3': numbers[2],
            '4': numbers[3],
            '5': numbers[4],
            '6': numbers[5],
            'Additional Number': additional
        })
    
    df = pd.DataFrame(sample_data)
    df.to_csv("toto_results.csv", index=False)
    print("Sample data created and saved to toto_results.csv")
    return df

def main():
    """
    Main function with multiple fallback strategies
    """
    print("TOTO Results Scraper v2")
    print("=" * 40)
    
    # Strategy 1: Try improved web scraping
    results = scrape_toto_results_v2()
    
    if results is not None:
        print(f"\n✅ Successfully scraped {len(results)} results!")
        return results
    
    # Strategy 2: Try API endpoints
    api_data = try_api_endpoint()
    if api_data is not None:
        print("✅ Found API data!")
        # Process API data here
        return api_data
    
    # Strategy 3: Create sample data for testing
    print("\n⚠️  Web scraping failed. Creating sample data for testing...")
    results = create_sample_data()
    
    print(f"\n✅ Created {len(results)} sample results for testing!")
    print("You can now run the analysis with this sample data.")
    print("To get real data, please manually download from:")
    print("https://en.lottolyzer.com/history/singapore/toto")
    
    return results

if __name__ == "__main__":
    main() 