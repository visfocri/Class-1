import random

elemnts = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
lenght = int(input("De cuantos caracteres sera la contraseña?: "))

password = ""

for i in range(lenght):
    password += random.choice(elemnts)
print("Tu contraseña es: ", password)   
