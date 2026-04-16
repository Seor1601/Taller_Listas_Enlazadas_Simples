from punto_1 import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insertar_inicio(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertar_final(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node

    def tamano(self):
        contador = 0
        actual = self.head
        while actual is not None:
            contador += 1
            actual = actual.next
        return contador
    
    def invertir(self):
        anterior = None
        actual = self.head

        while actual is not None:
            siguiente = actual.next
            actual.next = anterior
            anterior = actual
            actual = siguiente

        self.head = anterior
    
    def ordenar(self):
        if self.head is None or self.head.next is None:
            return

        cambio = True

        while cambio:
            cambio = False
            anterior = None
            actual = self.head

            while actual is not None and actual.next is not None:
                siguiente = actual.next

                if actual.data > siguiente.data:
                    cambio = True

                    actual.next = siguiente.next
                    siguiente.next = actual

                    if anterior is None:
                        self.head = siguiente
                    else:
                        anterior.next = siguiente

                    anterior = siguiente
                else:
                    anterior = actual
                    actual = actual.next

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    #puntos 4,5 y 6

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" --> ")
            current = current.next
        print("None")

    def search(self, target):
        current = self.head
        while current is not None:
            if current.data == target:
                return current
            current = current.next
        return -1

    def delete_head(self):
        if self.head is None:
            print("No hay elementos que eliminar")
            return
        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("No hay elementos que eliminar")
            return
        
        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next
        
        current.next = None

    def deleteXsearch(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
