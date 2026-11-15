import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def scrape_static_jobs():
    """
    Scrapes job postings from Hacker News using BeautifulSoup.
    Suitable for statically rendered HTML pages.
    """
    print("=== Web Scraping: Static Content (BeautifulSoup4) ===")
    
    target_url = "https://news.ycombinator.com/jobs"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    print(f"[INFO] Fetching HTML content from: {target_url}")
    try:
        response = requests.get(target_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        print("[INFO] Parsing HTML DOM...")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Locate the table rows containing job information
        job_rows = soup.find_all('tr', class_='athing')
        print(f"[SUCCESS] Found {len(job_rows)} job listings.\n")
        
        extracted_data = []
        for row in job_rows[:10]: # Process the first 10 rows
            title_element = row.find('span', class_='titleline').find('a')
            if title_element:
                job_title = title_element.text
                job_url = title_element['href']
                extracted_data.append({
                    "Job_Title": job_title,
                    "URL": job_url
                })
                
        df_jobs = pd.DataFrame(extracted_data)
        
        print("--- Extracted Data ---")
        print(df_jobs.to_string(index=False))
        print("----------------------\n")
        
        # Save results locally
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, "bs4_jobs_result.csv")
        df_jobs.to_csv(csv_path, index=False)
        print(f"[SUCCESS] Data saved to: {csv_path}")
        
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch the website: {e}")

if __name__ == "__main__":
    scrape_static_jobs()
