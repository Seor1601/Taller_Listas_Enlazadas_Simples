from listaEnlazada import LinkedList

def menu():
    lista = LinkedList()

    while True:
        print("\n=== Menu lista enlazada ===")
        print("7. Tamaño de la lista")
        print("8. Invertir lista")
        print("9. Ordenar lista")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "7":
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
            