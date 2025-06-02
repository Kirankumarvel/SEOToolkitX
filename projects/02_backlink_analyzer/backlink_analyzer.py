import requests
from bs4 import BeautifulSoup
import pandas as pd
from mozapi import MozApi
import time

# Moz API Config (replace with your keys)
moz = MozApi(
    api_key=os.getenv("MOZ_API_KEY"),
    secret_key=os.getenv("MOZ_SECRET_KEY")
)

def get_backlinks(url):
    try:
        # Scrape backlinks (simplified for demo)
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(f"https://www.google.com/search?q=link:{url}", headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract links (example: Google search results)
        backlinks = []
        for link in soup.find_all("a", href=True):
            href = link["href"]
            if "http" in href and url not in href:
                backlinks.append({"Source URL": href})

        return backlinks[:10]  # Limit to 10 for demo

    except Exception as ex:
        print(f"Error fetching backlinks: {ex}")
        return []

def analyze_domain_authority(domains):
    results = []
    for domain in domains:
        try:
            metrics = moz.url_metrics(domain)
            results.append({
                "Domain": domain,
                "DA": metrics.get("da", "N/A"),
                "PA": metrics.get("pa", "N/A")
            })
            time.sleep(2)  # Rate limit
        except Exception as ex:
            print(f"Error analyzing {domain}: {ex}")
    return results

if __name__ == "__main__":
    competitor_url = "example.com"  # Replace with target URL
    backlinks = get_backlinks(competitor_url)
    
    if backlinks:
        # Extract domains from backlinks
        domains = list(set(bl["Source URL"].split("/")[2] for bl in backlinks))
        
        # Get DA/PA for each domain
        da_pa_results = analyze_domain_authority(domains)
        
        # Save to CSV
        df = pd.DataFrame(da_pa_results)
        print(df.head())
        df.to_csv("backlink_analysis.csv", index=False)
