import os
os.system("cls")

# Inicialización de variables
nombre_cliente = ""         # Usaremos para capturar el nombre de cliente
direccion_cliente = ""      # Usaremos para capturar la dirección de cliente
cantidad_pizzas = 0         # Usaremos para capturar cantidad de pizzas solicitadas por el cliente
tipo_pizza = ""             # Usaremos para capturar el tipo de pizza escogida por el cliente
precios_pizza = 5000        # Asignamos precio fijo para todas las pizzas 
total_pizzas_vendidas = 0   # Acumulador para el total de pizzas vendidas
total_venta_diaria = 0      # Acumulador para el monto total de la venta diaria

# Funcion para mostrar menu de pizzas
def menu_pizzas():
    print("____________MENU PIZZAS____________\n  ") 
    print("***         Margarita           ***    ")
    print("***         Napolitana          ***    ")
    print("***         Peperoni            ***    ")
    print("***         Española            ***    ")
    print("***         Marinera            ***    ")
    print("***         Fugazza             ***    ")
    print("***         Hawaiana            ***    ")
    print("***         Fungi               *** \n ")

# Saludo de bienvenida
print("¡Bienvenido a Pizzeria del Sur! \n ")


# Bucle para tomar los pedidos de los clientes
while True:
    # Captura del nombre del cliente
    nombre_cliente = input("Ingrese nombre del cliente o 'salir' para terminar turno: \n")

    # Salir del bucle si se ingresa "salir"
    if nombre_cliente.lower() == "salir": # Convertimos todos el texto ingresado a minuscula para comparar con "salir"
        break
    
    # Captura de la dirección del cliente
    direccion_cliente = input("Ingrese dirección del cliente: \n")
   

    # Captura de la cantidad de pizzas 
    
    cantidad_pizzas = int(input("Ingrese cantidad de pizzas solicitadas por el cliente: \n"))

    # Mostramos mensaje para solicitar el tipo de pizza
    print("Ingrese el tipo de pizza: \n")
    menu_pizzas()    # Mostramos menu de pizzas al vendedor

    # Captura del tipo de pizza
    tipo_pizza = input()

    # Mostrar el pedido recibido
    print("\n___Pedido completado______ \n")
    print("Cliente:", nombre_cliente)
    print("Dirección:", direccion_cliente)
    print("Cantidad:", cantidad_pizzas)
    print("Tipo:", tipo_pizza, "\n" )
    print("___Ingrese nuevo pedido___ \n")
    
    
    # Actualización del total de pizzas y monto recibido
    total_pizzas_vendidas = total_pizzas_vendidas + cantidad_pizzas             # Acumulamos la suma total de pizzas vendidas
    total_venta_diaria = total_venta_diaria + cantidad_pizzas * precios_pizza   # Acumulamos la suma total de la venta diaria 

# Mostrar resumen del día
print("\n Resumen del día:")
print("Cantidad total de pizzas vendidas:", total_pizzas_vendidas)
print("Monto recibido durante el día: \n", total_venta_diaria)

# Fin

print("Implementado por Leonardo Cofre Oyarzun ")
