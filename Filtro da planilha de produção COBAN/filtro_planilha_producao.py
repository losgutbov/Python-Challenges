# Iniciado às 09:32 de 09/01/2025

import pandas as pd
from pathlib import Path


class FiltroPlanilha:

    def __init__(self, path_base) -> None:
        self._path_base = path_base

    def ler_planilha(self):
        pass

    def realizar_filtro(self, filtros):
        pass

    def gerar_planilha_resultado(self):
        pass

if __name__ == "__main__":
    filtro = FiltroPlanilha()