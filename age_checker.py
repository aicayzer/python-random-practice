# 18-21 wristband
# 21+ drink, normal entry
# too young, sorry

age = input("How old are you? ...be truthful ")
age = int(age)
if age < 18:
    print("Please leave")
elif age >= 18 and age < 21:
    print("Please put this wristband on")
else:
    print("Come in and buy a drink")
