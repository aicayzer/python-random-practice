name = input("What is your name? ")

print(f"Hello {name}, there how many kilometers did you run today?")
km = float(input())
print("Nice work!")
# km = float(km)
mi = km / 1.60934
mi = round(mi, 2)
print(f"Ok {name}, you ran {mi} miles today, well done!") 
