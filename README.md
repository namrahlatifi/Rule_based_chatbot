# 🤖 Advanced Rule-Based Chatbot

This is a rule-based chatbot built using Python that uses pattern matching, synonym handling, and simple NLP techniques to respond to user inputs in a conversational manner — without any ML models.

---

## 📌 Features

✅ Pattern matching using regex  
✅ Case-insensitive and punctuation-free input handling  
✅ 20+ FAQ responses using pre-defined templates  
✅ Synonym recognition (e.g., "explain python" → "what is python")  
✅ Small talk support (weather, hobbies, compliments)  
✅ Greeting and farewell detection  
✅ Fallback response for unmatched queries  
✅ Conversation logging to a `.txt` file  
✅ CLI interface for user interaction  
✅ Config-driven responses using a JSON file

---

## 🛠 Tech Stack

- **Language:** Python 3.7+
- **Libraries:** Standard libraries only (`re`, `json`, `random`)
- **Interface:** Command Line (CLI)
- **Data Storage:** `config.json` for patterns and `conversation_log.txt` for logs

---

## 📁 File Structure

chatbot_advanced/
├── chatbot.py # Core bot logic
├── config.json # All patterns, synonyms, and responses
├── run_chatbot.py # CLI script to run the bot
├── utils.py # Preprocessing and regex matching
├── conversation_log.txt # Conversation log file
└── README.md # This file

---

## 🚀 How to Run

### 1. Clone or Download the Project

```bash
git clone https://github.com/your-username/chatbot_advanced.git
cd chatbot_advanced

## **🚀 2. Run the Chatbot**

```bash
python run_chatbot.py

## **💬 3. Try Chatting**

You: hello  
Bot: Hi there! How can I help you today?

You: what is ai  
Bot: AI stands for Artificial Intelligence.

You: tell me a joke  
Bot: Why did the developer go broke? Because he used up all his cache!

You: goodbye  
Bot: Take care!

## 📝 Sample Questions Supported
- What is AI / Python / NLP?
-Who created you?
-How are you?
-What can you do?
-What’s the weather?
-Tell me a joke
-Do you like music?
-And many more...

## 📦 How It Works
Input is preprocessed (lowercased, punctuation removed).

Bot checks for matches in greetings, farewells, FAQs.

If no match is found, it tries synonym mapping.

Still no match? It responds with a fallback message.

All conversations are logged into conversation_log.txt.
