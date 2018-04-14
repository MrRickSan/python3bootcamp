print("\nWelcome to rock, paper, scissors game!")
p1 = input("Player 1, make your move: ")
p2 = input("Player 2, make your move: ")

if p1 == "rock" and p2 == "scissors":
    print("Player 1 wins!")
elif p1 == "rock" and p2 == "paper":
    print("Player 2 wins!")
elif p1 == "paper" and p2 == "scissors":
    print("Player 2 wins!")
elif p1 == "paper" and p2 == "rock":
    print("Player 1 wins!")
elif p1 == "scissors" and p2 == "rock":
    print("Player 2 wins!")
elif p1 == "scissors" and p2 == "paper":
    print("Player 1 wins!")
elif p1 == p2:
    print("It's a tie!")
else:
    print("something went wrong")
