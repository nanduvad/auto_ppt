from llm.hf_llm import generate


class BaseAgent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def think(self, content: str):

        prompt = f"""
Create a professional PowerPoint presentation.

Return ONLY valid JSON in this format:

{{
  "title": "presentation title",
  "slides": [
    {{
      "title": "slide title",
      "bullets": ["point1", "point2", "point3"]
    }}
  ]
}}

Rules:
- 6 to 8 slides
- bullet points short (max 12 words)
- no explanations
- no markdown
- no extra text

Content:
{content}
"""

        return generate(prompt)