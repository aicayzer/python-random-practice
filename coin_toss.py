from random import random

# def flip_coin():
#
#     if random() > 0.5:
#         return "HEADS"
#     else:
#         return "TAILS"
#
# print(flip_coin())


h = 0
t = 0

while h < 1000 and t < 1000:
    if random() < 0.5:
        h += 1
    else:
        t += 1
print("***************")
print(f"Total Heads: {h}    Total Tails: {t}")
if h > t:
    print("/nHeads wins")
else:
    print("/nTails wins")
