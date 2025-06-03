import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import csv
import os

# Session to reuse connections
_session = requests.Session()
_session.headers.update(
    {"User-Agent": "BrokenLinkChecker/1.0 (+https://example.com/contact)"}
)

def find_broken_links(base_url: str, *, timeout: float = 10.0) -> list[str]:
    """
    Crawl `base_url` (single page) and return a list of absolute URLs
    that return a non-200 response (client or server error).
    """
    broken: list[str] = []

    try:
        resp = _session.get(base_url, timeout=timeout)
        resp.raise_for_status()
    except requests.RequestException as exc:
        print(f"Could not fetch {base_url}: {exc}")
        return broken

    soup = BeautifulSoup(resp.text, "html.parser")

    seen: set[str] = set()

    def is_checkable(href: str) -> bool:
        if not href or href.startswith(("#", "mailto:", "javascript:", "tel:")):
            return False
        return True

    for tag in soup.find_all("a"):
        href = tag.get("href")
        if not is_checkable(href):
            continue

        absolute = urljoin(base_url, href)

        if absolute in seen:
            continue
        seen.add(absolute)

        try:
            head = _session.head(absolute, allow_redirects=True, timeout=timeout)
            if head.status_code in (405, 501):
                head = _session.get(absolute, allow_redirects=True, timeout=timeout)

            if head.status_code >= 400:
                broken.append(absolute)
        except requests.RequestException:
            broken.append(absolute)

    return broken


def save_broken_links_to_csv(base_url: str, broken_links: list[str], output_dir="reports"):
    os.makedirs(output_dir, exist_ok=True)
    filename = base_url.replace("https://", "").replace("http://", "").replace("/", "_") + "_broken_links.csv"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Base URL", "Broken Link"])
        for link in broken_links:
            writer.writerow([base_url, link])

    print(f"Broken links saved to: {filepath}")


if __name__ == "__main__":
    base_url = "https://www.examples.com/"
    broken_links = find_broken_links(base_url)

    if broken_links:
        print(f"Found {len(broken_links)} broken links on {base_url}. Saving to CSV...")
        save_broken_links_to_csv(base_url, broken_links)
    else:
        print(f"No broken links found on {base_url}.")
