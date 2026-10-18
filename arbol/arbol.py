class Nodo:
    def __init__ (self, codigo):
        self.codigo = codigo
        self.izq = None
        self.der = None


class ArbolNodos:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, codigo):
        if self.raiz is None:
            self.raiz = Nodo(codigo)
        else:
            self._insertar(self.raiz, codigo, 1)

    def _insertar(self, nodo, codigo, nivel):
        if codigo == nodo.codigo:
            raise Exception("El codigo ya se encuentra registrado")
        
        if codigo < nodo.codigo:
            if nodo.izq is None:
                if nivel >= 4:
                    raise Exception("No puede exceder 4 niveles")
                nodo.izq = Nodo(codigo)
            else:
                self._insertar(nodo.izq,codigo,nivel + 1)

        elif codigo > nodo.codigo:
            if nodo.der is None:
                if nivel >=4:
                    raise Exception("No puede exceder 4 niveles")
                nodo.der = Nodo(codigo)
            else:
                self._insertar(nodo.der, codigo, nivel + 1)

    def buscar(self, codigo):
        return self._buscar(self.raiz, codigo)
    
    def _buscar(self, nodo, codigo):
        if nodo is None:
            return False
        if nodo.codigo == codigo:
            return True
        if codigo < nodo.codigo:
            return self._buscar(nodo.izq, codigo)
        return self._buscar(nodo.der, codigo)
    
    def preorden(self):
        datos = []
        self._preorden(self.raiz, datos)
        return datos
    
    def _preorden(self, nodo, datos):
        if nodo:
            datos.append(nodo.codigo)
            self._preorden(nodo.izq, datos)
            self._preorden(nodo.der, datos)
    
    def inorden(self):
        datos = []
        self._inorden(self.raiz, datos)
        return datos
    
    def _inorden(self, nodo, datos):
        if nodo:
            self._inorden(nodo.izq,datos)
            datos.append(nodo.codigo)
            self._inorden(nodo.der, datos)
    
    def postorden(self):
        datos = []
        self._postorden(self.raiz, datos)
        return datos
    
    def _postorden(self, nodo, datos):
        if nodo:
            self._postorden(nodo.izq,datos)
            self._postorden(nodo.der, datos)
            datos.append(nodo.codigo)

    def limpiar(self):
        self.raiz = None
        

