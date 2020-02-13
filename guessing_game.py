import random

random_number = random.randint(1, 10)
guess = None


while True:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
    if int(guess) > random_number:
        guess = input("Too high, try again... ")
    elif guess < random_number:
        guess = input("Too low, try again... ")
    else:
        print("You got it, well done!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            random_number = random.randint(1, 10)
            guess = None
            print(random_number)
        else:
            print("Thank you for playing!")
            break


# if guess == random_number:
#     print("Well done, you got it!")
