soma = 0

numero = int(input('Digite o número inteiro(0 para sair): '))

while numero != 0:
    soma +=numero
    numero = int(input("Digite o número inteiro(0 para sair): "))
print(f"A soma dos números é: {soma}")

# faz a variavel soma, usa o while e se o numero for 0 quebra.