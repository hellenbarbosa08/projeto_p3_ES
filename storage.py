from abc import ABC, abstractmethod
from typing import List
import json
import os
from models import Task, TipoTarefa, Status

class StorageStrategy(ABC):
    @abstractmethod
    def load(self) -> List[Task]: pass
    
    @abstractmethod
    def save(self, tasks: List[Task]) -> None: pass

class JsonFileStorage(StorageStrategy):
    def __init__(self, filepath: str = "tasks.json"):
        self.filepath = filepath

    def load(self) -> List[Task]:
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            return [Task(
                id=item['id'],
                tipo=TipoTarefa(item['tipo']),
                nome=item['nome'],
                descricao=item['descricao'],
                status=Status(item['status'])
            ) for item in data]
        except Exception:
            return []

    def save(self, tasks: List[Task]) -> None:
        data = [{
            "id": t.id,
            "tipo": t.tipo.value,
            "nome": t.nome,
            "descricao": t.descricao,
            "status": t.status.value
        } for t in tasks]
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
