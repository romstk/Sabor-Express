from abc import ABC, abstractmethod

#Vamos importar ABC e Abastrctmethod para que esta classe possa declarar um método abastrado para que as classes filhas implementem o método 
class ItemCardapio(ABC): 
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco 

    #Todas as classes filhas irão implementar este método
    @abstractmethod
    def aplicar_desconto(self): 
        pass

        