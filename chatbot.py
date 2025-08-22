# Basic Chatbot

def chatbot():
    print("🤖 Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.\n")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        # Rule-based responses
        if user_input in ["hi", "hello", "hey"]:
            print("🤖 Chatbot: Hi there!")
        elif user_input in ["how are you", "how are you doing"]:
            print("🤖 Chatbot: I'm fine, thanks! How about you?")
        elif user_input in ["bye", "exit", "quit"]:
            print("🤖 Chatbot: Goodbye! Have a nice day 😊")
            break
        elif user_input in ["what is your name", "who are you"]:
            print("🤖 Chatbot: I’m your friendly chatbot!")
        else:
            print("🤖 Chatbot: Sorry, I don’t understand that.")

# Run the chatbot
chatbot()
