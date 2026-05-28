import pandas as pd

df_estoque = pd.read_csv('estoque_produtos_100_itens.csv', sep=';')
padrao_limpeza = r'(sabonete|creme dental|detergente|amaciante|shampoo|desinfetante)'
padrao_alimentos = r'(leite|queijo|suco|sal|óleo|arroz|creme|^[creme dental]|presunto|molho|ovos|café|açúcar|cereal|farinha|achocolatado)'

df_limpeza = df_estoque[df_estoque['Descricao'].str.contains(padrao_limpeza, case=False, na=False)].copy()
df_limpeza['Categoria'] = "Limpeza"
df_alimentos = df_estoque[df_estoque['Descricao'].str.contains(padrao_alimentos, case=False, na=False)].copy()
df_alimentos['Categoria'] = "Alimentos"

estoque_categorizado = pd.concat([df_limpeza,df_alimentos], axis=0, ignore_index=True)

df_resultado = estoque_categorizado.sort_values('Codigo')
df_resultado= estoque_categorizado.sort_values('Preco')
df_resultado= estoque_categorizado.sort_values('Preco')

print(df_resultado)
