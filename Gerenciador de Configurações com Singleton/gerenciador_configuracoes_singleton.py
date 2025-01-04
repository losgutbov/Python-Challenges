# Iniciado às 15:57 de 04/01/2025
# Finalizado às 16:06 de 04/01/2025


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

class ConfigManager(Singleton):
    
    def __init__(self):
        if not hasattr(self, "_configs"): # Correção apresentada pelo CHAT-GPT para evitar que o configs seja inicializado toda vez, 
                                            # já que o singleton não impede que o __init__ seja iniciado ao gerar uma nova instânica.
            self._configs = {}

    def set_config(self, key, value):
        self._configs[key] = value

    def get_config(self, key):
        if key in self._configs:
            return self._configs[key]
        return None
    
    def list_configs(self):
        return self._configs
    

config1 = ConfigManager()
config1.set_config("theme", "dark")
print(config1.get_config("theme"))  # Output: "dark"

config2 = ConfigManager()
print(config2 is config1)  # Output: True (mesma instância)

config2.set_config("theme", "light")
print(config1.get_config("theme"))  # Output: "light" (reflete a mudança)

config2.set_config("language", "en")
print(config1.list_configs())  # Output: {"theme": "light", "language": "en"}

print(config1.get_config("font_size"))  # Output: None


# Solução IDEAL do CHAT GPT:
# class ConfigManager:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls, *args, **kwargs)
#             cls._instance._configs = {}  # Inicializa a variável aqui para evitar sobrescrita
#         return cls._instance

#     def set_config(self, key, value):
#         """Define ou atualiza uma configuração."""
#         self._configs[key] = value

#     def get_config(self, key):
#         """Retorna o valor de uma configuração ou None se não existir."""
#         return self._configs.get(key)

#     def list_configs(self):
#         """Retorna todas as configurações como um dicionário."""
#         return self._configs
