
from operacionnumeros import *

class Listas(Intermedio):
    def __init__(self, lista=[]):
        self.lista=lista
    def presentarLista(self):
        for i in self.lista:
            print (i)

    def buscarLista(self,valor):           
        if valor in self.lista:
            print("Se ha encontrado el valor de {} en la lista".format(valor))
        else:
            print("Valor no encontrado el valor de {} en la lista".format(valor))

    def listaFactorial(self):
        for i in self.lista:
            if type(i) == int:
                print("El factorial del numero {} es {}".format(i,obj.factorial(i)))
    def listaPrimo(self):
        for i in self.lista:
            if type(i)==int:
                obj.primo(i)

    def listaNotas(self,listaNotasDicccionario):
        print("Notas")
        for i in listaNotasDicccionario:
            for clave , valor in i.items():
                print("El estudiante {} obtuvo una nota de {}".format(clave,valor))

    def insertarLista(self,posicion,valor):
        auxlist=[]
        for i in range(len(self.lista)):
            if i < posicion:
                auxlist.append(self.lista[i])
        auxlist.append(valor)
        auxlist = auxlist+self.lista[posicion:]   
        return auxlist

    def eliminarLista(self,valor):
        for i in self.lista:
            if i == valor:
                self.lista.remove(valor) 
        return self.lista

    def retornar(self,pos):
        for posicion,valor in enumerate (self.lista):
            if pos == posicion:
                print(valor) 
        self.lista.pop(pos)
        print(self.lista)


    def tuplalista(self,tupla):
        list = []
        for i in tupla:
            list.append(i)
        return list

               
   
# obj = Listas(["Ecuador",
#                 "España",
#                 "Italia",
#                 "Inglaterra",
#                 "Francia"])
obj = Listas(["hola",5,4,6,"hola",7,8,9,"hola",7])
# obj.presentarLista()
# obj.buscarLista("inglaterra")
# obj.listaFactorial()
# obj.listaPrimo()
# obj.listaNotas([{"Miguel":8 , "Andres":7 }])

# print(obj.insertarLista(posicion=1,valor="yep"))
tupla=(4,5,"hola mundo","mi tarea",14)
print(obj.tuplalista(tupla))
