class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.vazia():
            return self.itens.pop()
        return None

    def topo(self):
        if not self.vazia():
            return self.itens[-1] #inverte a lista, mostrando o último elemento
        return None

    def vazia(self):
        return len(self.itens) == 0

    def __str__(self):
        return str(self.itens)

p = Pilha()
p.empilhar(1)
p.empilhar(2)
p.empilhar(3)
print(p)
