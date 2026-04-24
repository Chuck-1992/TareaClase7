import os

# ******************************************************************************************
# Uso de operadores relacionales
# Menú de Opciones con Condicionales y Operadores Relacionales
# ******************************************************************************************

# Función para mostrar el menú al usuario en la consola
def mostrar_menu():
    print("\n************ MENÚ DE OPCIONES ***************")
    print(" 1. Calcular rango de edad")
    print(" 2. Clasificar nota")
    print(" 3. Comparar cadenas")
    print(" 4. Limpiar consola")
    print(" 5. Salir")
    print("*********************************************\n")

# Función para mostrar el resultado en formato tabla
def imprimir_tabla(encabezados, filas):
    # Convertir todo a texto
    filas = [[str(dato) for dato in fila] for fila in filas]

    # Calcular ancho de cada columna
    anchos = []
    for i in range(len(encabezados)):
        ancho_maximo = len(encabezados[i])
        for fila in filas:
            if len(fila[i]) > ancho_maximo:
                ancho_maximo = len(fila[i])
        anchos.append(ancho_maximo)

    # Crear separador
    separador = "+-" + "-+-".join("-" * ancho for ancho in anchos) + "-+"

    # Imprimir encabezados
    print(separador)
    print("| " + " | ".join(f"{encabezados[i]:<{anchos[i]}}" for i in range(len(encabezados))) + " |")
    print(separador)

    # Imprimir filas
    for fila in filas:
        print("| " + " | ".join(f"{fila[i]:<{anchos[i]}}" for i in range(len(fila))) + " |")

    print(separador)

# Inicio del programa
print("\nEscriba 'salir' en cualquier momento para cerrar el programa.")

try:
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción del 1 al 5: ").lower()

        if opcion == "salir" or opcion == "5":
            print("Programa finalizado. Gracias por usar el menú.")
            break

        elif opcion == "1":
          
            while True:
                edad_texto = input("Ingrese su edad: ").lower()

                if edad_texto == "salir":
                    print("Programa finalizado. Gracias por usar el menú.")
                    raise SystemExit

                if not edad_texto.isdigit():
                    print("Error: debe ingresar una edad válida en números enteros.")
                    continue

                edad = int(edad_texto)

                if edad > 150:
                    print("Error: ingresó una edad no válida. Por favor, escriba una edad entre 0 y 150 años.")
                    continue
                elif edad < 12:
                    rango = "Niño/a"
                elif edad < 18:
                    rango = "Adolescente"
                elif edad < 60:
                    rango = "Adulto"
                else:
                    rango = "Adulto mayor"

                print("\nCalcular rango de edad:")
                imprimir_tabla(
                    ["Edad ingresada", "Rango"],
                    [[edad, rango]]
                )
                break

        elif opcion == "2":
            while True:
                nota_texto = input("Ingrese una nota entre 0 y 10: ").lower()

                if nota_texto == "salir":
                    print("Programa finalizado. Gracias por usar el menú.")
                    raise SystemExit

                try:
                    nota = float(nota_texto)
                except ValueError:
                    print("Error: debe ingresar un número válido.")
                    continue

                if nota < 0 or nota > 10:
                    print("Error: la nota debe estar entre 0 y 10.")
                    continue
                elif nota >= 9:
                    clasificacion = "Excelente"
                elif nota >= 7:
                    clasificacion = "Aprobado"
                elif nota >= 5:
                    clasificacion = "Recuperación"
                else:
                    clasificacion = "Reprobado"

                print("\nClasificar nota:")
                imprimir_tabla(
                    ["Nota", "Clasificación"],
                    [[f"{nota:.2f}", clasificacion]]
                )
                break

        elif opcion == "3":
         
            while True:
                cadena1 = input("Ingrese la primera cadena: ").lower()

                if cadena1 == "salir":
                    print("Programa finalizado. Gracias por usar el menú.")
                    raise SystemExit

                if cadena1 == "":
                    print("Error: la primera cadena no puede estar vacía.")
                    continue

                cadena2 = input("Ingrese la segunda cadena: ").lower()

                if cadena2 == "salir":
                    print("Programa finalizado. Gracias por usar el menú.")
                    raise SystemExit

                if cadena2 == "":
                    print("Error: la segunda cadena no puede estar vacía.")
                    continue

                if cadena1 == cadena2:
                    resultado = "Son exactamente iguales"
                elif len(cadena1) > len(cadena2):
                    resultado = "La primera es más larga"
                elif len(cadena1) < len(cadena2):
                    resultado = "La segunda es más larga"
                else:
                    resultado = "Misma longitud, pero distintas"

                print("\nComparar cadenas:")
                imprimir_tabla(
                    ["Cadena 1", "Longitud 1", "Cadena 2", "Longitud 2", "Resultado"],
                    [[cadena1, len(cadena1), cadena2, len(cadena2), resultado]]
                )
                break

        elif opcion == "4":
            os.system("cls")
            print("Consola limpiada correctamente.")

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

except KeyboardInterrupt:
    print("\nCierre realizado correctamente.")
