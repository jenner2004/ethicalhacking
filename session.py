# # int variable = 10 

# # VARIABLES 


# number= 10 

# name= " Jandry Garcia"

# active= True

# if number>5: 
#   print("The number is greater than 5 ")

# else:
#   print("The number is less than 5 ")

#   for i in range(10):
#     print("The number is :", i)
#     print( "The number id: {i}")  


#     students=list()
#     for i in range(100):
#         students.append(i)  

# for i in students:
#    print("The student number is :", i)


# names= ["Carlos":,"Maria", "Jose"]
# for name in names:
#  print(name)   



# names= {"Carlos":1 ,"Maria":2, "Jose":3}

# print(names["Jose"])

# for name in names.items{}:
#  print(name) 

# Lista con exactamente 10 diccionarios
inventario = [
    {"id": 1, "producto": "Laptop", "precio": 850.00, "stock": 12},
    {"id": 2, "producto": "Mouse", "precio": 25.50, "stock": 45},
    {"id": 3, "producto": "Teclado", "precio": 45.00, "stock": 30},
    {"id": 4, "producto": "Monitor", "precio": 200.00, "stock": 8},
    {"id": 5, "producto": "Audífonos", "precio": 60.00, "stock": 25},
    {"id": 6, "producto": "Webcam", "precio": 50.00, "stock": 15},
    {"id": 7, "producto": "Impresora", "precio": 150.00, "stock": 5},
    {"id": 8, "producto": "Tablet", "precio": 300.00, "stock": 10},
    {"id": 9, "producto": "Smartphone", "precio": 500.00, "stock": 20},
    {"id": 10, "producto": "Parlantes", "precio": 40.00, "stock": 18}
]


for id in inventario:
    if id['stock']>9:
        print("A pasado")
    else:
        print("A perdido")



 