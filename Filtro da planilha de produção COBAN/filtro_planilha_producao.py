# Iniciado às 09:32 de 09/01/2025
# Pausado às 10:19 de 09/01/2025
# Retomado às 10:30 de 09/01/2025
# Finalizado às 10:47 de 09/01/2025

import pandas as pd
from pathlib import Path


class FiltroPlanilha:

    def __init__(self, path_base) -> None:
        self._path_base = path_base

    def _ler_planilha(self, path_planilha):
        return pd.read_excel(path_planilha)

    def _gerar_planilha_resultado(self, path, planilha):
        planilha.to_excel(str(path / "planilnha_agrupada_filtrada.xlsx"), index=False)

    def _selecionar_colunas(self, planilha, colunas):
        return planilha[colunas]

    def _filtrar_por_campos_especificos(self, planilha, filtros):
        planilha_copia = planilha
        for chave, valor in filtros.items():
            if valor is not None:
                if valor != "NOT EMPTY":
                    planilha_copia = planilha_copia[planilha_copia[chave]==valor]
                else:
                    planilha_copia = planilha_copia[planilha_copia[chave].notna()]     
        return planilha_copia 
    
    def _adicionar_zeros(self, valor):
        valor = str(int(valor))
        zeros = 11- len(valor)
        return zeros*"0" + valor

    def _corrigir_cpf(self, planilha):
        if "CPF" in planilha.columns:
            planilha["CPF"] = planilha["CPF"].apply(self._adicionar_zeros)
        return planilha

    def realizar_filtro(self, filtros):
        path = Path(self._path_base) 
        df = self._ler_planilha(str(path / "planilha_agrupada.xlsx"))
        df = self._selecionar_colunas(df, list(filtros))
        df = self._filtrar_por_campos_especificos(df, filtros)
        df = self._corrigir_cpf(df)
        self._gerar_planilha_resultado(path, df)


if __name__ == "__main__":
    filtro = FiltroPlanilha("C:\\Users\\losgu\\Documents\\TRABALHOS\\VIRTUS\\clientes\\2024")
    filtro.realizar_filtro({"CPF":"NOT EMPTY", "Nome Cliente": None, "Prefixo Ag. Responsável":None,
                            "Código Convênio": 1640, "ChaveJ":None})