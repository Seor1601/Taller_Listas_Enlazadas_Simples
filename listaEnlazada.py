class LinkedList:
    def __init__(self):
        self.primero = None

    def tamano(self):
        contador = 0
        actual = self.primero

        while actual is not None:
            contador += 1
            actual = actual.next

        return contador

    def invertir(self):
        anterior = None
        actual = self.primero

        while actual is not None:
            next_temporal = actual.next
            actual.next = anterior
            anterior = actual
            actual = next_temporal

        self.primero = anterior

    def ordenar(self):
        if self.primero is None or self.primero.next is None:
            return

        cambio = True

        while cambio:
            cambio = False
            anterior = None
            actual = self.primero

            while actual is not None and actual.next is not None:
                next = actual.next

                if actual.dato > next.dato:
                    cambio = True

                    actual.next = next.next
                    next.next = actual

                    if anterior is None:
                        self.primero = next
                    else:
                        anterior.next = next

                    anterior = next
                else:
                    anterior = actual
                    actual = actual.next