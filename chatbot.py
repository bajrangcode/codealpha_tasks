import nltk
from nltk.chat.util import Chat, reflections

# Ensure you have the necessary NLTK data files
nltk.download('punkt')

# Define a set of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created for a demo.",]
    ],
    [
        r"how are you?",
        ["I'm just a bunch of code, but thanks for asking!",]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no worries!",]
    ],
    [
        r"quit",
        ["Bye! Take care.",]
    ],
    [
        r"(.*)",
        ["I see. Can you tell me more?",]
    ]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to start the chatbot
def chatbot_conversation():
    print("Hi! I am your chatbot. Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye! Take care.")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot conversation
chatbot_conversation()
