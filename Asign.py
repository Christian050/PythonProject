# sample list
fruits = ["apple", "banana", "pineapple"]
vegetables = ["carrot", "onion", "peas"]
places = ["nima", "madina", "osu"]

# print(fruits)


# sample __iter__,__next__
"""
for x in fruits:
    print(x)
"""
try:
    myiter = iter(fruits)
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
except StopIteration:
    print("axe")



