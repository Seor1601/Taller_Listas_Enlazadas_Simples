class LinkedList:
    def __init__(self):
        self.primero = None

    def tamano(self):
        contador = 0
        actual = self.primero

        while actual is not None:
            contador += 1
            actual = actual.siguiente

        return contador

    def invertir(self):
        anterior = None
        actual = self.primero

        while actual is not None:
            siguiente_temporal = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente_temporal

        self.primero = anterior

    def ordenar(self):
        if self.primero is None or self.primero.siguiente is None:
            return

        cambio = True

        while cambio:
            cambio = False
            anterior = None
            actual = self.primero

            while actual is not None and actual.siguiente is not None:
                siguiente = actual.siguiente

                if actual.dato > siguiente.dato:
                    cambio = True

                    actual.siguiente = siguiente.siguiente
                    siguiente.siguiente = actual

                    if anterior is None:
                        self.primero = siguiente
                    else:
                        anterior.siguiente = siguiente

                    anterior = siguiente
                else:
                    anterior = actual
                    actual = actual.siguiente