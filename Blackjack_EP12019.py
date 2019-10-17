import random
 
 
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
 
 
pergunta_quantos_jogares = input('quantos jogadores na partida? ')
 
jogadores = []
lista_saldo_jogadores = []
i = 0
contador = 0
dic_jogadores_por_saldo = {}
 
while i != int(pergunta_quantos_jogares):
    nome_do_jogador = input('nome do jogador {0} '.format(i+1)) 
    jogadores.append(nome_do_jogador)
    i += 1
while contador < len(jogadores):
    lista_saldo_jogadores.append(100)
    contador+=1
 
for i in range(0,len(jogadores)):
    dic_jogadores_por_saldo[jogadores[i]] = lista_saldo_jogadores[i]
 
 
 
 
 
