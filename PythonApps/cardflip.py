#!/usr/bin/python3

def flip(number):
    count = 0
    order = []
    prev_card = "0"
    next_card = False
    for index, num in enumerate(number):
        if num == "1":
            count += 1

        if next_card:
            order.append(index)
        else:
            order.insert(0, index)
        
        if num != prev_card:
            # toggle direction
            next_card ^= 1 

        prev_card = num
    if count % 2:
        return order
    else:
        return "No solution"

print(flip("0100110"))
