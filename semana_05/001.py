print('Olá mundo!')
#print() - mostra uma mensagem na tela
#print= imprimir / exibir

numero1=int(input('Digite o 1° número: '))
numero2=int(input('Digite o 2° número: '))

soma=numero1+numero2

print(soma)

'''
Explicação dos comandos:

input() : comando que pede uma informação ao usuário.

int() : transforma a informação digitada em número inteiro.

+: operador de adição.

print(): mostra o resultado.

Tradução dos termos: 
input = entrada de dados
int = inteiro (número sem casas decimais)
+ = somar
print = imprimir / exibir

'''

num=int(input('Digite um número: '))

if num % 2 == 0 :
    print('número digitado é par')
else:
    print('número digitado é impar')