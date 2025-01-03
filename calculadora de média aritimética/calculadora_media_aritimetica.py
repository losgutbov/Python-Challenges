# Iniciou às 11:15 02/01/2025
# Finalizado às 11:21 02/01/2025

def calcular_media(lista):
    # Identifica o tamnho da lista
    tamanho = len(lista)
    # Verifica se a lista está vazia
    if tamanho > 0:
        # Calcula e retorna a média dos valores da lista
        return sum(lista)/tamanho
    return None


casos_de_teste = [
    ([10, 20, 30, 40], 25.0),
    ([5], 5.0),
    ([], None),
    ([7, 14, 21], 14.0),
    ([1, 2, 3, 4, 5], 3.0)
]

def rodar_testes():
    for entrada, esperado in casos_de_teste:
        resultado = calcular_media(entrada)
        assert resultado == esperado, f"Erro: {entrada} -> {resultado}, esperado {esperado}"
    print("Todos os testes passaram!")

rodar_testes()

# RESPOSTA MAIS CONCISA DO CHAT GPT
# def calcular_media(lista):
#     return sum(lista) / len(lista) if lista else None