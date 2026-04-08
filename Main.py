def menu():

    while True:
        print("\n=== Menu lista enlazada ===")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Mostrar lista")
        print("4. Buscar elemento")
        print("5. Eliminar primer elemento")
        print("6. Eliminar por valor")
        print("7. Tamaño de la lista")
        print("8. Invertir lista")
        print("9. Ordenar lista")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")
    
    match opcion:
        case "1":
            print("insertar al inicion")
            dato=input("Escriba el dato")
            n=Node(dato)
        case "2":
            print("insertar al final")
            dato=input("Escriba el dato")
            n=Node(dato)
        case "3":
        
            