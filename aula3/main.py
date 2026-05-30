import aula3.services.limpador as limpador
import aula3.services.leitor as leitor
import pandas as pd

# Escopo é o código que muda apenas, e somenta apenas, quando contexto daquele muda
# nada mais
# Cria uma separação entre os pedaços de código

# Mude para le json, esse ponto no código não deve mudar 
base_inicial = leitor.le_arquivo("dados.csv")

# caso eu mude o formato da limpeza esse local não muda
limpador.remover_nullos(base_inicial)