
from listaEnlazada import LinkedList

def menu():
    lista = LinkedList()

    while True:
        print("\n=== Menu lista enlazada ===")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Mostrar lista")
        print("7. Tamaño de la lista")
        print("8. Invertir lista")
        print("9. Ordenar lista")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            print ("Insertar al inicio")
            dato-input("Escriba el dato")
            ll.insertar_inicio(dato)
            
        elif opcion == "2":
            print ("Insertar al final
            dato-input("Escriba el dato")
            ll.insertar_final(dato)
                   
        elif opcion == "7":
            print("Tamaño de la lista:", lista.tamano())

        elif opcion == "8":
            lista.invertir()
            print("Lista invertida")

        elif opcion == "9":
            lista.ordenar()
            print("Lista ordenada")

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opcion invalida")

menu()
           