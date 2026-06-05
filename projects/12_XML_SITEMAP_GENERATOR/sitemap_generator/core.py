import os
import math
from typing import List, Optional
from lxml import etree
from datetime import datetime

# Optional config import – if you created config.py
try:
    from config import MAX_URLS_PER_SITEMAP, SITEMAP_NAMESPACE, OUTPUT_DIR
except ImportError:
    MAX_URLS_PER_SITEMAP = 50000
    SITEMAP_NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"
    OUTPUT_DIR = "output"

def generate_sitemap(urls: List[str], filename: str, base_url: Optional[str] = None) -> str:
    """
    Generates a single sitemap XML file from a list of URLs.

    :param urls: List of URL strings.
    :param filename: Output filename (e.g., 'sitemap1.xml').
    :param base_url: Optional base URL for relative paths (ignored if urls are absolute).
    :return: Path to the created file.
    """
    if not urls:
        raise ValueError("URL list cannot be empty")

    # Create root element
    root = etree.Element("urlset", xmlns=SITEMAP_NAMESPACE)

    for url in urls:
        url_elem = etree.SubElement(root, "url")
        loc = etree.SubElement(url_elem, "loc")
        # If a relative URL is given and base_url is set, prepend base_url
        if base_url and not url.startswith(("http://", "https://")):
            full_url = base_url.rstrip("/") + "/" + url.lstrip("/")
        else:
            full_url = url
        loc.text = full_url

        # Optional: add lastmod, changefreq, priority
        # For simplicity we omit them, but you can easily add:
        # lastmod = etree.SubElement(url_elem, "lastmod")
        # lastmod.text = datetime.now().date().isoformat()

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    file_path = os.path.join(OUTPUT_DIR, filename)

    # Write XML file
    with open(file_path, "wb") as f:
        f.write(etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8"))

    return file_path

def generate_sitemap_index(sitemap_files: List[str]) -> str:
    """
    Creates a sitemap index file referencing multiple sitemap files.
    Use this when you have more than MAX_URLS_PER_SITEMAP URLs.

    :param sitemap_files: List of sitemap filenames (e.g., ['sitemap1.xml', 'sitemap2.xml']).
    :return: Path to the sitemap index file.
    """
    root = etree.Element("sitemapindex", xmlns=SITEMAP_NAMESPACE)

    for sitemap in sitemap_files:
        sitemap_elem = etree.SubElement(root, "sitemap")
        loc = etree.SubElement(sitemap_elem, "loc")
        # Assuming sitemaps are placed in the same directory as the index
        loc.text = sitemap
        # Optional lastmod
        # lastmod = etree.SubElement(sitemap_elem, "lastmod")
        # lastmod.text = datetime.now().date().isoformat()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    index_path = os.path.join(OUTPUT_DIR, "sitemap_index.xml")
    with open(index_path, "wb") as f:
        f.write(etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8"))

    return index_path

def generate_sitemap_from_file(input_file: str, base_url: Optional[str] = None) -> None:
    """
    Reads URLs from a text file (one URL per line) and generates appropriate sitemap(s).
    Automatically splits into multiple sitemaps if needed.

    :param input_file: Path to a text file with URLs.
    :param base_url: Optional base URL to prefix relative paths.
    """
    with open(input_file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    if not urls:
        print("No valid URLs found in the file.")
        return

    total_urls = len(urls)
    num_sitemaps = math.ceil(total_urls / MAX_URLS_PER_SITEMAP)

    sitemap_filenames = []
    for i in range(num_sitemaps):
        start = i * MAX_URLS_PER_SITEMAP
        end = min((i + 1) * MAX_URLS_PER_SITEMAP, total_urls)
        chunk = urls[start:end]
        filename = f"sitemap_{i+1}.xml"
        generate_sitemap(chunk, filename, base_url)
        sitemap_filenames.append(filename)
        print(f"Generated {filename} with {len(chunk)} URLs.")

    if num_sitemaps > 1:
        index_path = generate_sitemap_index(sitemap_filenames)
        print(f"Generated sitemap index: {index_path}")
    else:
        print(f"Single sitemap created at output/{sitemap_filenames[0]}")