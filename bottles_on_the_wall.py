def make_song(value, beverage):
    while value >=1:
        if value > 1:
            print("{} bottles of {} on the wall.".format(value, beverage))
            value -= 1
        else:
            print("{} bottle of {} left!".format(value, beverage))
            value -= 1
    print("No more {}".format(beverage))
    value -= 1

make_song(10, "Kombucha")
