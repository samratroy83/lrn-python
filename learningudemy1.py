ex_var = 5
print(ex_var)
ex_var = 7
print(ex_var)
ex_var = True
print(ex_var)
#asdasd
ex_var = 8*5
print(ex_var) 

add_assign= 5
print(add_assign)
add_assign *= 5
print(add_assign)
print(round(100/3,2))

ex_8 = "orange"
print(ex_8[3])
print("12345678"[2:5])

print("---------------------")


 

def some_function(param):
    print("I am inside a function"+param)
print("I am outside a function")

some_function(" samrat")



celsius = int(input("Please enter an integer value for degrees celsius. "))
 
 
def fahrenheit(cel):
    # To avoid the approximation error that would occur if the float 1.8 was used in the calculation, 1.8 * 10 is used
    # instead, resulting in the integer 18.  To balance this out, 32 is also multiplied by 10 to get 320.  After the
    # calculations in the parentheses are finished, the result is divided by 10, which gives the correct Fahrenheit
    # temperature.
    return (18 * cel + 320) / 10
 
 
print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")100