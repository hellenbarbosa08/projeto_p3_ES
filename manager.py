from typing import List, Optional
from storage import StorageStrategy

class TaskManager:
    _instance: Optional["TaskManager"] = None

    def __new__(cls, storage: StorageStrategy) -> "TaskManager":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, storage: StorageStrategy):
        if getattr(self, "_initialized", False):
            return
        self.storage = storage
        self.tasks = self.storage.load()
        self.next_id = max((t.id for t in self.tasks), default=0) + 1
        self._initialized = True

    def persist(self):
        self.storage.save(self.tasks)
