# 🤖 Multi-Agent Research Assistant

An AI-powered research assistant that uses multiple specialized agents to search, analyze, scrape, write, and review research reports automatically.

---

## 🚀 Features

- 🔍 AI-powered web search using Tavily
- 🌐 Intelligent webpage scraping with BeautifulSoup
- 🤖 Multi-Agent architecture using LangGraph
- ✍️ Automatic report generation using Mistral AI
- ✅ AI critic that reviews and scores the generated report
- 🎨 Interactive Streamlit web interface
- 📥 Download generated research reports

---

## 🏗️ Architecture

```
                 User Query
                      │
                      ▼
             🔍 Search Agent
                      │
                      ▼
             🌐 Reader Agent
                      │
                      ▼
             ✍️ Writer Agent
                      │
                      ▼
             ✅ Critic Agent
                      │
                      ▼
               Final Report
```

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| LLM | Mistral AI |
| Framework | LangChain, LangGraph |
| Search | Tavily API |
| Scraping | BeautifulSoup4 |
| UI | Streamlit |
| Environment | Python Dotenv |

---

## 📂 Project Structure

```
multi-agent-research-assistant/
│
├── app.py                 # Streamlit UI
├── pipeline.py            # Main research workflow
├── agents.py              # Search & Reader agents
├── tools.py               # Tavily + Scraper tools
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-research-assistant.git
cd multi-agent-research-assistant
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file

```env
TAVILY_API_KEY=YOUR_TAVILY_KEY
MISTRAL_API_KEY=YOUR_MISTRAL_KEY
```

---

## ▶️ Run Streamlit App

```bash
streamlit run app.py
```

---

## 📸 Screenshots

### Home Page

*(Add screenshot here)*

---

### Research Report

*(Add screenshot here)*

---

### Critic Review

*(Add screenshot here)*

---

## 🔄 Workflow

1. User enters a research topic.
2. Search Agent gathers reliable sources.
3. Reader Agent scrapes the most relevant webpage.
4. Writer Agent generates a structured research report.
5. Critic Agent reviews the report and provides feedback.

---

## 📌 Example Research Topics

- Impact of AI on Healthcare
- Effects of War on Stock Markets
- Quantum Computing
- Climate Change
- Electric Vehicles

---

## 📈 Future Improvements

- PDF export
- Citation generation
- Multiple webpage scraping
- Memory-enabled agents
- Chat interface
- Research history
- Deployment on Streamlit Cloud

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Dipanshu Rathor**

If you found this project helpful, ⭐ Star the repository!
