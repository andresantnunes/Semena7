import pandas as pd
import seaborn as sns

tempo = pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'])
vendas = [100, 150, 130, 210]
categoria = ['Eletrônicos', 'Eletrônicos', 'Roupas', 'Roupas']

df_vendas = pd.DataFrame({
    'tempo': tempo,
    'vendas': vendas,
    'categoria': categoria
})

print(df_vendas.head())



sns.set_theme(style="darkgrid")
sns.lineplot(
    x=df_vendas['tempo'], 
    y=df_vendas['vendas'], 
    hue=df_vendas['categoria'], # hue -> tonalidade
    palette="dark" # Define uma paleta de cores escuras
    )