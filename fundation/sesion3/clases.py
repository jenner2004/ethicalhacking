
class User:
 def __init__ (self, name,email):
    self.name=name
    self.email=email

    print("User Created")
    def show_information(self):
       return f"name{self.name}, email:{self.email}"

user1=User("Cesar","cesar.sinchiguano@gmail.com")
user2=User("Jandry","jandry_2004@gmail.com")
user3=User("Josue","josuealcivar@gmail.com")

# tmp=user1.show_information()
# print(tmp)

print(user1.display())
print(user2.display())
print(user3.display())



