from dataclasses import dataclass
from enum import Enum

class Status(str, Enum):
    DISPONIVEL = "Disponível"
    FAZENDO = "Fazendo"
    FEITA = "Feita"

class TipoTarefa(str, Enum):
    LABORATORIO = "Laboratório"
    ESTUDO = "Estudo"
    GRUPO = "Trabalho em Grupo"
    PROJETO = "Projeto"
    APRESENTACAO = "Apresentação"

@dataclass
class Task:
    id: int
    tipo: TipoTarefa
    nome: str
