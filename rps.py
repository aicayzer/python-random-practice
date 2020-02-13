
name = input("What is your name? ")
# obtaining user choice
print(f"\nWelcome to rock, paper, scissors {name}!")

game = input("\nDo you want to play against a friend or the computer? ").lower()
game = game[0]
times = input("\nHow many times do you want to play? ")
times = int(times)
p1s = 0
p2s = 0
p2full = None

if game == "f":
    name2 = input("\n\nHey Player 2, what is your name? ")
    print(f"\nWelcome to rock, paper, scissors {name2}!")
else:
    name2 = "The Computer"

    # logic

for num in range(times):
    p1 = input(
        f"\n\nGet ready {name} 3,2,1: Rock, Paper or Scissors? ").lower()
    # indexing user choice to either R, P or S to avoid typo problems
    p1 = p1[0]
    if game == "f":
        p2 = input(f"\n\nGet ready {name2} 3,2,1: Rock, Paper or Scissors? ").lower()
        # indexing user choice to either R, P or S to avoid typo problems
        p2 = p2[0]
    else:
        from random import choice
        p2 = choice(["r", "p", "s"])
        if p2 == "r":
            p2full == "Rock"
        elif p2 == "s":
            p2full = "Scissors"
        else:
            p2full = "Paper"

    print(f"\nThe computer chose {p2full}")

    if p1 == p2:
        print("\nIt is a draw!")
        p1s += 1
        p2s += 1
    elif p1 == "p" and p2 == "r":
        print(f"\n{name} wins! Better luck next time {name2}.")
        p1s += 1
    elif p1 == "s" and p2 == "p":
        print(f"\n{name} wins! Better luck next time {name2}.")
        p1s += 1
    elif p1 == "r" and p2 == "s":
        print(f"\n{name} wins! Better luck next time {name2}.")
        p1s += 1
    elif p2 == "p" and p1 == "r":
        print(f"\n{name2} wins! Better luck next time {name}.")
        p2s += 1
    elif p2 == "s" and p1 == "p":
        print(f"\n{name2} wins! Better luck next time {name}.")
        p2s += 1
    elif p2 == "r" and p1 == "s":
        print(f"\n{name2} wins! Better luck next time {name}.")
        p2s += 1
    else:
        print("Something went wrong, sorry!")

print(f"\n{name} scored {p1s} and {name2} scored {p2s}")

if p1s > p2s:
    print(f"Well done {name}, you won overall. Better luck next time {name2}.")
elif p2s > p1s:
    print(
        f"Well done {name2}, you won overall. Better luck next time {name1}.")
else:
    print(f"{name} and {name2}, you drew overall.")
