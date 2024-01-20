
# Tuples    --->denoted by ()

# Tuples are immutable, meaning they cannot be changed.
tup = (1, 2, 5, 43)
tup[0:]
print(tup)
print(type(tup), tup)


# Converting tuple to list to modify and then converting it back to tuple
countries = ("Pakistan", "England", "India", "Asia", "Mansoori")
print(countries)
temp = list(countries)
temp.append("Bangladesh")
temp.pop(3)    # Delete the elements from the tuple
temp[2] = "China"
countries = tuple(temp)
print(countries)



# Combining tuples
name = ("Moiz", "Ahmed", "Mansoori")
name2 = ("Muhammad", "Roshan")
myfullname = name + name2
print(myfullname)

# Tuple methods
tuple_example = (1, 4, 2, 7, 3, 2, 3, 7, 2, 3, 2)
res = tuple_example.count(2)
print("The count of 2 is", res)
