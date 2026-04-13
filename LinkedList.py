
class LinkedList:
    def __init__(self):
        self.head = None

    def display (self):
        current = self.head
        while current is not None:
            print(current.data, end= "-->")
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
        if self.head is not None:
            current= self.head
            while current.next is not None:
                current.data=current.next.data
            current=None
        return
    
    def deleteXsearch(self, data):
        current = self.head
        while current is not None:
          if current.data == data:
            current=None
            while current.next is not None:
                current.data=current.next.data
                current = current.next
        return



          
          
          
        



    def delete_end(self):
        if self.head is None:
            print("No hay elementos que eliminar")

        current = self.head
        while current.next is None:
            current = None
        while current.next is not None:
            current = current.next
        current = None
        return

    def ordenar(self):
        

      cambio = True
      if self.head is not None and self.head.next is not None:
        while cambio:
            cambio = False
            anterior = None
            actual = self.head

            while actual is not None and actual.next is not None:
                next = actual.next

                if actual.dato > next.dato:
                    cambio = True

                    actual.next = next.next
                    next.next = actual

                    if anterior is None:
                        self.head = next
                    else:
                        anterior.next = next

                    anterior = next
                else:
                    anterior = actual
                    actual = actual.next

        
             
            

        

        
             
            

        
