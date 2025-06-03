from lighthouse import get_lighthouse_metrics
from broken_link_checker import find_broken_links
import requests
from bs4 import BeautifulSoup

def run_audit(url):
    try:
        # Check mobile-friendliness
        mobile_friendly = check_mobile(url)
        
        # Get Lighthouse metrics
        speed_metrics = get_lighthouse_metrics(url)
        
        # Find broken links
        broken_links = find_broken_links(url)
        
        return {
            "mobile_friendly": mobile_friendly,
            "page_speed": speed_metrics,
            "broken_links": broken_links
        }
        
    except Exception as e:
        print(f"Audit failed: {str(e)}")
        return None

def check_mobile(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X)"})
        soup = BeautifulSoup(response.text, 'html.parser')
        viewport = soup.find("meta", attrs={"name": "viewport"})
        return bool(viewport)
    except:
        return False

if __name__ == "__main__":
    print(run_audit("https://example.com"))
