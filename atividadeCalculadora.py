num1 = int(input('Digite o primeiro número'))
operacao = input('Escolha a operação (+, -, /, *): ')
num2 = int(input('Digite o segundo número'))

if operacao == '+' :
   resultado = num1+num2
elif operacao == "-" :
   resultado = num1-num2
elif operacao == '/' :
   resultado = num1/num2
elif operacao == "*" :
   resultado = num1*num2
else:
   resultado = "Operação Invalida"

print (f"O resultado é {resultado}: ")

#faz as variavies dos numeros, coloca int input faz o if,elif,else e da print.