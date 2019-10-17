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
 
