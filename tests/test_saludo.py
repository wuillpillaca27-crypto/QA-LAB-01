def saludar(nombre):
   return f"Holla {nombre }" 
def test_saludar():
   assert saludar("Ana") == "Holla Ana"