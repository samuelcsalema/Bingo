# Importações necessárias 
import random
import pandas as pd
# Criando a função que gera a tabela
def gerar_bingo():
    # Range dos números na tabela (0 até 100)
    numeros = list(range(101))
    # Randomizando a ordem dos números
    random.shuffle(numeros)
    # Criando a tabela do bingo (lista)
    bingo = []
    # Adicionando os números da tabela em 5 listas de 5 números
    for numero in range(5):
        linha = numeros[numero*5:(numero+1)*5]
        bingo.append(linha)
    # Convertendo a lista em cartilha (DataFrame)
    df_bingo = pd.DataFrame(bingo, columns=["B", "I", "N", "G", "O"])
    # Substituindo o valor central por nulo (X)
    df_bingo.iloc[2,2] = "X"
    # Retornando a tabela do bingo completa
    return df_bingo
# Gerando tabelas
bingo1 = gerar_bingo()
bingo2 = gerar_bingo()
# Exibindo as tabelas
print(bingo1, '\n', bingo2)