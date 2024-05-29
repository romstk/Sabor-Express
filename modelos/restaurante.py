from collections.abc import Iterable
from modelos.avaliacao import Avaliacao

class Restaurante: 
    restaurantes = []

    #ao instanciar a classe passamos os parametros e ja a adicionamos a lista restaurantes
    def __init__(self, nome, categoria):
        self._nome = nome.title()  #title - primeira letra maiuscula  
        self._categoria = categoria.upper() #upper - todas letras maiusculas  
        self._ativo = False 
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls): 
        print(f"{'Nome '.ljust(25)} | {'Categoria'.ljust(25)} |{'Avaliacao'.ljust(25)}| {'Status'}")
        for restaurante in cls.restaurantes: 
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
        
    @property
    def ativo(self): 
        return '✅' if self._ativo else '❌'

    def alternar_estado(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self): 
        #Se o restaurante ainda não tiver avaliações vai retornar zero
        if not self._avaliacao: 
            return '-'
        #senão vamos fazer a soma das notas usando uma função sum que irá ler dentro da lista de avaliações da classe e pegando somente os campos _nota para somá-los 
        # avaliacao após o for - > variável que usada para iterar a lista de self._avaliacao. A cada iteracao em avaliacao o sistema vaia somar desta variaável avaliação a nota, portanto estas duas primeiras variáveis precisam ter os mesmos nomes pois estão relacionadas/são as mesmas com funcionaliades diferentes para funcionar a função sum.
        media_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media_das_notas = round(media_das_notas/(len(self._avaliacao)),1)
        return media_das_notas
