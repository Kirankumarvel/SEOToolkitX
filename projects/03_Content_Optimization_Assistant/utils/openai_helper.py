import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_suggestions(content, keyword):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an SEO expert."},
                {"role": "user", "content": f"Suggest SEO improvements for this content about {keyword}:\n\n{content}"}
            ],
            temperature=0.7
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"AI suggestion error: {str(e)}"
