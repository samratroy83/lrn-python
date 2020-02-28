veg = input("please enter")

if veg=="tomao":
    print("this is tomato")
else :
    print("not tomatotomao")


    
from random import randint
one_to_ten = randint(1, 10)
 
if one_to_ten == 1:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is I.")
elif one_to_ten == 2:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is II.")
elif one_to_ten == 3:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is III.")
elif one_to_ten == 4:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is IV.")
elif one_to_ten == 5:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is V.")
elif one_to_ten == 6:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VI.")
elif one_to_ten == 7:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VII.")
elif one_to_ten == 8:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VIII.")
elif one_to_ten == 9:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is IX.")
else:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is X.")


user_str = input("Please enter a string.")
 
count = 0  # This variable will be used to hold the number of characters in the string.
# This for loop adds 1 to count for each character in user_str.
for char in user_str:
    count += 1
 
print(user_str)  
print(count)
print("===================================")

mixed_case = "A Song of Ice and Fire"
print(mixed_case.isupper())  
print(mixed_case.islower())  
print(mixed_case.upper())  
print(mixed_case.lower())  
print(mixed_case.istitle())  
title_case = mixed_case.title()
print(title_case)  
print(mixed_case.startswith("A"))  
print(mixed_case.endswith("e"))  
words = mixed_case.split()
print(words)  
print("".join(words).isalpha()) 