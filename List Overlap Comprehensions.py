#Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes

c= [i for i in b if i in a]
print (c)


#Extra:
# Randomly generate two lists to test this

import random

list_1 = random.sample(range(30), 12)
list_2 = random.sample(range(30), 20)

new_list = [numbers for numbers in list_1 if numbers in list_2]
print (new_list)