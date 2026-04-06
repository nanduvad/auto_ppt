from ddgs import DDGS
from agents.base_agent import BaseAgent


class WebSearchAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            "web_search",
            "Summarize search results for PPT content."
        )

    def search(self, topic):

        results = []

        with DDGS() as ddgs:
            for r in ddgs.text(topic, max_results=5):
                results.append(r["body"])

        combined = "\n".join(results)

        return self.think(combined)