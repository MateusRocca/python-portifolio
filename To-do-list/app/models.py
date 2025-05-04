class Tarefa():
    lista_tarefas = []

    def __init__(self, nome, descricao, prazo):
        self._nome = nome.title()
        self._descricao = descricao.title()
        self._prazo = prazo
        self._prioridade = 'Baixa'
        self._status = False
        Tarefa.lista_tarefas.append(self)

    def __str__(self):
        return f'Nome: {self._nome}\nDescrição: {self._descricao}\nPrazo: {self._prazo}\nPrioridade: {self.prioridade}\nStatus: {self.status}'


    @property
    def prioridade(self):
        return self._prioridade
    @property
    def status(self):
        return 'Concluida ☑' if self._status else 'Em andamento ☐'

    def alternar_status(self):
        self._status = not self._status

    @classmethod
    def listar_tarefas(cls):
        print('\n=== Lista de Tarefas ===\n')
        for i, tarefa in enumerate(cls.lista_tarefas):
            print(f'Tarefa: {i + 1} \n{tarefa}')
            print('------------------------')

tarefa1 = Tarefa('inglês', 'estudar inglês', '3 dias')
tarefa2 = Tarefa('python', 'rever conceitos de dicionário', '1 dia')
tarefa2.alternar_status()
tarefa1.listar_tarefas()