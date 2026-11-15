import time
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def scrape_dynamic_content(keyword="Data Engineer Hiring"):
    """
    Scrapes Javascript-rendered content using Selenium WebDriver.
    Simulates human interactions (typing, clicking, scrolling) on Hacker News Algolia Search.
    """
    print("=== Web Scraping: Dynamic Content (Selenium) ===\n")
    print("[INFO] Initializing Headless Chrome Browser...")
    
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless=new') # Uncomment to run entirely in the background
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        # Target Algolia Search for Hacker News (Javascript/React rendered)
        target_url = "https://hn.algolia.com/"
        print(f"[INFO] Navigating to: {target_url}")
        driver.get(target_url)
        time.sleep(3)
        
        print(f"[INFO] Locating search bar and typing: '{keyword}'...")
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='search']"))
        )
        
        search_input.clear()
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.RETURN)
        
        print("[INFO] Waiting for Javascript to fetch and render results...")
        time.sleep(5)
        
        print("[INFO] Simulating scroll to load lazy elements...")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        
        # Locate result items
        items = driver.find_elements(By.XPATH, "//article | //div[contains(@class, 'Story')]")
        print(f"[SUCCESS] Found {len(items)} search results.")
        
        extracted_data = []
        for item in items[:10]: 
            try:
                # Extract inner text and format it
                text = item.text.strip().replace('\n', ' | ')
                if text:
                    extracted_data.append({"Content": text})
            except Exception as e:
                continue
                
        df = pd.DataFrame(extracted_data)
        
        print("\n--- Extracted Data ---")
        print(df.to_string(index=False))
        print("----------------------\n")
        
        # Save results locally
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, "selenium_hn_result.csv")
        df.to_csv(csv_path, index=False)
        print(f"[SUCCESS] Data saved to: {csv_path}")
        
    except Exception as e:
        print(f"[ERROR] Selenium automation failed: {e}")
        
    finally:
        print("[INFO] Shutting down browser instance...")
        driver.quit()

if __name__ == "__main__":
    scrape_dynamic_content("Data Engineer Hiring")
