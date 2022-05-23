#Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values
dictionary = {}
for i in range (97,123): # 97+26=123
    dictionary[chr(i)]=i
print("your dictionary is here  :", dictionary)