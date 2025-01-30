from pynput.keyboard import Controller, Key
import time
import random

keyboard = Controller()

messages = [ # List of messages to send
    "🤑 Saving every bit for Korblox! 💰",
    "🌟 Every robux gets me closer to Korblox! 💎",
    "💰 Slowly but surely, Korblox will be mine! ⏳",
    "💙 Saving up for my Korblox dream! ✨",
    "🤑 Every robux I save = closer to Korblox! 💰",
    "💎 Gotta stay focused... Korblox is the goal! 🔥",
    "✨ Dreaming of that Korblox flex! 💙",
    "🚀 The grind never stops! Saving for Korblox 💰",
    "🤑 Almost there... just a few more robux to go! 💰",
    "💙 Korblox is calling my name... gotta save up! 📢",
    "💎 The journey to Korblox is real! 🌟",
    "🛤️ Just a little more saving and I'll have Korblox! 💰",
    "🔥 Korblox isn't cheap... but I'm getting there! 💎",
    "💙 If you see me grinding, just know it's for Korblox! 💰",
    "🤑 Patience and robux = Korblox in my inventory soon! ⏳",
    "✨ Korblox is the dream, and I'm making it happen! 🚀"
]

def send_chat_message():
    print("Starting... You have 5 seconds to switch to Roblox.")
    time.sleep(5)

    while True:
        message = random.choice(messages)  # Picking random message from list
        print(f"Opening chat and sending: {message}")

        keyboard.press('/')
        keyboard.release('/')
        time.sleep(0.5)  # Allowing chat to open

        for char in message:
            keyboard.type(char)  # Type each character individually
            time.sleep(0.02)  # Delay to prevent issues

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        print("Message sent! Waiting 20 seconds...")
        time.sleep(20)  # Wait (...) seconds before sending the next message

send_chat_message()
