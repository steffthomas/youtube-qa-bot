# 🎥 YouTube Video Q&A Bot

An AI-powered web app that summarizes YouTube videos and allows users to ask intelligent questions based on the video content. Built using **LangChain**, **FAISS**, **OpenRouter (LLaMA 3.3)**, and **Streamlit**.

---

## 🔍 Features

- 🔗 Paste any YouTube video URL
- 📄 Fetches and summarizes video transcripts
- ❓ Ask custom questions based on video content
- 🧠 Vector-based retrieval using FAISS + MiniLM
- 💬 LLM-powered answers via Meta LLaMA 3.3 (OpenRouter)
- 🌐 Deployable on Streamlit Cloud, Render, or locally

---

## 📸 Screenshots

> 📍 _Screenshots of the app UI_

### 🔹 Home Page  
![Screenshot 2025-06-14 162628](https://github.com/user-attachments/assets/a11ffa31-f156-4560-a07e-3ef2ad402a32)



### 🔹 Summary Output  
![Screenshot 2025-06-14 162754](https://github.com/user-attachments/assets/dc228182-43f7-4b1d-a9c0-dc7a48b52a8c)


### 🔹 Q&A Interface  
![Screenshot 2025-06-14 162814](https://github.com/user-attachments/assets/62962326-e111-47b0-94f3-d8c98e46346a)

---
## 🎬 Demo Video

[▶️ Click to Watch Demo](./videos/demo.mp4)

---
## 🚀 Tech Stack

| Component         | Tool/Library                           |
|------------------|----------------------------------------|
| Frontend/Backend | Streamlit                              |
| LLM              | Meta LLaMA 3.3 via OpenRouter          |
| RAG Engine       | LangChain + FAISS                      |
| Embeddings       | `all-MiniLM-L6-v2`                     |
| Transcripts      | `youtube-transcript-api`               |
| Deployment       | Streamlit Cloud / Render / Localhost   |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/steffthomas/youtube-qa-bot.git
cd youtube-qa-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Your API Key

Create a `.env` file:

```env
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> ✅ If deploying to Streamlit Cloud or Render, use the platform's **secrets manager**

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🧪 Environment Variable

| Variable Name         | Description              |
|------------------------|--------------------------|
| `OPENROUTER_API_KEY`   | Your OpenRouter API key  |

---

## ⚠️ Notes

- YouTube may block transcript access from cloud IPs.
- For full functionality, run locally or deploy using a VPS for reliable IPs.

---

## 📄 License

MIT License © 2025

---

## ✨ Acknowledgements

- [LangChain](https://www.langchain.com/)
- [OpenRouter](https://openrouter.ai/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)

---

## 🙋‍♀️ Created By

**Stefy Thomas**  
GitHub: [@steffthomas](https://github.com/steffthomas)  
LinkedIn: [stefy-thomas](https://www.linkedin.com/in/stefy-thomas/)
