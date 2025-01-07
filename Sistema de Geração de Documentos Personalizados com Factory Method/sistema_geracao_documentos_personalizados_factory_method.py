# Iniciado às 15:54 de 07/01/2025
# Finalizado às 16:23 de 07/01/2025


from abc import ABC, abstractmethod

class Documento(ABC):
    
    @abstractmethod
    def gerar_conteudo(self):
        pass

    def exibir(self):
        print(self.gerar_conteudo())

class Contrato(Documento):

    def gerar_conteudo(self):
        return "Contrato: Este é um contrato jurídico com cláusulas específicas."
    
class Fatura(Documento):

    def gerar_conteudo(self):
        return "Fatura: Detalhes da fatura com impostos calculados."
    
class Relatorio(Documento):
    
    def gerar_conteudo(self):
        return "Relatório: Avaliação de desempenho dos funcionários."
    
    
class GeradorDeDocumentos(ABC):

    @abstractmethod
    def criar_documento(self):
        pass

class GeradorDeContrato(GeradorDeDocumentos):

    def criar_documento(self):
        return Contrato()
    
class GeradorDeFatura(GeradorDeDocumentos):

    def criar_documento(self):
        return Fatura()
    
class GeradorDeRelatorio(GeradorDeDocumentos):
    
    def criar_documento(self):
        return Relatorio()
    





