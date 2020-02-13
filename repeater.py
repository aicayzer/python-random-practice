

ans = input("Hey, how are you doing? ")
num = 0

while ans != "stop":
    num += 1
    if num == 3:
        ans = input(f"{ans}\n")
        print("You can stop this by saying 'stop'...")
    else:
        ans = input(f"{ans}\n")

print("Ok fine, you win!")
