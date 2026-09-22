# def greeting():
#     return print("Hello mundo")

# def greeting2(name):
#     return print("Hello, {name}!")

# def division(a,b):
#     if b==0:
#         return print("THe second number is zero")
#     else:
#         return print( f"The division of {a} and {b} is: {a/b}")


# division(10,2)
# greeting2("Juan")
try:
  
    variable1=int(input("enter a number: "))
except ValueError:
       print("The value entered is not a number")

print ( f"The number entered is: {variable1}")