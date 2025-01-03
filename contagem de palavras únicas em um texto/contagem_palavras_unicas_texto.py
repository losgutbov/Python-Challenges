# Iniciado às 11:29 02/01/2025
# Finalizado às 11:44 02/01/2025

def contar_palavras_unicas(texto):
    if len(texto):
        # Transformando todos os caracteres para mínusculos
        texto = texto.lower()
        # Remover pontuações
        novo_texto = ""
        for letra in texto:
            if letra.isalpha() or letra == " ":
                novo_texto += letra
        # Quebrar texto por espaços em branco
        texto_split = set(novo_texto.split(" "))

        return len(texto_split)
    return 0

casos_de_teste = [
    ("Python é incrível!", 3),  # ['python', 'é', 'incrível']
    ("Python, Python, python...", 1),  # ['python']
    ("Olá mundo! Mundo, olá.", 2),  # ['olá', 'mundo']
    ("Este é um teste simples.", 5),  # ['este', 'é', 'um', 'teste', 'simples']
    ("", 0)  # Texto vazio
]

def rodar_testes():
    for entrada, esperado in casos_de_teste:
        resultado = contar_palavras_unicas(entrada)
        assert resultado == esperado, f"Erro: {entrada} -> {resultado}, esperado {esperado}"
    print("Todos os testes passaram!")

rodar_testes()

# VERSÃO MELHORADA DO CHAT GPT
# import re

# def contar_palavras_unicas(texto):
#     if len(texto):
#         # Transformando todos os caracteres para minúsculos
#         texto = texto.lower()
#         # Remover pontuações usando expressão regular
#         texto = re.sub(r'[^a-zá-ú\s]', '', texto)
#         # Quebrar texto por espaços em branco e garantir palavras únicas
#         texto_split = set(texto.split())

#         return len(texto_split)
#     return 0


# import re

# def contar_palavras_unicas(texto):
#     # Transformando todos os caracteres para minúsculos e removendo pontuações
#     texto = re.sub(r'[^a-zá-ú\s]', '', texto.lower())
    
#     # Quebrar o texto por espaços e contar palavras únicas
#     palavras_unicas = set(texto.split())

#     return len(palavras_unicas)
