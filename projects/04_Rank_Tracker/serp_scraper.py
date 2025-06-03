from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scrape_serp(keyword, location="US"):
    try:
        options = Options()
        options.add_argument("--headless")  # Run without GUI
        driver = webdriver.Chrome(options=options)
        
        # Simulate location
        driver.get(f"https://www.google.com/search?q={keyword}&gl={location}")
        time.sleep(3)  # Allow page load
        
        # Extract top 100 organic results
        results = driver.find_elements(By.CSS_SELECTOR, "div.g a")
        urls = [result.get_attribute("href") for result in results if result.get_attribute("href")]
        
        driver.quit()
        return urls[:100]  # Return top 100
        
    except Exception as e:
        print(f"Scraping error: {str(e)}")
        return []
