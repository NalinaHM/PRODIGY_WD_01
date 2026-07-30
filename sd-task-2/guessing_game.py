import random

def run_game():
    print("==================================================")
    print("🎲 Software Development Task 02: Number Guessing Game")
    print("==================================================")
    secret = random.randint(1, 100)
    print("I have selected a secret number between 1 and 100.")
    attempts = 0
    
    # Simulated quick CLI demo
    test_guesses = [50, 75, secret]
    for g in test_guesses:
        attempts += 1
        print(f"Guess #{attempts}: {g}")
        if g < secret:
            print("   -> Too Low!")
        elif g > secret:
            print("   -> Too High!")
        else:
            print(f"   -> 🎉 Correct! Target reached in {attempts} attempts.")
            break

if __name__ == "__main__":
    run_game()
