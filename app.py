from models import Status, TipoTarefa
from actions import AddTaskAction, ListTasksAction, RemoveTaskAction, UpdateStatusAction

class TaskApp:
    def __init__(self, manager):
        self.manager = manager

    def run(self):
        while True:
            print("\n" + "="*30)
            print("  GERENCIADOR OO DE TAREFAS")
            print("="*30)
            print("1. Adicionar Tarefa\n2. Listar Tarefas\n3. Remover Tarefa\n4. Alterar Status\n0. Sair")
            
            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                self._menu_adicionar()
            elif opcao == "2":
                ListTasksAction().execute(self.manager)
            elif opcao == "3":
                self._menu_remover()
            elif opcao == "4":
                self._menu_status()
            elif opcao == "0":
                print("Encerrando...")
                break
            else:
                print("Opção inválida!")

    def _menu_adicionar(self):
        nome = input("Nome: ")
        desc = input("Descrição: ")
        print("Status: 1. Disponível | 2. Fazendo | 3. Feita")
        st = input("> ")
        status = {"1": Status.DISPONIVEL, "2": Status.FAZENDO, "3": Status.FEITA}.get(st, Status.DISPONIVEL)
        
        AddTaskAction(TipoTarefa.ESTUDO, nome, desc, status).execute(self.manager)

    def _menu_remover(self):
        try:
            tid = int(input("Digite o ID para remover: "))
            RemoveTaskAction(tid).execute(self.manager)
        except ValueError:
            print("ID inválido.")

    def _menu_status(self):
        try:
            tid = int(input("Digite o ID da tarefa: "))
            print("Novo Status: 1. Disponível | 2. Fazendo | 3. Feita")
            st = input("> ")
            status = {"1": Status.DISPONIVEL, "2": Status.FAZENDO, "3": Status.FEITA}.get(st)
            if status:
                UpdateStatusAction(tid, status).execute(self.manager)
            else:
                print("Status inválido.")
        except ValueError:
            print("ID inválido.")

