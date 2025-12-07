#Esse código implementa uma fila (estrutura de dados FIFO – First In, First Out) usando uma lista em Python
class fila_com_lista(object):
    #inicializa os atributos
    def __init__(self):
        self.elementos = []

    #incluir elementos na fila
    def incluir_na_fila(self, elemento):
        self.elementos.append(elemento)

    #retira o elemento da fila
    def retirar_da_fila(self):
        if self.elementos:
            self.elementos.pop(0)  # Remove o primeiro elemento

    #reescrevendo o método para recuperar a quantidade de elementos
    def __len__(self):
        return len(self.elementos)

    #reescrever o método para retornar o objeto como caracter
    def __str__(self):
        retorno = '\n'
        for i, elemento in enumerate(self.elementos):
            retorno += f"{i} - {elemento}\n"
        return retorno


fila_com_lista = fila_com_lista()
fila_com_lista.incluir_na_fila(10)
fila_com_lista.incluir_na_fila(20)
fila_com_lista.incluir_na_fila(30)
print(fila_com_lista.__str__())
fila_com_lista.retirar_da_fila()
print(fila_com_lista.__str__())