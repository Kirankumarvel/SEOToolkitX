import nltk
from nltk.tokenize import word_tokenize
from textstat import flesch_reading_ease
import re

nltk.download('punkt')

def analyze_content(content, target_keyword):
    # Keyword Density
    words = word_tokenize(content.lower())
    keyword_count = words.count(target_keyword.lower())
    keyword_density = (keyword_count / len(words)) * 100 if words else 0
    
    # Readability
    readability = flesch_reading_ease(content)
    
    # Meta Analysis
    title = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    meta_desc = re.search(r'<meta name="description" content="(.*?)"', content, re.IGNORECASE)
    
    return {
        "keyword_density": round(keyword_density, 2),
        "readability_score": round(readability, 2),
        "title_exists": bool(title),
        "meta_description_exists": bool(meta_desc)
    }