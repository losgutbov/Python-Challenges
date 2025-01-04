# Iniciado às 16:41 de 04/01/2025
# Finalizado às 16:49 de 04/01/2025

class LogManager():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._logs = []
        return cls._instance
    

    def log_message(self, level, message):
        self._logs.append({"level": level, "message": message})

    def show_logs(self):
        return self._logs

service1_log = LogManager()
service2_log = LogManager()

service1_log.log_message("INFO", "Service 1 initialized.")
service2_log.log_message("ERROR", "Service 2 failed to connect to the database.")

print(service1_log.show_logs())
# Output:
# [
#     {"level": "INFO", "message": "Service 1 initialized."},
#     {"level": "ERROR", "message": "Service 2 failed to connect to the database."}
# ]


# O CHAT GPT apresentou outra solução como sendo a ideal, 
# no entanto, os pontos que ele adicionou ou alterou dizem respeito 
# ao contexto do desafio e não ao uso do padrão singlenton que no momento era o meu foco.

# from datetime import datetime

# class LogManager:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls, *args, **kwargs)
#             cls._instance._logs = []
#         return cls._instance

#     def log_message(self, level, message):
#         if level not in {"INFO", "WARNING", "ERROR"}:
#             raise ValueError(f"Nível de log inválido: {level}")
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self._logs.append({"timestamp": timestamp, "level": level, "message": message})

#     def show_logs(self):
#         return self._logs

#     def save_logs_to_file(self, filename):
#         with open(filename, "w") as file:
#             for log in self._logs:
#                 file.write(f"{log['timestamp']} [{log['level']}] {log['message']}\n")
