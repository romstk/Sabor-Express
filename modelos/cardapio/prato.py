
from modelos.cardapio.item_cardapio import ItemCardapio

#Passando a classe mãe entre os parênteses como se fosse um parâmetro estou dizendo que a classe Prato herda a classe ItemCardapio
class Prato (ItemCardapio):
    def __init__(self, nome, preco, descricao):
        #Para que eu possa utilizar o construtor da classe mãe uso a palavra super
        super().__init__(nome, preco)
        self._descricao = descricao
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)