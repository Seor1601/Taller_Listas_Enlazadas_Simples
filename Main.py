
from LinkedList import LinkedList 
from listaEnlazada import LinkedLists

def menu():
    ll=LinkedList()
    l2=LinkedLists()
    while True:
        print("\n=== Menu lista enlazada ===")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Tamaño de la lista")
        print("4. Mostrar lista")
        print("5. Buscar valor")
        print("6. Eliminación por búsqueda")
        print("7. Eliminación del primer elemento")
        print("8. Invertir lista")
        print("9. Ordenar lista")
        print("10.Eliminación del último elemento")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            print ("Insertar al inicio ")
            dato=int(input("Escriba el dato "))
            ll.insertar_inicio(dato)
            
        elif opcion == "2":
            print ("Insertar al final ")
            dato= int(input("Escriba el dato "))
            ll.insertar_final(dato)
        
        elif opcion == "3":
            print("Tamaño de la lista:", ll.tamano())
        
        elif opcion == "4":
            print("Mostrar nodos")
            ll.display()

        elif opcion == "5":
            print("Buscar dato")
            target=int(input("Ingrese el valor del dato que desea buscar "))
            if(ll.search(target)!=-1):
                print("La posición del elemento es ",ll.search(target))
            else:
                print("El elemento buscado no se encuentra")

                   
        elif opcion == "6":
            print("Eliminación por búsqueda")
            data=int(input("Ingrese el dato del nodo que desea eliminar "))
            ll.deleteXsearch(data)
            ll.display()

        elif opcion == "7":
            print("Eliminación del primer elemento")
            ll.delete_head()
            ll.display()

        elif opcion == "8":
            ll.invertir()
            print("Lista invertida")
            ll.display()

        elif opcion == "9":
            ll.ordenar()
            print("Lista ordenada")
            ll.display()

            # este es un plus no pedido
        elif opcion=="10":
            print("Eliminación del último elemento")
            ll.delete_end()
            ll.display()

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opcion invalida")

menu()
           