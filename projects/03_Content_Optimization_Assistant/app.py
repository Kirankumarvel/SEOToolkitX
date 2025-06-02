from flask import Flask, render_template, request, jsonify
from utils.seo_analyzer import analyze_content
from utils.openai_helper import get_ai_suggestions
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        target_keyword = request.form['keyword']
        
        # Basic SEO Analysis
        analysis = analyze_content(content, target_keyword)
        
        # AI-Powered Suggestions
        ai_suggestions = get_ai_suggestions(
            content=content,
            keyword=target_keyword
        )
        
        return jsonify({
            "analysis": analysis,
            "ai_suggestions": ai_suggestions
        })
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
