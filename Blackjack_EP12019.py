import random
import os
 
#Use se for Windows
def clear():
    os.system('cls')
 
#Use se for Linux/MAC
#def clear():
    #os.system('clear')
 
def embaralha_cartas(lista):
    cartas=lista[:]
    random.shuffle(cartas)
    return cartas
 
def retorna_carta(lista_cartas):
    carta=lista_cartas[0]
    del(lista_cartas[0])
    return carta
 
def dealer():
    cartadealer1=retorna_carta(cartas_embaralhadas)
    cartadealer2=retorna_carta(cartas_embaralhadas)
    somadealer=cartadealer1+cartadealer2
    print('As cartas do dealer são: {0} e {1} (soma: {2})'.format(cartadealer1,cartadealer2,somadealer))
    while somadealer<=17:
        cartanova=retorna_carta(cartas_embaralhadas)
        somadealer+=cartanova
        print('{0} (soma: {1})'.format(cartanova,somadealer))
    return somadealer
 
def madness():
    sorteio = random.randint(5,100)
    return sorteio
 
saldo_inicial=100
saldo=saldo_inicial
play_again='s'
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n **Você possui 3 fichas. Cada jogo gastará 1 delas**')
baralhos=int(input('\n Com quantos baralhos você deseja jogar? (1-4) '))
if baralhos<1 or baralhos>4:
    baralhos=1
    print('Quantidade de baralhos não disponível, jogo definido com 1 baralho')
fichas=3
 
while play_again=='s' and fichas>0 and baralhos<=4 and baralhos>0:
    fichas-=1
    valor_apostado=0
    J = 10
    Q = 10
    K = 10
    A = 1
    deck_de_cartas = [2,3,4,5,6,7,8,9,10,J,Q,K,A]*4*baralhos
    
    valor_apostado=input('Você possui {0} dólares. Qual será o valor da sua aposta? (mínimo: 15) '.format(saldo))
    
    if valor_apostado=='fim' or valor_apostado=='Fim':
        break
    
    valor_apostado=int(valor_apostado)
    
    if valor_apostado>saldo or valor_apostado<15:
        print('Valor escolhido fora de alcance.')
        valor_apostado=input('Você possui {0} dólares. Qual será o valor da sua aposta? (mínimo: 15) '.format(saldo))
        if valor_apostado=='fim' or valor_apostado=='Fim':
            print('Fim do jogo')
            break
