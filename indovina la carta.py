
from random import *

semi=['bastoni', 'coppe', 'denari', 'spade']
valori=['asso', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'fante', 'cavallo', 're']

n=40

carte = list(range(n))

shuffle(carte)

while True:
    estrai = input('Per estrarre una carta E, altrimenti premi U per uscire. ')
    if estrai in ['u', 'U']:
        print('Quit')
        exit()
    elif estrai in ['e', 'E']:
        print('Continua')
    estratta = carte.pop()      
    n -= 1
    s = estratta//10
    v = estratta%10

    print('Devi indovinare il SEME hai due tentativi a disposizione!')

    tentativo = 0

    for i in range(2):
        indovina = input('scrivi il seme: bastoni, coppe, denari oppure spade: ')
        if indovina == 'bastoni':
            indovina = 'bastoni'
        elif indovina == 'coppe':
            indovina = 'coppe'
        elif indovina == 'denari':
            indovina = 'denari'
        elif indovina == 'sspade':
            indovina = 'spade'
        else:
            print('Hai sbagliato a digitare') 
        if indovina == semi[s]:
            print('Hai indovinato il seme! ')
            tentativo = 1
            break
        else:
            print('Non hai indovinato!')
 
    if tentativo == 1:
        print('Devi indovinare il VALORE hai tre tentativi a disposizione!')
        for i in range(3):
            numero = input('scrivi il valore in questo modo: asso, due, tre, quattro, cinque, sei, sette, fante, cavallo, re: ')
            if numero == valori[v]:
                print('Hai indovinato! ')
                break
            else:
                print('Non hai indovinato! ')
                if i == 2:
                    print('La carta estratta era: ', valori[v], 'di', semi[s] )

    print()
