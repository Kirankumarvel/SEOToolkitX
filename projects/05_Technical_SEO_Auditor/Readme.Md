# 05_Technical_SEO_Auditor

A Python-based technical SEO auditing toolkit that analyzes websites for key SEO factors such as mobile-friendliness, page speed (using Lighthouse metrics), and broken link detection. The tool generates comprehensive CSV reports for straightforward review and actionable insights.

---

## Features

- **Mobile Friendliness Check**  
  Detects whether a webpage includes a viewport meta tag, indicating mobile-friendly design.

- **Page Speed & Performance Metrics**  
  Retrieves Lighthouse audit metrics for performance, accessibility, SEO, and more.

- **Broken Link Checker**  
  Crawls a single page to identify broken links (links returning HTTP status codes 400 and above).

- **CSV Report Generation**  
  Saves audit results as timestamped CSV files in the `reports/` directory for easy reference.

---

## File Overview

- `auditor.py`  
  Main runner script that orchestrates checks, calls supporting modules, and saves results.

- `broken_link_checker.py`  
  Functions for identifying and saving broken links found on webpages.

- `lighthouse.py`  
  Manages mobile checks, Lighthouse metrics retrieval, and CSV output.

---

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Kirankumarvel/SEOToolkitX.git
    cd SEOToolkitX/projects/05_Technical_SEO_Auditor
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    <sub>Dependencies include: `requests`, `beautifulsoup4`</sub>

---

## Usage

Run the audit with:

```bash
python auditor.py
```

- By default, the tool audits `https://example.com`.
- To audit a different URL, modify the `url` variable in `auditor.py`, or add argument parsing as needed.

---

## How It Works

- **Mobile Friendliness:**  
  Checks for a viewport meta tag by fetching the page with a mobile user-agent.

- **Lighthouse Metrics:**  
  Uses `get_lighthouse_metrics(url)` from `lighthouse.py` to retrieve performance scores.

- **Broken Links:**  
  Parses all `<a>` tags on the page and checks link responses for error status codes (400+).

- **Reporting:**  
  Each audit generates three CSV files, saved in `reports/`, with filenames based on the domain and timestamp:
    - Mobile friendliness results
    - Lighthouse performance metrics
    - Broken links list

---

## Example Output

```
Saved results to:
  reports/example.com_20250603_141230_mobile.csv
  reports/example.com_20250603_141230_lighthouse.csv
  reports/example.com_20250603_141230_broken_links.csv
```

Sample console summary:
```json
{
  "mobile_friendly": true,
  "page_speed": {
    "performance": 0.92,
    "accessibility": 0.88,
    "seo": 0.95
  },
  "broken_links": [
    "https://example.com/broken-link-1",
    "https://example.com/broken-link-2"
  ]
}
```

---

## Notes

- The Lighthouse metrics function `get_lighthouse_metrics()` must be implemented or linked to a Lighthouse API/CLI wrapper.
- The broken link checker uses HEAD requests, with fallback to GET requests for robustness.
- Designed for single-page audits. Multi-page crawling could be added in future versions.

---

## License

MIT License — feel free to use and modify for your SEO auditing needs.

---

