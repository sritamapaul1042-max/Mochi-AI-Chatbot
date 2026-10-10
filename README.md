# 🎀 Mochi — AI Roast Chatbot

> A playful AI chatbot that turns ordinary conversations into witty roasts. 🎀

**Mochi** is an interactive AI roast assistant built using **Python, LangChain, Groq LLM, and Streamlit**. It uses a custom system prompt to maintain a humorous and sarcastic personality while keeping the conversation playful.

## 🚀 Live Demo

👉 **[Try Mochi](https://mochi-ai-chatbot-vtuyn3ciosjrnrlyfimbbf.streamlit.app)**

---

## ✨ Features

- 🎀 AI-powered roast chatbot
- 🤖 Powered by Groq LLM
- 🧠 Conversational message history
- 💬 Interactive Streamlit chat interface
- 😂 Playful sarcasm and witty responses
- ⚡ Fast LLM responses
- 🔐 API key protected using environment variables / Streamlit Secrets
- 🌐 Deployed using Streamlit Community Cloud

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM application framework |
| LangChain-Groq | Groq LLM integration |
| Groq | Large Language Model inference |
| Streamlit | Web interface |
| python-dotenv | Environment variable management |

---

## 🏗️ Project Structure

```text
Mochi-AI-Chatbot/
│
├── chatmodels/
│   ├── chatbot.py
│   └── uichatbot.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

### Files

**`chatmodels/chatbot.py`**

Contains the basic command-line chatbot implementation using LangChain and Groq.

**`chatmodels/uichatbot.py`**

Contains the Streamlit web interface for Mochi.

---

## ⚙️ How It Works

The chatbot follows a simple LLM pipeline:

```text
User Input
     ↓
Streamlit Interface
     ↓
LangChain Messages
     ↓
Groq LLM
     ↓
AI Response
     ↓
Displayed in Chat Interface
```

A custom system prompt defines Mochi's personality and ensures that responses remain humorous, sarcastic, and playful.

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/sritamapaul1042-max/Mochi-AI-Chatbot.git
cd Mochi-AI-Chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Groq API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

⚠️ Never commit your `.env` file to GitHub.

### 5. Run Mochi

```bash
streamlit run chatmodels/uichatbot.py
```

The application will open in your browser.

---

## 🔐 Environment Variables

The application requires:

```text
GROQ_API_KEY
```

For Streamlit Cloud, the key should be added through **Streamlit Secrets** rather than committed to the repository.

---

## 🎯 Future Improvements

- 🎨 More customization options
- 🧠 Persistent conversation history
- 👤 User authentication
- 📊 Chat analytics
- 🎭 Multiple chatbot personalities
- 🎤 Voice interaction
- 🌍 Multi-language support

---

## 👩‍💻 Author

**Sritama Paul**

B.Tech Computer Science Engineering

---

## ⭐ Support

If you enjoyed getting roasted by Mochi, consider giving the repository a ⭐ on GitHub!

🎀 **Happy Roasting!**
