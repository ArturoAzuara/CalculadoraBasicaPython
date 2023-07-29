"""
PROGRAMA REALIZADO POR:
Téc. Arturo Azuara
Calculadora simple con funciones
"""
import os #importa funcionalidades para poder trabajar en el sistema operativo de windows, nos interesa para ejecución en el CMD.
import msvcrt #Tiene muchas funcionalidades, pero la que me interesa es, leer el teclado, para pasar a otra ventana, en este caso, detectar una tecla para cerrar la ventana
print("""
         Bienvenido
        Calculadora
         Sencilla 
            """)
def borrar (): #Función para eliminar contenido de la ventana en el CMD, por esto importamos el modulo "OS".
    os.system("cls")

def menu ():
    print("Introduce un par de numeros")
    while True: #Mientras que sea verdadero, este blucle se seguira repitiendo.
        try: #Excepción utilizada para que diferencie entre un tipo de dato entero de un string.
            numero1 = int(input("Primer numero: "))
            numero2 = int(input("Segundo numero: "))
            borrar() #Implemento la función borrar
            break
        except ValueError: #Al detectar un string lanzara el siguiente mensaje, si detecta un entero seguira la ejecución con normalidad.
            borrar()       #La ventaja de implementar excepciones es que no se cierra el programa abruptamente y permite la fluidez del mismo.
            print("Solo puedo recibir valores enteros, intenta de nuevo")

    opcion = 0
    while True:
        print("""
        Presiona la opcion que gustes:
        1) Suma
        2) Resta
        3) Multiplicación
        4) División
        5) Salir
        """)
        try: #La mismo excepción de arriba
            opcion = int(input("N° de opción: "))
            borrar() #implemento la funcion borrar
            if opcion == 1:
                print("La suma de: ",numero1," y ",numero2," es: ",numero1+numero2)
            elif opcion == 2:
                print("La resta de: ",numero1," y ",numero2," es: ",numero1-numero2)
            elif opcion == 3:
                print("La multiplicación de: ",numero1," y ",numero2," es: ",numero1*numero2)
            elif opcion == 4:
                print("La división de: ",numero1," y ",numero2," es: ",numero1/numero2)
            elif opcion == 5:
                print("¡Gracias, vuelve pronto!")
                break
            else: # De escoger una opcion que no existe en el menú, me regresa el siguiente mensaje.
                print("Error, esa opción no existe prueba con otra")
        except ValueError:
            borrar()
            print("Esa opción no esta en el menú, intenta de nuevo")



menu() #mando a llamar la funcion menu
msvcrt.getch() #La coloco al final, ya que al cerrar el programa, no haga que se cierre abruptamente, se puede observar mejor la funcion al ejecutar el programa en el cmd.
"""
Las funciones van de arriba para abajo, conforme las vayas necesitando,
no puedes comenzar de abajo para arriba, si no, no compilara jamas,
así iran apareciendo conforme las vayas necesitando :)
"""



