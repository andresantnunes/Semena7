from logging import logging
from sqlalchemy import create_engine
import pandas as pd

class PipelineClientes:
    def __init__(self, string_banco):
        self.engine = create_engine(string_banco)
        self.dados = None
        
    def extrair(self):
        logging.info("Simulação de dados brutos recebidos")
        self.dados = pd.DataFrame({'raw_nome': ['  joão ', 'maria '], 'raw_val': ['10', '20']})
        return self
    
    def transformar(self):
        logging.info("Limpeza de strings e tipagem numérica")

        self.dados['nome'] = self.dados['raw_nome'].str.strip().str.upper()
        self.dados['valor'] = self.dados['raw_val'].astype(int)
        return self

    def carregar(self):
        logging.info("Carga no banco SQL final")
        self.dados[['nome', 'valor']].to_sql('tb_clientes', con=self.engine, if_exists='append', index=False)
        print("Pipeline executado com sucesso!")