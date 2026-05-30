from logging import log, INFO, ERROR
import logging
from service.pipeline import PipelineClientes

# essa formatação ser ve em todas as classes
logging.basicConfig(
        level=INFO,  # Set the minimum log level
        # format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
      
# Instanciação e execução fluida do pipeline em produção
engenharia_sql = 'sqlite:///empresa.db'

pipeline = PipelineClientes(string_banco=engenharia_sql)

log(INFO, "Extraindo Dados")
pipeline.extrair()

log(INFO, "Tranformad Dados")
pipeline.transformar()

log(INFO, "Carrega Dados")
pipeline.carregar()
