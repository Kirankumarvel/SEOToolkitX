import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def setup_driver():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        
        # Point to your chromedriver.exe
        service = Service(executable_path=r'C:\path\to\chromedriver.exe')  # Update this path
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        print(f"Driver setup failed: {str(e)}")
        return None

def scrape_serp(keyword, location="US"):
    driver = setup_driver()
    if not driver:
        return []
    
    try:
        driver.get(f"https://www.google.com/search?q={keyword}&gl={location}")
        results = driver.find_elements("css selector", "div.g a")
        urls = [result.get_attribute("href") for result in results if result.get_attribute("href")]
        return urls[:100]
    finally:
        driver.quit()

def track_rankings(keyword, website_url):
    try:
        rankings = scrape_serp(keyword)
        position = next((i + 1 for i, url in enumerate(rankings) if website_url in url), "Not in top 100")

        conn = sqlite3.connect('rankings.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS rankings
                     (date TEXT, keyword TEXT, position TEXT)''')
        c.execute("INSERT INTO rankings VALUES (?, ?, ?)",
                (datetime.now().strftime("%Y-%m-%d"), keyword, str(position)))
        conn.commit()
        return position
    except Exception as e:
        print(f"Tracking error: {str(e)}")
        return None

if __name__ == "__main__":
    print(f"Current rank: {track_rankings('best running shoes', 'nike.com')}")
