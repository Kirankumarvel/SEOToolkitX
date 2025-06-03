from lighthouse import get_lighthouse_metrics
from broken_link_checker import find_broken_links
import requests
from bs4 import BeautifulSoup
import os
import csv
from datetime import datetime
from urllib.parse import urlparse

def run_audit(url):
    try:
        # Check mobile-friendliness
        mobile_friendly = check_mobile(url)

        # Get Lighthouse metrics
        speed_metrics = get_lighthouse_metrics(url)

        # Find broken links
        broken_links = find_broken_links(url)

        # Save results to CSV
        save_results_to_csv(url, mobile_friendly, speed_metrics, broken_links)

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
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X)"}
        )
        soup = BeautifulSoup(response.text, 'html.parser')
        viewport = soup.find("meta", attrs={"name": "viewport"})
        return bool(viewport)
    except:
        return False


def save_results_to_csv(url, mobile_friendly, speed_metrics, broken_links):
    # Prepare output folder and filename base
    os.makedirs("reports", exist_ok=True)
    parsed_url = urlparse(url).netloc.replace("www.", "")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Mobile friendliness CSV
    mobile_csv = os.path.join("reports", f"{parsed_url}_{timestamp}_mobile.csv")
    with open(mobile_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["url", "mobile_friendly"])
        writer.writerow([url, mobile_friendly])

    # Lighthouse CSV (only if no error)
    if "error" not in speed_metrics:
        lighthouse_csv = os.path.join("reports", f"{parsed_url}_{timestamp}_lighthouse.csv")
        with open(lighthouse_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(speed_metrics.keys())
            writer.writerow(speed_metrics.values())
    else:
        lighthouse_csv = None
        print(f"Lighthouse error: {speed_metrics['error']}")

    # Broken links CSV
    broken_csv = os.path.join("reports", f"{parsed_url}_{timestamp}_broken_links.csv")
    with open(broken_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["broken_link"])
        for link in broken_links:
            writer.writerow([link])

    print(f"Saved results to:\n  {mobile_csv}\n  {lighthouse_csv if lighthouse_csv else 'No Lighthouse CSV'}\n  {broken_csv}")


if __name__ == "__main__":
    url = "https://example.com"
    result = run_audit(url)
    print(result)
