from chatbot import Chatbot

def main():
    bot = Chatbot()
    print("Bot: Hello! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        response = bot.get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()