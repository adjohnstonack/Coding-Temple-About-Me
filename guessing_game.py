import random

play_again = "yes"
while play_again.lower()in["yes", "y"]:

    secret=random.randint(1,100)
    attempts=0
    max_attempts=7

    print("===Number Guessing Game===")
    print("I'm thinking of a number between 1 and 100")
    print(f"You have {max_attempts} attempts.")
    while attempts < max_attempts:
        try:
            guess=int(input(f"Attempt {attempts+1}/ {max_attempts}:"))
        except ValueError:
            print("Please enter a valid number.")
            continue
        attempts +=1

        if guess == secret:
            print(f"\nYou got it in {attempts} attempts!")
            break
        elif guess < secret:
            print("To low!")
        else:
            print("To high!")

            remaining=max_attempts-attempts
            if remaining > 0:
                print(f"{attempts} attempts remaining.")

    else: print(f"\nOut of attempts! The number was {secret}.")

    play_again = input("\nplayagain? (yes/no): ")

print("Thanks for playing!")




