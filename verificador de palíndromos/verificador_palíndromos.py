#Iniciou às 10:46 02/01/2025
#Finalizado às 10:58 02/01/2025


def eh_palindromo(termo):
    # Remove espaços em branco e transforma todos em caracteres em minúsculos
    termo = termo.replace(" ", "").lower()
    # Utilizando uma propriedade das listas em Python é possível inverter a ordem dos caracteres da string
    termo_ao_contrario = termo[::-1]
    # Caso o termo e o termo ao contrário sejam iguais, então se trata de um palíndromo
    if termo == termo_ao_contrario:
        return True
    return False

casos_de_teste = [
    # Casos simples
    ("radar", True),
    ("python", False),
    ("madam", True),
    
    # Casos com letras maiúsculas
    ("Radar", True),
    ("MadAm", True),

    # Casos com espaços
    ("A base do teto desaba", True),
    ("nunca odd ou even", False),
    ("never odd or even", True),

    # Casos com caracteres não-palíndromos
    ("hello world", False),
    ("open ai", False)
]

def rodar_testes():
    for entrada, esperado in casos_de_teste:
        resultado = eh_palindromo(entrada)
        assert resultado == esperado, f"Erro: {entrada} -> {resultado}, esperado {esperado}"
    print("Todos os testes passaram!")

rodar_testes()