
# Dictionary   --->denoted by {}

# Dictionaries store key-value pairs.
dic = {
    29: "Muzammil",
    32: "Moiz",
    9: "Hamza",
    11: "Wajahat"
}
print(dic[32])

# Iterating through dictionary keys
info = {'Name': 'Moiz', 'ID': '22F-BSAI-32', 'Subject': 'Python'}
print(info.items())
for key, value in info.items():
    print(f"The value of the corresponding {key} is {info[key]}")

# Dictionary methods

# Updating a dictionary
marks = {'22F-BSAI-32': 60, '22F-BSAI-29': 70, '22F-BSAI-09': 80}
more = {'22F-BSAI-11': 65, '22F-BSAI-17': 75}
marks.update(more)
print(marks)

# Clearing a dictionary
marks.clear()
print(marks)

# Removing an item from a dictionary
marks = {'22F-BSAI-32': 60, '22F-BSAI-29': 70, '22F-BSAI-09': 80}
more = {'22F-BSAI-11': 65, '22F-BSAI-17': 75}
marks.update(more)
marks.pop('22F-BSAI-17')
print(marks)

# Removing the last item from a dictionary
marks.popitem()
print(marks)
