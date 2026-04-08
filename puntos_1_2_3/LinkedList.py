class LinkedList:
    def __init__(self):
        self.head = None
    
    #punto 3
        
    def insertar_inicio(self, data):
        new_Node=None(data)
        new_Node.next =self.head
        self.head=new_Node
    
    def insertar_final(self,data):
        new_Node=None(data)
        if self.head is None:
            self.head=new_Node
            return
        current=self.head
        current.traverse()
        current.next= new_Node
    
    def traverse(self):
        while current is not None:
            print(current)
            current=current.next
        
        
    


