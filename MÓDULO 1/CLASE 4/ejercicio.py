user = "dan"
password = "2"

usuario = input("escriba su nombre:")
password2 = input("Escriba su contaseña:")

if (usuario.lower() == user and password2 == password):
   print ("Bienvenido", usuario)
elif (usuario.lower() == user and password2 != password):
   print("gay")
else:
   print("Acceso Denegado")

