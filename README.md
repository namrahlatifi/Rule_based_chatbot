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

git clone https://github.com/your-username/chatbot_advanced.git
cd chatbot_advanced

### 2. Run the Chatbot


python run_chatbot.py

## 💬 Try Chatting


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
- Who created you?  
- How are you?  
- What can you do?  
- What’s the weather?  
- Tell me a joke  
- Do you like music?  
- What’s your hobby?  
- How to learn Python?  
- And many more...

---

## 📦 How It Works

- User input is preprocessed: converted to lowercase and cleaned of punctuation  
- The bot checks for matches in these categories, in order:
  1. Greetings (e.g., "hi", "hello")
  2. Farewells (e.g., "bye", "see you")
  3. Small talk (e.g., hobbies, music, weather)
  4. FAQs (predefined Q&A)
  5. Synonyms (e.g., "explain python" → "what is python")
- If no match is found, a fallback response is triggered  
- Every question and answer is logged in `conversation_log.txt`





