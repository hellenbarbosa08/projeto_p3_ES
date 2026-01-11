import json
import os
from dataclasses import asdict
from typing import List
from models import Task, TipoTarefa, Status
from .base import StorageStrategy

class JsonFileStorage(StorageStrategy):
    """Implementação polimórfica para persistência em JSON."""
    
    def __init__(self, filepath: str = "tasks.json"):
        self.filepath = filepath

    def load(self) -> List[Task]:
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            return [
                Task(
                    id=int(item["id"]),
                    tipo=TipoTarefa(item["tipo"]),
                    nome=str(item["nome"]),
                    descricao=str(item["descricao"]),
                    status=Status(item["status"]),
                ) for item in data
            ]
        except Exception:
            return []

    def save(self, tasks: List[Task]) -> None:
        data = []
        for t in tasks:
            item = asdict(t)
            item["tipo"] = t.tipo.value
            item["status"] = t.status.value
            data.append(item)
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
