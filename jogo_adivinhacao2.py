import random 

numero = random. randint (1,5)

tentativa = 0 

while tentativa <5
    palpite = int(input ('Digite o seu palpite 1 até o 5: '))
    tentativa += 1

    if palpite == numero:
        print ('Voce acertou o número!')
        break
    elif palpite <numero: 
        print('O número é maior')
    

 


