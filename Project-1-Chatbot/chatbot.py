# =========================================
# SUPER ADVANCED RULE-BASED AI CHATBOT
# =========================================

import datetime
import random
import time

# Typing Effect Function
def bot_print(message):
    for char in message:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

# Welcome Screen
print("=" * 60)
print("        🤖 SUPER AI CHATBOT SYSTEM 🤖")
print("=" * 60)

name = input("Enter your name: ")

bot_print(f"\nHello {name}! I am DecodeBot.")
bot_print("Type 'help' to see commands.")
bot_print("Type 'bye' to exit.\n")

# Joke List
jokes = [
    "Why did the computer get cold? Because it forgot to close Windows!",
    "Why was the math book sad? Because it had too many problems.",
    "Why do programmers hate nature? Too many bugs!"
]

# Motivational Quotes
quotes = [
    "Success starts with small steps.",
    "Keep learning and keep growing.",
    "Every expert was once a beginner."
]

# Main Chat Loop
while True:

    user = input(f"{name}: ").lower()

    # Greetings
    if user in ["hello", "hi", "hey", "salam"]:
        bot_print("Bot: Hello! Nice to meet you.")

    # Asking bot name
    elif "your name" in user:
        bot_print("Bot: My name is DecodeBot.")

    # Asking user mood
    elif "i am sad" in user:
        bot_print("Bot: Don't worry. Better days are coming 😊")

    elif "i am happy" in user:
        bot_print("Bot: That's great to hear! 🎉")

    # Time
    elif "time" in user:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        bot_print(f"Bot: Current time is {current_time}")

    # Date
    elif "date" in user:
        today = datetime.datetime.now().strftime("%d-%m-%Y")
        bot_print(f"Bot: Today's date is {today}")

    # Joke
    elif "joke" in user:
        bot_print("Bot: " + random.choice(jokes))

    # Motivation
    elif "motivate me" in user:
        bot_print("Bot: " + random.choice(quotes))

    # Calculator
    elif user == "calculator":

        try:
            bot_print("Bot: Calculator Opened")

            num1 = float(input("Enter First Number: "))
            op = input("Enter Operator (+,-,*,/): ")
            num2 = float(input("Enter Second Number: "))

            if op == "+":
                result = num1 + num2

            elif op == "-":
                result = num1 - num2

            elif op == "*":
                result = num1 * num2

            elif op == "/":
                result = num1 / num2

            else:
                result = "Invalid Operator"

            bot_print(f"Bot: Result = {result}")

        except:
            bot_print("Bot: Invalid Input!")

    # Help Menu
    elif user == "help":

        print("\n========== COMMAND LIST ==========")
        print("hello / hi")
        print("time")
        print("date")
        print("joke")
        print("calculator")
        print("motivate me")
        print("i am sad")
        print("i am happy")
        print("your name")
        print("bye")
        print("==================================\n")

    # Exit
    elif user == "bye":
        bot_print(f"Bot: Goodbye {name}! Have a nice day.")
        break

    # Unknown Commands
    else:

        random_reply = [
            "Sorry, I don't understand.",
            "Can you say that differently?",
            "Interesting... Tell me more.",
            "I am still learning that command."
        ]

        bot_print("Bot: " + random.choice(random_reply))
