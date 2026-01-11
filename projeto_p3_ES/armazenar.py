from abc import ABC, abstractmethod
from typing import List
from models import Task

class StorageStrategy(ABC):
    """Classe base abstrata para demonstrar Herança."""
    
    @abstractmethod
    def load(self) -> List[Task]:
        pass

    @abstractmethod
    def save(self, tasks: List[Task]) -> None:
        pass
