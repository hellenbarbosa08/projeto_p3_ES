from abc import ABC, abstractmethod
from manager import TaskManager
from models import Task, TipoTarefa, Status

class TaskAction(ABC):
    @abstractmethod
    def execute(self, manager: TaskManager): pass

class AddTaskAction(TaskAction):
    def __init__(self, tipo: TipoTarefa, nome: str, descricao: str, status: Status):
        self.tipo = tipo
        self.nome = nome
        self.descricao = descricao
        self.status = status

    def execute(self, manager: TaskManager):
        task = Task(manager.next_id, self.tipo, self.nome, self.descricao, self.status)
        manager.tasks.append(task)
        manager.next_id += 1
        manager.persist()
        print(f"\n✔ Tarefa '{task.nome}' adicionada com ID {task.id}!")

class ListTasksAction(TaskAction):
    def execute(self, manager: TaskManager):
        if not manager.tasks:
            print("\nNenhuma tarefa cadastrada.")
            return
        print("\n--- LISTA DE TAREFAS ---")
        for t in manager.tasks:
            print(f"[{t.id:02d}] {t.nome:20} | {t.status.value:12} | {t.tipo.value}")

