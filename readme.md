# 🚀 AI PowerPoint Generator Agent

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![AI](https://img.shields.io/badge/AI-Multi--Agent-green)
![LLM](https://img.shields.io/badge/LLM-HuggingFace-orange)
![Status](https://img.shields.io/badge/Status-Working-success)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

An **AI-powered autonomous agent system** that generates **professional PowerPoint presentations automatically** from any topic using web research, Large Language Models (LLMs), and automated slide design.

---

## 🎯 Demo

### Input

``` 
Topic: Any Topic of your choice
Theme: dark/corporate/modern/minimal(any one of your choice)
Location :where you want to save your ppt on your desktop 
```

### Output

✅ Fully structured PPT
✅ Professional layout
✅ Consistent theme
✅ 6–8 slides automatically generated

---

## 🧠 What This Project Does

This system behaves like a **mini AI employee** that:

1. 🔎 Searches the web for topic information
2. 🧠 Uses an LLM to structure presentation content
3. 🎨 Designs slides automatically
4. 📄 Generates a polished PowerPoint file

No manual slide creation required.

---

## ⚙️ System Architecture

```
                User Input
                     │
                     ▼
              Controller Agent
                     │
     ┌───────────────┼───────────────┐
     ▼               ▼               ▼
Web Search      LLM Reasoning     PPT Generator
  Agent             Agent            Agent
                                         │
                                         ▼
                                   File Save Agent
                                         │
                                         ▼
                                 Generated PPT
```

---

## 📁 Project Structure

```
ahent2/
│
├── main.py                     # Entry point
├── .env                        # API keys
│
├── agents/
│   ├── base_agent.py           # Core agent logic
│   ├── web_search_agent.py     # Web research
│   ├── ppt_agent.py            # PPT creation
│   └── file_agent.py           # File saving
│
├── orchestrator/
│   └── controller.py           # Workflow manager
│
├── llm/
│   └── hf_llm.py               # Cloud LLM connection
│
├── outputs/                    # Generated PPT files
└── README.md
```

---

## ✨ Features

* ✅ Topic-independent presentation generation
* ✅ Multi-agent architecture
* ✅ Cloud LLM (no local model download)
* ✅ Automatic slide structuring
* ✅ Professional layouts
* ✅ Theme-based styling
* ✅ Zero hardcoding
* ✅ Local PPT export

---

## 🎨 Supported Themes

| Theme       | Style             |
| ----------- | ----------------- |
| `modern`    | Clean & minimal   |
| `dark`      | Dark professional |
| `minimal`   | Simple academic   |
| `corporate` | Business style    |

---

## 🛠️ Installation

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd ahent2
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install python-pptx requests python-dotenv ddgs
```

---

### 4️⃣ Setup Environment Variables

Create `.env` file:

```
HF_TOKEN=your_huggingface_token_here
```

Get token from:
https://huggingface.co/settings/tokens

(finegrained.)

---

## ▶️ Run the Project

```bash
python main.py
```

Example interaction:

```
Topic: AI in Retail Industry
Theme: dark
Save path: outputs/ai_retail.pptx
```

---

## 🧩 How It Works

### 🔎 Web Search Agent

Collects real-world information using DuckDuckGo search.

### 🧠 LLM Agent

Transforms research into structured JSON slides:

```json
{
  "title": "AI in Retail",
  "slides": [
    {
      "title": "Introduction",
      "bullets": ["AI transforms retail", "Improves customer insights"]
    }
  ]
}
```

### 🎨 PPT Agent

* Builds slides automatically
* Applies formatting & themes
* Prevents blank pages

### 💾 File Agent

Exports `.pptx` locally.

---

## 📸 OUTPUT VIDEO 


https://drive.google.com/file/d/15ZP1rG5FiBvqw1DI36_1mApZc4zf6vcP/view?usp=sharing

---

## ⚠️ Challenges I faced



🧩 Challenges & Issues Faced
1️⃣ Local LLM Download Issues (Storage & Performance)

Initially, the system used locally hosted HuggingFace models.
Large models (~14GB) were downloaded automatically, which caused:

Long download times
High disk usage
Heavy RAM/GPU requirements
Slow initialization

Solution

Switched to cloud-based HuggingFace Inference API instead of local model loading.

2️⃣ HuggingFace Model Compatibility Errors

Multiple errors occurred while selecting models:

model_not_supported
model_not_found
task not supported for provider

Cause:

Some models support only chat-completion
Some providers were not enabled
Incorrect model IDs

Solution

Migrated to supported chat-completion models
Updated API endpoint usage
Configured HuggingFace token correctly.
3️⃣ Deprecated HuggingFace API Endpoint

Error received:

https://api-inference.huggingface.co is no longer supported

Solution

Updated inference calls to:

https://router.huggingface.co/v1/chat/completions
4️⃣ Python Dependency Issues

Missing packages caused runtime failures:

ModuleNotFoundError: transformers
ModuleNotFoundError: duckduckgo_search
ModuleNotFoundError: ddgs

Solution

Installed required dependencies and updated renamed packages:

pip install transformers
pip install ddgs
5️⃣ Agent Architecture Initialization Errors

Errors like:

TypeError: object.__init__() takes exactly one argument
BaseAgent.__init__() missing arguments

Cause:

Improper inheritance setup
Agents not calling parent constructor.

Solution

Standardized all agents to initialize using:

super().__init__(name, role)
6️⃣ Function Signature Mismatch

Error:

create_ppt() takes 2–3 arguments but 4 were given

Cause:

Controller passed (topic, content, theme)
Agent expected fewer parameters.

Solution

Unified interface across agents.

7️⃣ Invalid LLM Output Format

Early PPTs contained:

Blank slides
Raw API error text
Improper layouts

Cause:
LLM returned free-form text instead of structured data.

Solution

Forced strict JSON output using prompt constraints:

Fixed schema
Bullet limits
No markdown rules

---

### Model not supported error

Ensure HuggingFace router API is used and token is valid.

---

## 🔮 Future Enhancements

* 📊 Automatic charts & graphs
* 🖼️ AI image insertion
* 🎙 Speaker notes generation
* 🌐 Web UI interface
* 📄 PDF export
* 🧩 Custom company branding

---

## 👩‍💻 Tech Stack

* Python
* Multi-Agent Architecture
* HuggingFace Inference API
* python-pptx
* DuckDuckGo Search (DDGS)
* JSON Structured Generation

---

## ⭐ Why This Project Matters

This project demonstrates:

* Agent-based AI system design
* LLM orchestration
* Automation workflows
* Real-world AI application development

Perfect for:

* AI portfolios
* Final year projects
* Resume showcases

---

## 📜 License

Educational & Research Use.

---

## 🙌 Author

Built as an AI Agent Automation Project.

If you found this useful, ⭐ star the repository!
