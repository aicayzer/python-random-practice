class House:

    def __init__(self, number, colour, value, bedrooms):
        self.number = number
        self.colour = colour
        self.value = value
        self.bedrooms = bedrooms

    def price_range(self):
        if self.value < 2:
            return "This is a cheap house"
        elif self.value > 2 and self.value[0] < 5:
            return "This is a midrange house"
        return "This is an expensive house"

    def price_change(self):
        self.value -= 1
        print("Change in price alert!! This house has just dropped by 1 million pounds! It is a bargain now!")

house1 = House(42, "White", 8.2, 5)
house2 = House(12, "Red Brick", 1.2, 3)
house3 = House(15, "Black", 4.7, 3)
house4 = House(2, "White", 28.5, 7)

print(house2.price_range())
print(house4.value)
print(house4.price_change())
print(house4.value)
print(house1.bedrooms)
