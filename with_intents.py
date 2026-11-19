
# def get_response(message):
#     message = message.lower().strip()
#     intents ={
#         "greeting":{
#             "patterns":["hello","hi","hey"],
#             "responses":["Hello! How can I help you?"]
#         },
    
#         "ask_name":{
#             "patterns":["who are you?","what is your name?"],
#             "responses":["I'm PyBot, your personal Python chatbot!"]
#         },
        
#         "ask_age":{
#             "patterns":["what is your age?","how old are you?"],
#             "responses":["I'm timeless! I don't have an age like humans do."]
#         },
        
#         "goodbye":{
#             "patterns":["bye","goodbye","exit"],
#             "responses":["Goodbye! Have a great day."]
#         }
#     } 
    
#     for intent, data in intents.items():
#         if message in data["patterns"]:
#             return data["responses"]
        
#         elif message.strip() == "":
#             return "Please enter something."
    
#     return "I'm still learning. I don't understand that yet."

# def start_chatbot():
#     print("=" * 40)
#     print("       WELCOME TO PYBOT")
#     print("=" * 40)

#     while True:
#         user_input = input("\nYou: ")
#         response = get_response(user_input)
#         print("PyBot:", response)
        
#         if user_input.lower().strip() in ["bye", "goodbye", "exit"]:
#             break
        
#         elif response is None:
#             print("Please enter something.")
        
# if __name__ == "__main__":
#     start_chatbot()


import random

intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey"],
        "responses": [
            "Hello! How can I help you?",
            "Hey there! What's up?",
            "Hi! Nice to meet you."
        ]
    },

    "ask_name": {
        "patterns": ["who are you?", "what is your name?"],
        "responses": [
            "I'm PyBot, your personal Python chatbot!"
        ]
    },

    "ask_age": {
        "patterns": ["what is your age?", "how old are you?"],
        "responses": [
            "I'm timeless! I don't have an age like humans do."
        ]
    },

    "goodbye": {
        "patterns": ["bye", "goodbye", "exit"],
        "responses": [
            "Goodbye! Have a great day."
        ]
    },

    "thanks": {
        "patterns": ["thanks", "thank you"],
        "responses": [
            "You're welcome!",
            "Happy to help!",
            "Anytime!"
        ]
    }
}


def get_response(message):
    message = message.lower().strip()

    if not message:
        return "Please enter something!"

    for intent, data in intents.items():
        if message in data["patterns"]:
            return random.choice(data["responses"])

    return "I'm still learning. I don't understand that yet."


def start_chatbot():
    print("=" * 40)
    print("       WELCOME TO PYBOT")
    print("=" * 40)
    print("Type 'exit' to close PyBot.")

    while True:
        user_input = input("\nYou: ")

        response = get_response(user_input)

        print("PyBot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit"]:
            break


if __name__ == "__main__":
    start_chatbot()
