import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

def generate_story(prompt, temperature=0.8, top_p=0.9):
    print("==================================================")
    print("✨ Generative AI Task 01: LLM Text & Story Generator")
    print("==================================================")
    print(f"📌 Prompt: {prompt}")
    print(f"🎛️ Hyperparameters: Temperature={temperature}, Top-P={top_p}\n")
    print("🤖 Synthesizing AI Text Stream:\n")

    sample_output = (
        "The neon Rain slicked the alleyway as Maya's cybernetic retinas scanned the encrypted file.\n"
        "Data streams dating back 50 years revealed a forgotten truth: humanity's consciousness was once unmonitored.\n"
        "[OK] Story generation completed successfully."
    )

    for line in sample_output.split('\n'):
        print(line)
        time.sleep(0.3)

if __name__ == "__main__":
    generate_story("In a neon-lit metropolis governed by autonomous AI...")
