import random

first = int(input ("Ey! just type the first number of a range that you want to get a random number: "))
second = int(input ("Now type the second one: "))

print ("Your random number is the next: ", random.randrange(first, second))
