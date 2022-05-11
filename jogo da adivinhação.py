from random import randint
print('=' * 30, ' JOGO DE ADIVINHAÇÃO', '=' * 30)
print('Olá, seja bem vindo(a) ! Escolha um número entre 1 e 100 e tente me derrotar !')
cont = 0
usuario = 0

computador = randint(1, 100)

while usuario != computador:
    usuario = int(input('Digite um número:'))
    cont += 1
    if usuario < computador:
        print('ERROU !!')
        print('Seu palpite está abaixo do computador. Tente mais uma vez !')
    elif usuario > computador:
        print('ERROU !!')
        print('Vish ... foi longe. Vamos mais uma vez !')
    else:
        print('Você acertou, parabéns. Você tentou {}  vezes me derrotar.'.format(cont))
        print('=' * 30, 'FIM DE JOGO',  '=' * 30)

