from transformers import pipeline
from config.settings import Config
from mcp_servers.ppt_server import PPTServer
from .prompt_template import SYSTEM_PROMPT


class PPTAgent:
    def __init__(self):
        self.llm = pipeline(
            "text-generation",
            model=Config.MODEL_ID
        )

        self.ppt = PPTServer()

    def ask_llm(self, prompt):
        try:
            response = self.llm(prompt, max_length=150)
            return response[0]["generated_text"].strip()
        except Exception as e:
            print("LLM ERROR:", e)
            return ""

    def extract_plan(self, text):
        try:
            start = text.find("[")
            end = text.find("]")
            return eval(text[start:end+1])
        except:
            return ["Introduction", "Applications", "Advantages", "Conclusion"]

    def extract_bullets(self, text):
        bullets = []
        for line in text.split("\n"):
            line = line.strip()
            if line:
                bullets.append(line.replace("-", "").strip())
            if len(bullets) == 4:
                break

        if not bullets:
            bullets = [
                "Basic concept",
                "Key idea",
                "Example usage",
                "Conclusion"
            ]

        return bullets

    async def run(self, user_input):
        print("[agent] Planning...")

        plan_prompt = f"""
Create 5 slide titles for:
{user_input}

Return only Python list.
"""

        plan_text = self.ask_llm(plan_prompt)
        slides = self.extract_plan(plan_text)

        print("[agent] Plan:", slides)

        self.ppt.create_presentation()

        for title in slides:
            print("[agent] Slide:", title)

            content_prompt = f"""
Topic: {user_input}
Slide: {title}

Write 4 bullet points:
- point 1
- point 2
- point 3
- point 4
"""

            content = self.ask_llm(content_prompt)
            bullets = self.extract_bullets(content)

            self.ppt.add_slide(title, bullets)

        self.ppt.save_presentation("output.pptx")
        print("✅ PPT Generated Successfully")