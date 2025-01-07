import unittest

from sistema_geracao_documentos_personalizados_factory_method import (
    GeradorDeContrato,
    GeradorDeFatura,
    GeradorDeRelatorio,
    Contrato,
    Fatura,
    Relatorio,
)

class TestFactoryMethod(unittest.TestCase):
    def test_gerador_de_contrato(self):
        fabrica = GeradorDeContrato()
        documento = fabrica.criar_documento()
        self.assertIsInstance(documento, Contrato)
        self.assertEqual(
            documento.gerar_conteudo(),
            "Contrato: Este é um contrato jurídico com cláusulas específicas.",
        )

    def test_gerador_de_fatura(self):
        fabrica = GeradorDeFatura()
        documento = fabrica.criar_documento()
        self.assertIsInstance(documento, Fatura)
        self.assertEqual(
            documento.gerar_conteudo(),
            "Fatura: Detalhes da fatura com impostos calculados.",
        )

    def test_gerador_de_relatorio(self):
        fabrica = GeradorDeRelatorio()
        documento = fabrica.criar_documento()
        self.assertIsInstance(documento, Relatorio)
        self.assertEqual(
            documento.gerar_conteudo(),
            "Relatório: Avaliação de desempenho dos funcionários.",
        )

    def test_integracao_geracao_de_documentos(self):
        # Testando a geração de documentos de forma integrada
        fabricas = [
            GeradorDeContrato(),
            GeradorDeFatura(),
            GeradorDeRelatorio(),
        ]
        conteudos_esperados = [
            "Contrato: Este é um contrato jurídico com cláusulas específicas.",
            "Fatura: Detalhes da fatura com impostos calculados.",
            "Relatório: Avaliação de desempenho dos funcionários.",
        ]

        for fabrica, conteudo_esperado in zip(fabricas, conteudos_esperados):
            documento = fabrica.criar_documento()
            self.assertEqual(documento.gerar_conteudo(), conteudo_esperado)

if __name__ == "__main__":
    unittest.main()