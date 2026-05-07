Usuario = input("Ingrese su nombre: ").lower().capitalize()
saludo = "Hola, " + Usuario + "! Bienvenido a la calculadora simple."
print(saludo)
while True:

    print("\nCalculadora")
    print("0. Salir")
    print("1. Suma")
    print("2. Resta") 
    print("3. Multiplicación")
    print("4. División")
    opcion = int(input("Seleccionar una opcion: "))
    if opcion == 0:
        print("El programa ha finalizado")
        break
    elif opcion in [1, 2, 3, 4]:
        num_1 = float(input("Ingresar el primer numero: "))
        num_2 = float(input("Ingresar el segundo numero: "))
        if opcion == 1:
            resultado = num_1 + num_2
            print("El resultado de la suma es:", resultado)
        elif opcion == 2:
            resultado = num_1 - num_2
            print("El resultado de la resta es:", resultado)
        elif opcion == 3:
            resultado = num_1 * num_2
            print("El resultado de la multiplicación es:", resultado)
        elif opcion == 4:
            if num_2 != 0:
                resultado = num_1 / num_2
                print("El resultado de la división es:", resultado)
            else:
                print("Error: No se puede dividir por cero")
    else:
        print("Opción no válida")