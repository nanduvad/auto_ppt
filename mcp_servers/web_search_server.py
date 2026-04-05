import requests

class WebSearchServer:
    def search(self, query):
        try:
            url = f"https://api.duckduckgo.com/?q={query}&format=json"
            res = requests.get(url).json()
            return res.get("AbstractText", "")
        except:
            return "No data found"