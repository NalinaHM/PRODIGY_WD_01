import sys

sys.stdout.reconfigure(encoding='utf-8')

def run_chatbot_session():
    print("==================================================")
    print("💬 Generative AI Task 03: Conversational AI Chatbot")
    print("==================================================")
    print("🎭 Current System Persona: Senior Developer 👨‍💻\n")

    conversation = [
        ("User", "What is the benefit of Kotlin ViewBinding in Android development?"),
        ("AI Assistant", "ViewBinding provides null-safety and type-safety by generating a binding class for each XML layout file, eliminating `findViewById` crashes.")
    ]

    for speaker, text in conversation:
        print(f"[{speaker}]: {text}")

    print("\n✅ Multi-turn conversational session logged.")

if __name__ == "__main__":
    run_chatbot_session()
