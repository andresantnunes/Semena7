import sqlite3
import os

def ler_dados_filtrados(caminho_banco):
    # Utilizando o 'with' para garantir o fechamento seguro da conexão
    with sqlite3.connect(caminho_banco) as conexao:
        # cursor é literalemente o texto do SQL que vamos executar
        cursor = conexao.cursor()
        
        # O dbt gerou esta tabela automaticamente com os filtros aplicados
        cursor.execute("SELECT * FROM clientes_ativos")
        resultados = cursor.fetchall()
        
        print("Clientes Ativos (Filtrados pelo dbt):")
        for linha in resultados:
            print(f"ID: {linha[0]} | Nome: {linha[1]} | Idade: {linha[2]} | Status: {linha[3]}")

if __name__ == "__main__":
    # Define o caminho do seu banco SQLite (deve ser o mesmo mapeado no profiles.yml do dbt)
    CAMINHO_BANCO = "loja.db"
    
    
    # 2. Se o dbt filtrou com sucesso, lê os dados usando a conexão 'with'
    if sucesso and os.path.exists(CAMINHO_BANCO):
        ler_dados_filtrados(CAMINHO_BANCO)