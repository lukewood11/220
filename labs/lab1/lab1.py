"""
Name: LukeWoodlab1.py
"""
def calc_area():
    length = 20
    width = 5
    area = length * width
    print("area =", area)
def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("area=", area)
def calc_volume():
    length = eval(input("enter the length"))
    width = eval(input("enter the width"))
    height = eval(input("enter the height"))
    volume = length * width * height
    print("volume", volume )
def shooting_percentage():
    total_shots = eval(input("enter total shots"))
    shots_made = eval(input("enter total shots made"))
    percentage = shots_made / total_shots *100
    print("Shooting percentage", percentage)
def coffee():
    coffee_price = eval(input("enter pounds of coffee"))
    price = 10.50 * coffee_price + .86 * coffee_price + 1.50
    print("price", price)
def kilometers_to_miles():
    kilometers = eval(input("enter number of kilometers"))
    miles = (kilometers / 1.61)
    print("miles", miles)



