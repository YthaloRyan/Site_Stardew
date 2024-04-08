from concurrent.futures import ThreadPoolExecutor
import time

class Worker:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} começou a trabalhar")
        time.sleep(2)  # Simulando algum trabalho demorado
        print(f"{self.name} terminou o trabalho")
        return f"{self.name} concluiu o trabalho"

# Função que será chamada para executar o trabalho em uma thread
def execute_work(worker):
    return worker.work()

# Criar instâncias da classe Worker
workers = [Worker(f"Trabalhador {i}") for i in range(5)]

# Criar um ThreadPoolExecutor com 3 threads
with ThreadPoolExecutor(max_workers=3) as executor:
    # Enviar as tarefas para serem executadas no ThreadPoolExecutor
    futures = [executor.submit(execute_work, worker) for worker in workers]

    # Capturar os resultados quando as tarefas forem concluídas
    for future in futures:
        result = future.result()
        print("Resultado:", result)
