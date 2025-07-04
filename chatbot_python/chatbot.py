import random

print("🤖 SmartBot: Hello! I'm your assistant. Type 'bye' to exit.")

fallback_responses = [
    "Bot: I'm not sure I understand. Could you rephrase?",
    "Bot: Interesting... Tell me more.",
    "Bot: Sorry, I don't have a response for that yet.",
    "Bot: Hmmm... I'm still learning. Ask something else!"
]

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ['hi', 'hello', 'hey']:
        print("Bot: Hello! 😊 How can I assist you today?")

    elif 'how are you' in user_input:
        print("Bot: I'm functioning as expected. How about you?")

    elif 'your name' in user_input or 'who are you' in user_input:
        print("Bot: I'm SmartBot, your friendly rule-based assistant!")

    elif 'help' in user_input:
        print("Bot: I can chat with you, answer questions, and keep you company.")

    elif 'thank' in user_input:
        print("Bot: You're very welcome! 😊")

    elif 'weather' in user_input:
        print("Bot: I can't fetch live weather yet, but it’s always sunny in my world! ☀️")

    elif 'time' in user_input:
        from datetime import datetime
        now = datetime.now()
        print(f"Bot: The current time is {now.strftime('%H:%M:%S')}")

    elif 'date' in user_input:
        from datetime import datetime
        today = datetime.now().strftime('%A, %B %d, %Y')
        print(f"Bot: Today's date is {today}")

    elif 'joke' in user_input:
        jokes = [
            "Why don’t programmers like nature? It has too many bugs! 🐞",
            "Why did the computer show up at work late? It had a hard drive! 💻",
            "Why do Java developers wear glasses? Because they don’t see sharp. 🤓"
        ]
        print("Bot:", random.choice(jokes))

    elif user_input in ['bye', 'exit', 'quit']:
        print("Bot: Goodbye! It was nice chatting with you. 👋")
        break

    else:
        print(random.choice(fallback_responses))
