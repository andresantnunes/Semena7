import pandas as pd

def remover_nullos(base_antes: pd.Dataframe)-> pd.Dataframe:
    dados_limpos = base_antes # remover Nones e NaNs
    return dados_limpos