import json
import random
from utils import preprocess_input, match_pattern

class Chatbot:
    def __init__(self, config_path="config.json"):
        with open(config_path, "r") as f:
            self.config = json.load(f)
        self.last_question = None

    def get_response(self, user_input):
        user_input = preprocess_input(user_input)

        with open("conversation_log.txt", "a") as log:
            log.write(f"User: {user_input}\n")

        if match_pattern(user_input, self.config["greetings"]["patterns"]):
            response = random.choice(self.config["greetings"]["responses"])
        elif match_pattern(user_input, self.config["farewells"]["patterns"]):
            response = random.choice(self.config["farewells"]["responses"])
        elif user_input in self.config.get("small_talk", {}):
            response = self.config["small_talk"][user_input]
        else:
            response = self.match_faq(user_input)
            if not response:
                response = self.match_synonyms(user_input)

        if not response:
            response = "I'm not sure how to answer that. Can you rephrase it?"

        self.last_question = user_input

        with open("conversation_log.txt", "a") as log:
            log.write(f"Bot: {response}\n\n")

        return response

    def match_faq(self, user_input):
        for key in self.config["faqs"]:
            if preprocess_input(key) == user_input:
                return self.config["faqs"][key]
        return None

    def match_synonyms(self, user_input):
        for key, synonyms in self.config.get("synonyms", {}).items():
            if user_input == key or user_input in [preprocess_input(s) for s in synonyms]:
                return self.config["faqs"].get(key)
        return None