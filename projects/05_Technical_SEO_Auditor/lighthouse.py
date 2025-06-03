import os
import csv
from datetime import datetime
from urllib.parse import urlparse

from lighthouse import get_lighthouse_metrics
from broken_link_checker import find_broken_links
import requests
from bs4 import BeautifulSoup

def check_mobile(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X)"})
        soup = BeautifulSoup(response.text, 'html.parser')
        viewport = soup.find("meta", attrs={"name": "viewport"})
        return bool(viewport)
    except Exception:
        return False

def save_dict_to_csv(data_dict, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(data_dict.keys())
        writer.writerow(data_dict.values())

def save_list_to_csv(header, data_list, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for item in data_list:
            writer.writerow([item])

def run_audit(url):
    try:
        print(f"Starting audit for: {url}")
        
        # Mobile friendliness
        mobile_friendly = check_mobile(url)
        print(f"Mobile Friendly: {mobile_friendly}")
        
        # Lighthouse metrics (returns dict with scores or error)
        speed_metrics = get_lighthouse_metrics(url)
        print(f"Lighthouse metrics: {speed_metrics}")
        
        # Broken links
        broken_links = find_broken_links(url)
        print(f"Found {len(broken_links)} broken links.")
        
        # Prepare filenames for output CSVs
        parsed_url = urlparse(url).netloc.replace("www.", "")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        reports_dir = "reports"
        
        # Save mobile friendliness
        mobile_csv = os.path.join(reports_dir, f"{parsed_url}_{timestamp}_mobile.csv")
        save_dict_to_csv({"url": url, "mobile_friendly": mobile_friendly}, mobile_csv)
        
        # Save Lighthouse metrics (if no error)
        if "error" not in speed_metrics:
            lighthouse_csv = os.path.join(reports_dir, f"{parsed_url}_{timestamp}_lighthouse.csv")
            save_dict_to_csv(speed_metrics, lighthouse_csv)
        else:
            lighthouse_csv = None
        
        # Save broken links
        broken_csv = os.path.join(reports_dir, f"{parsed_url}_{timestamp}_broken_links.csv")
        save_list_to_csv(["broken_link"], broken_links, broken_csv)
        
        return {
            "mobile_friendly": mobile_friendly,
            "mobile_csv": mobile_csv,
            "page_speed": speed_metrics,
            "lighthouse_csv": lighthouse_csv,
            "broken_links": broken_links,
            "broken_links_csv": broken_csv
        }
        
    except Exception as e:
        print(f"Audit failed: {e}")
        return None


if __name__ == "__main__":
    url = "https:www.example.com/"
    result = run_audit(url)
    if result:
        print("\nAudit complete. Summary:")
        print(f"Mobile friendly: {result['mobile_friendly']} (CSV: {result['mobile_csv']})")
        if result['lighthouse_csv']:
            print(f"Lighthouse metrics saved to: {result['lighthouse_csv']}")
        else:
            print(f"Lighthouse error: {result['page_speed'].get('error')}")
        print(f"Broken links ({len(result['broken_links'])}) saved to: {result['broken_links_csv']}")
    else:
        print("Audit failed.")
