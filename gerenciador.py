from dataclasses import dataclass
from enum import Enum
from typing import List


class Status(str, Enum):
    DISPONIVEL = "Disponível"
    FAZENDO = "Fazendo"
    FEITA = "Feita"

    @staticmethod
    def from_menu_choice(choice: str) -> "Status":
        mapping = {
            "1": Status.DISPONIVEL,
            "2": Status.FAZENDO,
            "3": Status.FEITA,
        }
        if choice not in mapping:
            raise ValueError("Escolha inválida de status.")
        return mapping[choice]


class TipoTarefa(str, Enum):
    LABORATORIO = "Laboratório"
    ESTUDO = "Estudo"
    GRUPO = "Trabalho em Grupo"
    PROJETO = "Projeto"
    APRESENTACAO = "Apresentação"

    @staticmethod
    def from_menu_choice(choice: str) -> "TipoTarefa":
        mapping = {
            "1": TipoTarefa.LABORATORIO,
            "2": TipoTarefa.ESTUDO,
            "3": TipoTarefa.GRUPO,
            "4": TipoTarefa.PROJETO,
            "5": TipoTarefa.APRESENTACAO,
        }
        if choice not in mapping:
            raise ValueError("Escolha inválida de tipo.")
        return mapping[choice]


@dataclass
class Task:
    id: int
    tipo: TipoTarefa
    nome: str
    descricao: str
    status: Status


class TaskManager:
    def __init__(self) -> None:
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, tipo: TipoTarefa, nome: str, descricao: str, status: Status) -> Task:
        task = Task(id=self.next_id, tipo=tipo, nome=nome, descricao=descricao, status=status)
        self.next_id += 1
        self.tasks.append(task)
        return task

    def list_tasks(self) -> List[Task]:
        return list(self.tasks)


# ====== Templates "acadêmicos" ======
TEMPLATES = [
    (TipoTarefa.LABORATORIO, "Entregar relatório de laboratório", "Organizar dados, concluir análise e formatar o relatório."),
    (TipoTarefa.ESTUDO, "Estudar para a prova ", "Resolver lista de exercícios + revisar teoria (assuntos da prova)."),
    (TipoTarefa.GRUPO, "Fazer trabalho em grupo", "Definir divisão de tarefas, prazos e consolidar versão final."),
    (TipoTarefa.PROJETO, "Revisar código do projeto", "Refatorar trechos críticos, corrigir bugs e rodar testes."),
    (TipoTarefa.APRESENTACAO, "Preparar apresentação", "Montar slides, revisar roteiro e treinar tempo de fala."),
]


def print_status_menu() -> None:
    print("Escolha o status:")
    print("  1) Disponível")
    print("  2) Fazendo")
    print("  3) Feita")


def print_tipo_menu() -> None:
    print("Escolha o tipo de tarefa:")
    print("  1) Laboratório")
    print("  2) Estudo")
    print("  3) Trabalho em Grupo")
    print("  4) Projeto")
    print("  5) Apresentação")


def choose_status() -> Status:
    print_status_menu()
    while True:
        try:
            return Status.from_menu_choice(input("> ").strip())
        except ValueError:
            print("Opção inválida. Tente novamente.")


def choose_tipo() -> TipoTarefa:
    print_tipo_menu()
    while True:
        try:
            return TipoTarefa.from_menu_choice(input("> ").strip())
        except ValueError:
            print("Opção inválida. Tente novamente.")


def main() -> None:
    manager = TaskManager()

    while True:
        print("\nMenu:")
        print("  1) Adicionar tarefa (modelos padroes)")
        print("  2) Adicionar tarefa (personalizada)")
        print("  3) Listar tarefas")
        print("  0) Sair")

        choice = input("> ").strip()

        if choice == "1":
            print("\nModelos disponíveis:")
            for i, (tipo, nome, _) in enumerate(TEMPLATES, start=1):
                print(f"  {i}) [{tipo.value}] {nome}")

            idx = input("> ").strip()
            if not idx.isdigit() or not (1 <= int(idx) <= len(TEMPLATES)):
                print("Modelo inválido.")
                continue

            tipo, nome, desc_padrao = TEMPLATES[int(idx) - 1]
            print(f"Descrição sugerida: {desc_padrao}")
            descricao = input("Descrição (enter para usar a sugerida): ").strip() or desc_padrao
            status = choose_status()

            task = manager.add_task(tipo, nome, descricao, status)
            print(f"Tarefa adicionada com ID {task.id}.")

        elif choice == "2":
            tipo = choose_tipo()
            nome = input("Nome: ").strip()
            descricao = input("Descrição: ").strip()
            status = choose_status()

            task = manager.add_task(tipo, nome, descricao, status)
            print(f"Tarefa adicionada com ID {task.id}.")

        elif choice == "3":
            tasks = manager.list_tasks()
            if not tasks:
                print("Nenhuma tarefa cadastrada.")
            else:
                print("\n--- Tarefas ---")
                for t in tasks:
                    print(f"[{t.id}] ({t.tipo.value}) {t.nome} | {t.status.value}")
                    print(f"     {t.descricao}")

        elif choice == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
