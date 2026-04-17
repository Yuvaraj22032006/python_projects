import random
attempts = 0

def levelSelection():
    print("Select Difficulty Level:")
    print("1. Easy (15 attempts and 1 to 50)")
    print("2. Medium (10 attempts and 1 to 100)")
    print("3. Hard (5 attempts and 1 to 200)")

    while True:
        try:
            level = int(input("Enter your choice (1, 2, or 3): "))
            if level == 1:
                return 15, 50
            elif level == 2:
                return 10, 100
            elif level == 3:
                return 5, 200
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

maxAttempts, maxNumber = levelSelection()
generatedNumber = random.randint(1, maxNumber)

while True:
    if attempts >= maxAttempts:
        print(f"Game over! You've used all your attempts. The number was {generatedNumber}.")
        break
    try:
        userInput = int(input(f"Guess the number between 1 and {maxNumber}: "))
        attempts += 1
        if userInput < generatedNumber:
            print("Too low! Try a Higher number.")
        elif userInput > generatedNumber:
            print("Too high! Try a Lower number.")
        else:
            print(f"Congratulations! You've guessed the number! {generatedNumber} \nNumber of attempts: {attempts}")
            break
        
    except ValueError:
        print("Invalid input. Please enter a number.")
