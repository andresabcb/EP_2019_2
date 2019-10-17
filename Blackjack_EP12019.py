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

 
""" saldo_inicial=100
saldo=saldo_inicial """
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
    for p in dic_jogadores_por_saldo:
 
        valor_apostado=input('Você possui {0} dólares. Qual será o valor da sua aposta {1}? (mínimo: 15) '.format(dic_jogadores_por_saldo[p],p))
        
        if valor_apostado=='fim' or valor_apostado=='Fim':
            break
              
        valor_apostado=int(valor_apostado)
        
        if valor_apostado>dic_jogadores_por_saldo[p] or valor_apostado<15:
            print('Valor escolhido fora de alcance.')
            valor_apostado=input('Você possui {0} dólares. Qual será o valor da sua aposta {1}? (mínimo: 15) '.format(dic_jogadores_por_saldo[p],p))
            if valor_apostado=='fim' or valor_apostado=='Fim':
                print('Fim do jogo')
                break
               
        else: 
            dic_jogadores_por_saldo[p]=dic_jogadores_por_saldo[p]-valor_apostado
            cartas_embaralhadas=(embaralha_cartas(deck_de_cartas))
            carta1=retorna_carta(cartas_embaralhadas)
            carta2=retorna_carta(cartas_embaralhadas)
            soma_de_cartas=carta1+carta2
            if carta1==A:
                if soma_de_cartas+10<=21:
                    carta1=11
                    soma_de_cartas+=10
            if carta2==A:
                if soma_de_cartas+10<=21:
                    carta2=11
                    soma_de_cartas+=10
            print('Suas cartas iniciais são: {0} e {1}, {3} (soma: {2})'.format(carta1,carta2,soma_de_cartas,p))
            
            if soma_de_cartas==21:
                madness=madness()
 
 
 
 
 
