# =========================================================
# ADVANCED AI RECOMMENDATION SYSTEM
# DecodeLabs Internship Project 3
# =========================================================

import time
import os

# ==============================
# Typing Effect
# ==============================

def slow_print(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# ==============================
# Clear Screen
# ==============================

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ==============================
# Database
# ==============================

recommendation_data = {
    "Technology": {
        "items": [
            "AI Masterclass",
            "Python Bootcamp",
            "Machine Learning Course",
            "Data Science Handbook",
            "Cybersecurity Guide"
        ]
    },

    "Fitness": {
        "items": [
            "Workout Planner",
            "Healthy Diet Program",
            "Yoga Sessions",
            "Fitness App Premium",
            "Weight Loss Guide"
        ]
    },

    "Gaming": {
        "items": [
            "Gaming Keyboard",
            "Action Games Collection",
            "Gaming Mouse",
            "Esports Guide",
            "FPS Training Pack"
        ]
    },

    "Music": {
        "items": [
            "Guitar Lessons",
            "Spotify Premium Playlist",
            "Piano Course",
            "Music Production Course",
            "Audio Editing Toolkit"
        ]
    },

    "Movies": {
        "items": [
            "Netflix Top Picks",
            "Marvel Collection",
            "Sci-Fi Recommendations",
            "IMDB Top Rated Movies",
            "Thriller Movie Pack"
        ]
    },

    "Books": {
        "items": [
            "Atomic Habits",
            "Deep Work",
            "Python Programming Book",
            "Rich Dad Poor Dad",
            "Self Development Collection"
        ]
    }
}

# ==============================
# Welcome Screen
# ==============================

clear()

slow_print("=" * 60)
slow_print("        ADVANCED AI RECOMMENDATION SYSTEM")
slow_print("                  BY HUSNA ")
slow_print("=" * 60)

# ==============================
# Show Categories
# ==============================

slow_print("\nAVAILABLE INTEREST CATEGORIES:\n")

for category in recommendation_data.keys():
    print(f"• {category}")

# ==============================
# User Input
# ==============================

user_input = input(
    "\nEnter your interests separated by commas: "
)

# Convert input into list
user_interests = [
    interest.strip().title()
    for interest in user_input.split(",")
]

# ==============================
# Recommendation Engine
# ==============================

matched_items = []

slow_print("\nAnalyzing user preferences...")
time.sleep(1.5)

for interest in user_interests:

    if interest in recommendation_data:

        items = recommendation_data[interest]["items"]

        for item in items:

            similarity_score = 80 + len(interest)

            matched_items.append({
                "category": interest,
                "item": item,
                "score": similarity_score
            })

# ==============================
# Sort Recommendations
# ==============================

matched_items.sort(
    key=lambda x: x["score"],
    reverse=True
)

# ==============================
# Display Results
# ==============================

if matched_items:

    slow_print("\nTOP RECOMMENDATIONS FOR YOU:\n")

    for index, recommendation in enumerate(matched_items, start=1):

        print(f"{index}. {recommendation['item']}")
        print(f"   Category : {recommendation['category']}")
        print(f"   Match    : {recommendation['score']}%")
        print("-" * 45)

else:

    slow_print("\nNo matching interests found.")
    slow_print("Please choose from available categories.")

# ==============================
# Continue Option
# ==============================

while True:

    choice = input(
        "\nDo you want another recommendation search? (yes/no): "
    ).lower()

    if choice == "yes":

        slow_print("\nRestart the program to search again.")
        break

    elif choice == "no":

        slow_print("\nThank you for using the system!")
        break

    else:
        print("Invalid input. Type yes or no.")

# ==============================
# Ending
# ==============================

slow_print("\nSystem Closed Successfully.")
slow_print("=" * 60)
