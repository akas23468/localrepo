import random

n = random.randint(1, 100)  # ✅ correct spelling

a = -1
guesses = 0

while a != n:
    a = int(input("Guess a number between 1 and 100: "))
    guesses += 1  # ✅ increment only once
    
    if a < n:
        print("Higher number please!")  # ✅ corrected hint
    elif a > n:
        print("Lower number please!")   # ✅ corrected hint

print(f"You have guessed the number {n} correctly in {guesses} guesses!")
