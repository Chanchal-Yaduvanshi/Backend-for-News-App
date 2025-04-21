# news_proxy.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_KEY = "2d5ccda8dcaa467ca62e5b0c5aa995cf"

@app.route("/news", methods=["GET"])
def get_news():
    category = request.args.get("category", "general")
    country = request.args.get("country", "us")
    url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={API_KEY}"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)

