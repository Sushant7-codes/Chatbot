import random
import string
from chatbot.intents import INTENTS

def tokenize(message):
    message = message.lower().strip()
    message = message.translate(
        str.maketrans("", "", string.punctuation)
    )
    
    return message.split()


def detect_intent(tokens):
    for intent, data in INTENTS.items():
        if any(keyword in tokens for keyword in data["keywords"]):
            return intent
        
    return None


def get_response(intent):
    if intent is None:
        return "I'm still learning. I don't understand that yet."

    return random.choice(INTENTS[intent]["responses"])


def start_chatbot():
    print("=" * 40)
    print("       WELCOME TO PYBOT - DAY 2")
    print("=" * 40)
    print("Type 'exit' to close PyBot.")

    while True:
        user_input = input("\nYou: ")

        tokens = tokenize(user_input)

        if not tokens:
            print("PyBot: Please enter something!")
            continue

        intent = detect_intent(tokens)

        response = get_response(intent)

        print("PyBot:", response)

        if intent == "goodbye":
            break


if __name__ == "__main__":
    start_chatbot()