
def get_response(message):

    message = message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hello! How can I help you?"

    elif message in ["who are you?", "what is your name?"]:
        return "I'm PyBot, your personal Python chatbot!"

    elif message in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a great day."

    else:
        return "I'm still learning. I don't understand that yet."


def start_chatbot():

    print("=" * 40)
    print("       WELCOME TO PYBOT")
    print("=" * 40)

    while True:

        user_input = input("\nYou: ")

        response = get_response(user_input)

        print("PyBot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit"]:
            break


if __name__ == "__main__":
    start_chatbot()
