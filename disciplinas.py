letra = input (' digite a letra da disciplina')

letra_mas = letra.upper()

if letra_mas == "P":
    print ('Portugues')
elif letra_mas == 'M':
    print ('Matemática')
elif letra_mas == 'H':
    print ('História')
elif letra_mas == 'G':
    print('Geografia')
elif letra_mas == 'S':
    print('Sociologia')
elif letra_mas == 'I':
    print('Ingles')
elif letra_mas  == 'B':
    print('Biologia')
elif letra_mas == 'Q':
    print('Química')
elif letra_mas == 'e':
    print('Educação Física')
elif letra_mas == 'F':
    print('Física')
elif letra_mas == 'L':
    print('Lógica e linguagem de programação')
elif letra_mas == 'C':
    print('Carreiras e competencias')
elif letra_mas == 'PD':
    print('Processos de desenvolvimento de sofware')
elif letra_mas == 'R':
    print('Redes de Computadores e Segurança da Informação na Nuvem')
else:
    print ('Nao existe nenhuma disciplina para a letra digitada')