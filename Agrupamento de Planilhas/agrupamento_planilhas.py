# Iniciado às 19:08 de 08/01/2025
# Finalizado às 19:50 de 08/01/2025
import pandas as pd
from pathlib import Path


class Agrupador:

    def __init__(self, path_base) -> None:
        self._path_base = path_base

    def ler_planilha(self, path_planilha):
        return pd.read_excel(path_planilha)
        
    def unir_planilhas(self, planilhas):
        return pd.concat(planilhas, axis=0)

    def gerar_planilha_agrupada(self, path, planilha_agrupada):
        planilha_agrupada.to_excel(str(path.parent / "planilha_agrupada.xlsx"))

    def agrupar_plainhas(self):
        path = Path(self._path_base)
        df_geral = pd.DataFrame()
        for planilha in path.rglob("*.xlsx"):
            planilha_atual = self.ler_planilha(str(planilha))
            df_geral = self.unir_planilhas([df_geral, planilha_atual])
        self.gerar_planilha_agrupada(path, df_geral)
        
if __name__ == "__main__":
    agrupador = Agrupador("C:\\Users\\losgu\\Documents\\TRABALHOS\\VIRTUS\\clientes\\2024\\2024")
    agrupador.agrupar_plainhas()