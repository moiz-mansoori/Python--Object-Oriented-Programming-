
                        # Setssssssss


# s = {2,42,4,5,3,3,2,5,4,4}
# print(s)

# info = {"Moiz", 19 , False , 5.9  ,19 }
# print(info)
# for value in info:
#     print(value)

# sets = {"talha", 23 , 43 , 52.9  , True , 4}
# print(sets)
# print(type(sets))

# set = {}
# print(type(set))

# moiz = set()
# print(type(moiz))



            # SETS METHOD

                    # UNION SETS
# s1 = {1,2,5,6}
# s2 = {3,2,4,6,7}
# print(s1,s2)
# print(s1.union(s2))
# s1.update(s2)
# print(s1,s2)

                    # INTERSECTION SETS
# s1 = {1,2,5,6}
# s2 = {3,2,4,6,7}
# print(s1,s2)
# print(s1.intersection(s2))
# s2.intersection_update(s1)
# print(s1,s2)

                    # DIFFERENCES SETS
# s1 = {1,2,5,6}
# s2 = {3,2,4,6,7}
# print(s1,s2)
# print(s1.difference(s2))
# s1.difference_update(s2)
# print(s1,s2)


                # ISDISJOINT SETS   <---  ya tb true hota h jb dono sets ma intersection na ho agr intersection hoga to false hojayga

# s1 = {1,2,21,5,61}
# s2 = {3,2,4,6,7}
# print(s1,s2)
# print(s2.isdisjoint(s1))


                    # ISSUPERSET   <---- ya tb true hota h jb ek method ka set ki values dusry set ma ho

# s1 = {1,2,5,6}
# s2 = {1,2}
# print(s1,s2)
# print(s1.issuperset(s2))
# print(s2.issubset(s1))




# s1 = {"karachi" , "lahore" , "peshawar"}
# s2 = {3,2,4,6,7}
# print(s1,s2)
# s1.add("truth")
# print(s1)



# s1 = {"karachi" , "lahore" , "peshawar"}
# s1.remove("lahore")
# print(s1)


# s1 = {"karachi" , "lahore" , "peshawar"}
# s1.pop()
# print(s1)


# s1 = {"karachi" , "lahore" , "peshawar"}
# del s1
# print(s1)


# a = {1,12,2,6,7,8}
# b = {15,0,1,3,6}
# c = a.symmetric_difference(b)
# print(c)























                        # Strings



# letter = "my name is {} and i study in {}"
# name = "Moiz"
# uni = "DUET"
# print(letter.format(name , uni))         #  This is a old method



# name = "Moiz"
# uni = "DUET"
# letter = (f"my name is {name} and i study in {uni}")         #This is a new method
# print(letter)                     
# print(type(letter))

# price = 12.0677
# text = (f"price of suit is {price:.2f} dollar")
# print(text)

# print(f"{2 * 30}")




# def square(n):
#     '''Take in a number n, returns the square of n'''
#     print(n**2)
# square(3)
# print(type(square))
# print(square.__doc__)