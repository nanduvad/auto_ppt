from agents.web_search_agent import WebSearchAgent
from agents.ppt_agent import PPTAgent
from agents.file_agent import FileAgent

class Controller:

    def __init__(self):
        self.web = WebSearchAgent()
        self.ppt = PPTAgent()
        self.file = FileAgent()

    def run(self, topic, theme, save_path):

        print("🔎 Searching web...")
        content = self.web.search(topic)

        print("🧠 Generating PPT...")
        presentation = self.ppt.create_ppt(
            topic, content, theme
        )

        print("💾 Saving file...")
        result = self.file.save(presentation, save_path)

        return result