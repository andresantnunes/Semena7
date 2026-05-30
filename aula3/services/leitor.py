import pandas as pd

def le_arquivo(nome_arquivo: str)-> pd.Dataframe:
    dados_lidos = pd.read_csv(nome_arquivo)
    return dados_lidos