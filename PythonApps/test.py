#!/usr/bin/python3
import random

# main array
frontarea = []
fullset = []

# declaration of constants
suits = ['索', '万', '筒', 'd', '风', 'a', 'f']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dragons = ['红中', '白板', '青發']
winds = ['东', '南', '西', '北']
animals = ['小猫', '老鼠', '公鸡', '蜈蚣']
flowers = ['1', '2', '3', '4']
flowCol = ['红花', '蓝花']

# hand
hand = []

def populate():
    # populate the fullset
    #for each suit besides the basic 3, loop through the numbered array
    for suit in suits:
        if suit == '索' or suit == '万' or suit == '筒':
            for num in numbers:
                for x in range(4):
                    fullset.append(str(num) + suit)

        elif suit == 'd':
            for d in dragons:
                for x in range(4):
                    fullset.append(d)
        
        elif suit == '风':
            for w in winds:
                for x in range(4):
                    fullset.append(w + suit)

        elif suit == 'a':
            for a in animals:
                fullset.append(a)

        else:
            for f in flowers:
                for c in flowCol:
                    fullset.append(c + f)
    #shuffle
    random.shuffle(fullset)


def initDraw(dealer):
    #draw tiles
    for r in range(13):
        hand.append(fullset.pop())

    if dealer:
        hand.append(fullset.pop())

# populate the set
populate()

# draw the tiles
initDraw(False)

while(True):
    print(frontarea)
    print(hand)


