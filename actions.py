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

class RemoveTaskAction(TaskAction):
    def __init__(self, task_id: int):
        self.task_id = task_id

    def execute(self, manager: TaskManager):
        original_len = len(manager.tasks)
        manager.tasks = [t for t in manager.tasks if t.id != self.task_id]
        if len(manager.tasks) < original_len:
            manager.persist()
            print(f"\n✔ Tarefa {self.task_id} removida.")
        else:
            print(f"\n❌ Erro: Tarefa com ID {self.task_id} não encontrada.")

class UpdateStatusAction(TaskAction):
    def __init__(self, task_id: int, new_status: Status):
        self.task_id = task_id
        self.new_status = new_status

    def execute(self, manager: TaskManager):
        for t in manager.tasks:
            if t.id == self.task_id:
                t.status = self.new_status
                manager.persist()
                print(f"\n✔ Status da tarefa {self.task_id} alterado para {self.new_status.value}.")
                return
        print(f"\n❌ Erro: ID {self.task_id} não encontrado.")
