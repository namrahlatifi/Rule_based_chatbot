import re

def preprocess_input(text):
    text = text.lower().strip()
    text = text.replace("’", "'")  # normalize fancy apostrophes
    text = re.sub(r"[^\w\s']", '', text)  # remove punctuation except apostrophes
    text = text.replace("what's", "whats")  # normalize contractions
    return text

def match_pattern(input_text, patterns):
    for pattern in patterns:
        if re.search(rf'\b{pattern}\b', input_text):
            return True
    return False