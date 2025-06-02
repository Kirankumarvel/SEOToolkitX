
# 🔍 Keyword Research Tool  
*Fetch keyword suggestions, search volume, and competition data using Google Ads API*  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Google Ads API](https://img.shields.io/badge/API-Google_Ads-orange) ![SEO](https://img.shields.io/badge/Use%20Case-SEO-brightgreen)

---

## 🚀 **Overview**  
This Python script automates keyword research by fetching:  
- **Keyword suggestions**  
- **Average monthly searches**  
- **Competition level**  
from Google Ads API. Ideal for SEO professionals and content strategists.

---

## ⚙️ **Tech Stack**  
- **Python 3.8+**  
- `google-api-python-client` (Google Ads API integration)  
- `pandas` (Data analysis and CSV export)  
- `python-dotenv` (Secure API key management)  

---

## 🛠️ **Setup Instructions**  

### 1. **Install Dependencies**  
```bash
pip install google-ads pandas python-dotenv
```

### 2. **Configure Google Ads API**  
Create a `.env` file in your project root with:  
```ini
GOOGLE_ADS_CUSTOMER_ID=1234567890
GOOGLE_ADS_DEVELOPER_TOKEN=your_dev_token
GOOGLE_ADS_CLIENT_ID=your_client_id
GOOGLE_ADS_CLIENT_SECRET=your_client_secret
GOOGLE_ADS_REFRESH_TOKEN=your_refresh_token
```
*Replace placeholders with your [Google Ads API credentials](https://developers.google.com/google-ads/api/docs/get-started).*

### 3. **Run the Script**  
```bash
python projects/01_keyword_research_tool/keyword_tool.py
```
*Outputs a `keyword_results.csv` file with data.*

---

## 📊 **Sample Output**  
| Keyword              | Avg. Monthly Searches | Competition  |  
|----------------------|-----------------------|--------------|  
| "best running shoes" | 165,000               | HIGH         |  
| "top running shoes"  | 74,000                | MEDIUM       |  

---

## 🚨 **Troubleshooting**  
- **Error: "Invalid API credentials"**  
  Double-check your `.env` file and [Google Ads API access](https://developers.google.com/google-ads/api/docs/access).  
- **No results returned**  
  Ensure your target location ID is valid (e.g., `2840` for USA).  

---

## 📜 **License**  
MIT License - Free for commercial and personal use.  

---

## 🤝 **Contribute**  
Found a bug? Want to add features?  
1. Fork the repository.  
2. Create a PR with your changes.  

---

## ✨ **Pro Tip**  
Pair this with the [Content Optimizer](link-to-project) in `SEOToolkitX` for end-to-end SEO workflow automation!  

```


