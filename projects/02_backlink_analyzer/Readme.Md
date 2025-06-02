# 🔗 Backlink Analyzer  
*Scrapes competitor backlinks and analyzes Domain Authority (DA/PA) using Moz API*  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Moz API](https://img.shields.io/badge/API-Moz-orange) ![SEO](https://img.shields.io/badge/Use%20Case-SEO-brightgreen)

---

## 🚀 **Overview**  
This Python tool helps you:  
- **Scrape competitor backlinks** from Google search results  
- **Analyze Domain Authority (DA) and Page Authority (PA)** using Moz API  
- **Export data to CSV** for further analysis  

Perfect for competitive SEO analysis and link-building campaigns.

---

## ⚙️ **Tech Stack**  
- **Python 3.8+**  
- `requests` (HTTP requests)  
- `beautifulsoup4` (HTML parsing)  
- `pandas` (Data export)  
- `mozapi` (Moz API integration)  

---

## 🛠️ **Setup Instructions**  

### 1. **Install Dependencies**  
```bash
pip install requests beautifulsoup4 pandas mozapi
```

### 2. **Configure Moz API**  
1. Sign up for [Moz API](https://moz.com/products/api)  
2. Create a `.env` file in your project root with:  
```ini
MOZ_API_KEY=your_access_id
MOZ_SECRET_KEY=your_secret_key
```

### 3. **Run the Script**  
```bash
python projects/02_backlink_analyzer/backlink_analyzer.py
```
*Outputs a `backlink_analysis.csv` file with results.*

---

## 📊 **Sample Output**  
| Domain          | DA  | PA  |  
|-----------------|-----|-----|  
| example.com     | 42  | 34  |  
| competitor.org  | 68  | 52  |  

---

## 🚨 **Troubleshooting**  
- **Error: "Moz API Limit Reached"**  
  The free tier has rate limits (2s between requests). Upgrade for higher limits.  
- **No backlinks found**  
  Try different search operators like `link:example.com -site:example.com`  

---

## 🔐 **Important Notes**  
- Google may block scrapers - use proxies if running at scale  
- Free Moz API tier has limited queries/month  
- For production use, consider:  
  - Switching to Ahrefs/SEMrush API  
  - Adding proxy rotation  

---

## 📜 **License**  
MIT License - Free for commercial and personal use.  

---

## 🤝 **Roadmap & Contributions**  
Planned features:  
- [ ] Add Ahrefs/SEMrush API support  
- [ ] Include spam score analysis  
- [ ] Build a dashboard interface  

**Contribute by:**  
1. Forking the repository  
2. Submitting a PR with your improvements  

---

## 💡 **Pro Tip**  
Combine this with the [Keyword Research Tool](link-to-keyword-tool) in `SEOToolkitX` for complete competitor analysis!  



Need help setting up proxies for large-scale scraping? Let me know! 🛡️
