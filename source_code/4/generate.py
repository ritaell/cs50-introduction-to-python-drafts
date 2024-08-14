import random

#head tails
coin = random.choice(["head" , "tails"])
print(coin)

#random number between 1 and 10
number = random.randint(1,10)
print(number)

#shuffle cards
cards = ["king","queen","idk"]
random.shuffle(cards)
for i in cards:
    print(i)