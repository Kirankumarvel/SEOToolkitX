
# 🗺️ XML Sitemap Generator

A lightweight, dependency‑simple Python tool to generate XML sitemaps from a list of URLs.  
Automatically splits large URL lists into multiple sitemap files and creates a sitemap index when needed – fully compliant with Google’s sitemap specifications.

## ✨ Features

- ✅ **Single or multiple sitemaps** – Handles up to 50,000 URLs per file (Google’s limit) and creates a `sitemap_index.xml` if you exceed it.
- ✅ **Absolute & relative URLs** – Add a `--base-url` to automatically prefix relative paths.
- ✅ **Clean, well‑formatted XML** – Uses `lxml` for standard‑compliant output.
- ✅ **No external APIs** – Pure Python, runs offline.
- ✅ **Ready for CI/CD** – Easily integrate into build pipelines or cron jobs.

## 📦 Installation

```bash
# Clone the repository (or copy the project folder)
git clone https://github.com/Kirankumarvel/SEOToolkitX.git
cd SEOToolkitX/projects/12_XML_SITEMAP_GENERATOR

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Usage

Prepare a text file with one URL per line (see `data/urls.txt` for an example). Then run:

```bash
python run.py data/urls.txt
```

If your URLs are relative (e.g., `/about`, `/contact`), add a base URL:

```bash
python run.py data/urls.txt --base-url https://example.com
```

Generated sitemap(s) will be saved in the `output/` folder.

### Example

**Input file (`urls.txt`):**
```
https://example.com/
https://example.com/about
https://example.com/contact
```

**Command:**
```bash
python run.py data/urls.txt
```

**Output (`output/sitemap_1.xml`):**
```xml
<?xml version='1.0' encoding='UTF-8'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
  </url>
  <url>
    <loc>https://example.com/about</loc>
  </url>
  <url>
    <loc>https://example.com/contact</loc>
  </url>
</urlset>
```

## 🔧 Configuration

Edit `config.py` to adjust these settings:

| Variable | Default | Description |
|----------|---------|-------------|
| `MAX_URLS_PER_SITEMAP` | 50000 | Max URLs per sitemap file (Google’s limit) |
| `OUTPUT_DIR` | `output` | Directory where sitemaps are saved |
| `SITEMAP_NAMESPACE` | `http://www.sitemaps.org/schemas/sitemap/0.9` | XML namespace (do not change unless required) |

## 📂 Project Structure

```
xml_sitemap_generator/
├── sitemap_generator/       # Core package
│   ├── __init__.py
│   ├── core.py              # Generation logic
│   └── cli.py               # Command‑line interface
├── data/                    # Example input
│   └── urls.txt
├── output/                  # Generated sitemaps (auto‑created)
├── config.py                # Settings
├── requirements.txt         # Dependencies
├── run.py                   # Entry point
└── README.md                # This file
```

## 🧪 Extending

You can easily add `<lastmod>`, `<changefreq>`, and `<priority>` tags.  
In `sitemap_generator/core.py`, inside the `generate_sitemap` function, uncomment and modify:

```python
lastmod = etree.SubElement(url_elem, "lastmod")
lastmod.text = datetime.now().date().isoformat()
```

## 🤝 Contributing

Feel free to open issues or pull requests in the [main SEOToolkitX repository](https://github.com/Kirankumarvel/SEOToolkitX).

## 📄 License

This project is part of SEOToolkitX – see the main repository for license information.
