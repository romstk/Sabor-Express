from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

# Instanciamos este restaurante e fazemos a avaliação e listamos os dados do mesmo mas só se o usuário responder que quer avaliar, senão o sistema não faz a parte de avaliação e listagem dos restaurantes instanciados.  
restaurante_praca = Restaurante('praça', 'gourmet')

bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
prato_paozinho = Prato('Pãozinho', 2.0, 'O melhor pão da cidade ')

bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)



print('Você vai informar o nome e nota para o restaurante. Pode informar quantas avaliações quiser entre 1 e 5. Para encerrar inform N') 
resp = input('Deseja avaliar ? ').upper()
while resp == 'S':
    nome = input('Informe o nome: ')
    nota = int(input('Informe a nota: '))
    while nota > 5 or nota < 1: 
        nota = int(input('Valor inválido. Informe a nota entre 1 e 5 : '))
    restaurante_praca.receber_avaliacao(nome, nota)
    resp = input('Continuar avaliando ?').upper()


if restaurante_praca.media_avaliacoes != '-':
    Restaurante.alternar_estado(restaurante_praca)    
    Restaurante.listar_restaurantes


def main():
    restaurante_praca.exibir_cardapio
    
    

# ponto de inicio do programa, 
if __name__ == '__main__':
    main()
    