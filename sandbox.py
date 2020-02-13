# factors = []
# def find_factors(user_input):
#     user_input = int(user_input)
#     for num in range(1,(user_input + 1)):
#         if user_input % num == 0:
#             factors.append(num)
#     print(factors)
#
# find_factors(11)


def find_factors(num):
    factors = []
    i = 1
    while(i <= num):
        if (num % i == 0):
            factors.append(i)
        i += 1
    print(factors)

factors = []
def find_factors2(user_input):
    user_input = int(user_input)
    for num in range(1,(user_input + 1)):
        if user_input % num == 0:
            factors.append(num)
    print(factors)


find_factors(2)
find_factors2(2)
