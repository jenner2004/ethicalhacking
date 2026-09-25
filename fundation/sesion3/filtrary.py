user=list()
user.append({"id": 1, "name": "Cesar", "email": "Cesar.sinchiguano@gmail.com", "rol": "admin"})
user.append({"id": 2, "name": "Jordan", "email": "Jordan.mera@gmail.com", "rol": "user"})
user.append({"id": 3, "name": "Jandry", "email": "Jandry.garcia@gmail.com", "rol": "user"})
user.append({"id": 4, "name": "Josue", "email": "Josue.Alcivar@gmail.com", "rol": "admin"})

counter=list()


for u in user:
    if u["role"]=="admin":
        print(f"Name: {u['name']}, Email: {u['email']}, Role: (u['role])")
        counter.append(u)


        print(f"Total Admin User: {len(counter)}")
