x = input("How many times shall I tell you to clean up your room? ")
x = int(x)
for y in range(x):
    print(f"Time {y + 1}: Clean up your room!")

if x == "1":
    print(f"There I did it {x} time ")
else:
    print(f"There I did it {x} times")
