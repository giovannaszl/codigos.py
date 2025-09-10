#contador = 1
#while contador <= 10:
    #print(contador)
    # contador = contador+1

#condicao = False
#while True:
    #print('Este bloco sempreserá execultado pelo menos uma vez.')
    #if not condicao:
        #break
    # Outras operações


# While tradicional pode não execultar se 'condição' for False
#while condicao:
    # Bloco de código

# Do-while emulado sempre execulta pelo menos uma vez
#while True:
    # Bloco de código
    #if not condicao:
        #break

#while True:
    #escolha = input('Escolha uma opção (1, 2, ou 3): ')
    # Processamento de escolha 
   # continuar = input('Deseja continuar? (s/n): ')
    #if continuar.lower() != "s":
        #break

# Lista de registros (pode estar vazia)
registros = []  # ou ['registro1', 'registro2', ...]

# Procedimentos de inicialização
def inicializacao():
    print("Executando inicialização...")

# Processamento de um registro
def processar(registro):
    print(f"Processando {registro}")

# Procedimentos de finalização
def finalizacao():
    print("Executando finalização...")

# Simulação do do-while
def processar_registros(registros):
    inicializacao()
    
    i = 0
    while True:
        # Se a lista estiver vazia, o loop executa uma vez e já para
        if i < len(registros):
            processar(registros[i])
            i += 1
        else:
            # Nenhum registro para processar (ou já processou todos)
            break
    
    finalizacao()

# Teste com lista vazia
processar_registros([])

print("\n---\n")

# Teste com lista com dados
processar_registros(['registro1', 'registro2'])
