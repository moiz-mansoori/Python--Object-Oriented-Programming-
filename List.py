# Lists    --->denoted by []

# Lists are mutable, and we can change them at any time.
marks = [4, 5, 7, "Moiz", "python", True]
print(type(marks))
print(marks[-3])  # Negative index
print(marks[len(marks) - 2])  # Positive index
print(marks[4])  # Positive index
print(marks[5 - 2])  # Positive index
if 6 in marks:
    print("Yes11")
else:
    print("No")

# List comprehensions
lst = [i for i in range(4)]
print(type(lst))
print(lst)
lst = [i * i for i in range(12)]
print(lst)
lst = [i * i for i in range(15) if i % 2 == 0]  # Only even numbers will be in the output
print(lst)


# List methods

l = [11, 23, 33, 1, 2, 33, 21]
print(l)
l.append(12)  # Adds 12 at the end of the list
l.sort()       # Sorts the list in ascending order
l.sort(reverse=True)  # Sorts the list in descending order
l.reverse()     # Reverses the list
print(l.index(4))  # Returns the index where 4 is located in the list
print(l.count(1))  # Counts how many times 1 appears in the list
m = l
m[0] = 0
l.insert(2, 655)  # Inserts 655 after the 1st and 2nd element
m = [123, 432, 321]
l.extend(m)           # Extends the list by adding elements from another list
print(l)
