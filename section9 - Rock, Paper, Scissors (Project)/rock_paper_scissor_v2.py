print("\nWelcome to rock, paper, scissors game!")
p1 = input("Player 1, make your move: ")
print(" *** NO CHEATING! *** \n\n" * 20)
p2 = input("Player 2, make your move: ")

if p1 == p2:
    print("It's a tie!")

elif p1 == "rock":
    if p2 == "scissors":
        print("Player 1 wins!")
    elif p2 == "paper":
        print("Player 2 wins!")

elif p1 == "paper":
    if p2 == "rock":
        print("Player 1 wins!")
    elif p2 == "scissors":
        print("Player 2 wins!")

elif p1 == "scissors":
    if p2 == "paper":
        print("Player 1 wins!")
    elif p2 == "rock":
        print("Player 2 wins!")

else:
    print("something went wrong")
