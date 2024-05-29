from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')


print('Você vai informar o nome e nota para o restaurante. Pode informar quantas avaliações quisee entre 1 e 5. Para encerrar inform N') 
resp = input('Deseja avaliar ? ').upper()
while resp == 'S':
    nome = input('Informe o nome: ')
    nota = int(input('Informe a nota: '))
    while nota > 5 or nota < 1: 
        nota = int(input('Valor inválido. Informe a nota entre 1 e 5 : '))
    restaurante_praca.receber_avaliacao(nome, nota)
    resp = input('Continuar avaliando ?').upper()



def main():
    Restaurante.alternar_estado(restaurante_praca)
    Restaurante.listar_restaurantes()
    

# ponto de inicio do programa, 
if __name__ == '__main__':
    main()
    