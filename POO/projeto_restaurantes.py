class Restaurante():
    restaurantes = []

    def __init__(self, nome, categoria):
        '''
        __init__ é fundamental para inicializar os atributos da instância, 
        permitindo definir valores padrão, como o atributo ativo sendo False.
        '''
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False #O _ na frente do nome torna o atributo privado
        Restaurante.restaurantes.append(self) #Adicione este objeto inteiro (que acabei de criar) à lista de restaurantes.
    
    def __str__(self):
        return f'Nome: {self._nome} | Categoria: {self._categoria} | Status: {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
    
    @property    
    def ativo(self):
        return 'Ativo ☑' if self._ativo else 'Desativado ☐'
    
    def alterar_estado(self):
        self._ativo = not self._ativo


restaurante1 = Restaurante('Mogiana', 'Mineira')
restaurante2 = Restaurante('monster', 'lanche')
restaurante1.alterar_estado()
restaurante2.alterar_estado()

Restaurante.listar_restaurantes()
