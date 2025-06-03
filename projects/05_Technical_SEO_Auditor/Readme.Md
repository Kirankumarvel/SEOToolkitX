
# 05\_Technical\_SEO\_Auditor

A Python-based technical SEO auditing toolkit to analyze websites for key SEO factors such as mobile-friendliness, page speed (using Lighthouse metrics), and broken link detection. The tool generates comprehensive CSV reports for easy review and follow-up action.

---

## Features

* **Mobile Friendliness Check**
  Detects if a webpage contains a viewport meta tag indicating mobile-friendly design.

* **Page Speed & Performance Metrics**
  Retrieves Lighthouse audit metrics for performance, accessibility, SEO, and more.

* **Broken Link Checker**
  Crawls a single page to identify broken links (links returning HTTP status codes 400 and above).

* **CSV Report Generation**
  Saves audit results into timestamped CSV files in a `reports/` folder for easy reference.

---

## Files

* `auditor.py`
  Main audit runner that orchestrates checks, calls other modules, and saves results.

* `broken_link_checker.py`
  Contains functions to find and save broken links on a given webpage.

* `lighthouse.py`
  Handles mobile check and manages Lighthouse metrics retrieval and CSV saving.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Kirankumarvel/05_Technical_SEO_Auditor.git
   cd 05_Technical_SEO_Auditor
   ```

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   *Dependencies include:* `requests`, `beautifulsoup4`

---

## Usage

Run the audit by executing the main script:

```bash
python auditor.py
```

By default, it audits `https://example.com`. To audit another URL, modify the `url` variable in `auditor.py` or integrate argument parsing.

---

## How It Works

* **Mobile Friendliness**
  Checks presence of a viewport meta tag by requesting the page with a mobile user-agent.

* **Lighthouse Metrics**
  Calls `get_lighthouse_metrics(url)` from `lighthouse.py` (assumed implemented) to retrieve performance scores.

* **Broken Links**
  Parses all anchor tags (`<a>`) on the page and checks if links respond with status codes indicating errors (400+).

* **Reporting**
  Generates three CSV files per audit:

  * Mobile friendliness result
  * Lighthouse performance metrics
  * Broken links list

These are saved under the `reports/` directory with filenames based on the audited domain and timestamp.

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

* The Lighthouse metric fetching function `get_lighthouse_metrics()` must be properly implemented or linked to an existing Lighthouse API or CLI wrapper.
* The broken link checker uses HEAD requests with fallback GET requests for robustness.
* Designed for single-page audits; multi-page crawling can be added in future versions.

---

## License

MIT License — feel free to use and modify for your SEO auditing needs.

---

If you want, I can help you add argument parsing or enhance the README with examples on how to extend this tool. Just let me know!
