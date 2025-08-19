import datetime

# Function 1: Handles the chatbot logic
def chatbot_response(message, bot_name="ChatBuddy"):
    """
    Generate a reply based on the user's message.
    """
    message = message.lower().strip()

    if message in ["hi", "hello", "hey"]:
        return f"{bot_name}: Hello! How can I help you today?"

    elif "your name" in message:
        return f"{bot_name}: My name is {bot_name}!"

    elif "how are you" in message:
        return f"{bot_name}: I'm just code, but I'm doing great! 😊"

    elif "time" in message:
        current_time = datetime.datetime.now().strftime("%H:%M")
        return f"{bot_name}: The current time is {current_time}."

    elif "weather" in message:
        return f"{bot_name}: I'm not connected to live weather data, but it looks sunny in my virtual world! ☀️"

    elif "bye" in message:
        return f"{bot_name}: Goodbye! Have a great day 👋"

    else:
        return f"{bot_name}: I'm not sure how to respond to that. Try asking something else!"

# Function 2: Handles the chat loop
def chat_loop():
    """
    Runs the chatbot in a loop until the user types 'bye'.
    """
    bot_name = "ChatBuddy"
    print(f"{bot_name}: Hi! I'm {bot_name}. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input, bot_name)
        print(response)

        if "goodbye" in response.lower():
            break

# Function Call: Start the chatbot
chat_loop()
