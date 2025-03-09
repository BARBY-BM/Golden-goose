import requests
from bs4 import BeautifulSoup
import openai
import time

openai.api_key = "your-api-key"

def get_trending_topics():
    url = "https://trends.google.com/trends/trendingsearches/daily"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    trends = [item.get_text() for item in soup.select(".title")]
    return trends[:5]  

def generate_content(topic):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI writer. Generate an engaging blog post."},
            {"role": "user", "content": f"Write an informative blog post about {topic}."}
        ]
    )
    return response['choices'][0]['message']['content']

def golden_goose_automation():
    print("🚀 Running Golden Goose Automation...")
    topics = get_trending_topics()
    for topic in topics:
        print(f"📈 Trending Topic: {topic}")
        content = generate_content(topic)
        filename = f"{topic.replace(' ', '_')}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"✅ Content saved: {filename}")
        time.sleep(2)

if __name__ == "__main__":
    golden_goose_automation()
