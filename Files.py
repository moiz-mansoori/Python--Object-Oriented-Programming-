# agr koi file ho tmhari or usko open krna hoto kch symbols hai or agr ham is ma kch write krna ki koshish krenge to iska data khtm hojay ga
# read = r --> isse ya hota h k ham file ka andr jo lkha hoga wo read krskty hai
# write = w --> isse ya hota h k ham new file create krskty hai or usma kch bh write krskty h
# append = a --> isse ya hota h k ham ek file ka andr kch sentence append krskty hai

# f = open("file.txt", 'w')
# f.write('Hello Moiz')
# f.close()


# f = open("file.txt", 'r')
# print(f)
# text = f.read()
# print(text)
# f.close()


# f = open("file.txt", 'a')
# f.write('Kya haal hai choty')
# f.write(' sb khair to hena')
# f.close()


# f = open("myfile2.txt", 'r')
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         break


# f = open("myfile.txt", 'r')
# i = 0
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     m4 = line.split(",")[3]
#     m5 = line.split(",")[4]
#     print(f"Marks of student {i} in Maths is: {m1}")
#     print(f"Marks of student {i} in English is: {m2}")
#     print(f"Marks of student {i} in Urdu is: {m3}")
#     print(f"Marks of student {i} in PST is: {m4}")
#     print(f"Marks of student {i} in PF is: {m5}")
#     print(line)

# f = open("myfile3.txt", 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()


# agr with sa kroge to f.close lgani ki zrurt nh pregi 
# with open('myfile.txt', 'r') as f:
#    f =  f.read()
# print(f)


# other functions in filehandlings 

# with open("myfile4.txt",'r') as f:
#     print(type(f))
#     # Move to the 10th byte in the file -->iska mtlb hai k jo reading hai wo 10 character ka bd sa start hogi
#     f.seek(10)
#     # Read the next 5 bytes --> 10 character ka bd kay 5 characters print honge
#     data = f.read(5)
#     print(data)


# with open("myfile4.txt",'r') as f:
#     print(type(f))
#     f.seek(10)
#     # ya mthod aesa hai k agr ham bhool jay k ktny character seek kre hai to ya hamy btae ga
#     print(f.tell())
#     data = f.read(5)
#     print(data)


# with open('sample.txt' , 'w') as f:
#     f.write("Hello world!")
#     # isma aesa hoga k jese seek ma hai lkn ya shuru ka 5 characters print krlega
#     f.truncate(5)


# with open('sample.txt', 'r') as f:
#     print(f.read())
