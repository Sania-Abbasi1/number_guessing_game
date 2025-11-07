
import random

def number_guessing_game():
    print("I'm thinking of a secret number.")
    print("Your mission is simple — guess the correct number in as few tries as possible!")
    print("💡 Here's how it works:")
    print("- If your guess is too low, I’ll say “Too Low!”")
    print("- If your guess is too high, I’ll say “Too High!”")
    print("- Keep guessing until you find the secret number.")
    print("🏆 Choose your level:")
    print("1️⃣ Easy   → Range: 1–50   | Attempts: 10")
    print("2️⃣ Medium → Range: 1–100  | Attempts: 7")
    print("3️⃣ Hard   → Range: 1–200  | Attempts: 5")

    level = input("Enter the number of your chosen level (1, 2, or 3): ")

    if level == '1':
        max_range = 50
        max_attempts = 10
    elif level == '2':
        max_range = 100
        max_attempts = 7
    elif level == '3':
        max_range = 200
        max_attempts = 5
    else:
        print("Invalid level choice. Starting with Medium level by default.")
        max_range = 100
        max_attempts = 7

    secret_number = random.randint(1, max_range)
    attempts = 0

    print(f"\nI'm thinking of a number between 1 and {max_range}.")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too Low!")
            elif guess > secret_number:
                print("Too High!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"\nSorry, you've run out of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
1