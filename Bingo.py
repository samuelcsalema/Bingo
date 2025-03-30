import random
import pandas as pd

def gerar_bingo():
    numeros = list(range(101))
    random.shuffle(numeros)

    bingo = []
    for i in range(5):
        linha = numeros[i*5:(i+1)*5]
        bingo.append(linha)

    df_bingo = pd.DataFrame(bingo, columns=["B", "I", "N", "G", "O"])
    df_bingo.iloc[2,2] = "X"
    return df_bingo

bingo1 = gerar_bingo()
bingo2 = gerar_bingo()

bingo1, bingo2
