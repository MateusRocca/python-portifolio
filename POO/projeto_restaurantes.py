class Restaurante():
    restaurantes = []

    def __init__(self, nome, categoria):
        '''
        __init__ é fundamental para inicializar os atributos da instância, 
        permitindo definir valores padrão, como o atributo ativo sendo False.
        '''
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self) #Adicione este objeto inteiro (que acabei de criar) à lista de restaurantes.
    
    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria} | Status: {self.ativo}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'Restaurante: {restaurante.nome} | Categoria: {restaurante.categoria}')


restaurante1 = Restaurante('Mogiana', 'Mineira')

Restaurante.listar_restaurantes()