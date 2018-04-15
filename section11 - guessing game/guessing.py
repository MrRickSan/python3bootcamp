from random import randint


number = randint(1, 10)
guess = None

while guess != number:
    guess = int(input("Pick a number from 1 to 10: "))
    if guess == number:
        print("Well done! You got it!")
        option = input("Do you want to continue? (y/n) ")
        if option == "n":
            print("Thank you for playing!")
            break
        else:
            number = randint(1, 10)
            guess = None
    elif guess > number:
        print("Too high")
    else:
        print("Too low")
