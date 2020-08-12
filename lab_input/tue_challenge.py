#!/usr/bin/env python3

icecream = ["flavors", "salty"]

price = 99
name = input("what is your name: ").title()

icecream.append(price)
print(icecream)

print(f"{icecream[2]} {icecream[0]}, and {name} chooses to be {icecream[1]}.")
