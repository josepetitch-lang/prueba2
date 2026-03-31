# TypeError por concatenar texto + número

# name = input("Nombre: ")
# age = int(input("Edad: "))
# print("Hola " + name + ", tienes " + age + " años.")

# NameError por variable mal escrita

# price = 100
# discount = 0.2
# final_price = price - (precio * discount)
# print(final_price)

# # IndexError por salirte del rango

# user = {"name": "Ana", "email": "ana@mail.com"}
# print("Edad:", user["age"])

# # Bug lógico (NO crashea) — promedio incorrecto

# scores = [10, 9, 8]
# avg = sum(scores) / (len(scores) - 1)
# print("Promedio:", avg)

# # UnboundLocalError por variable usada antes de asignar

def total_with_tax(amount):
    if amount > 0:
        total = amount * 1.19
    return total

print(total_with_tax(0))