from storage import JsonFileStorage
from manager import TaskManager
from app import TaskApp

class TaskSystem:
    def __init__(self):
       
        self.storage = JsonFileStorage("tasks_v2.json")
        self.manager = TaskManager(self.storage)
        self.app = TaskApp(self.manager)

    def start(self):
        self.app.run()

if __name__ == "__main__":
    system = TaskSystem()
    system.start()
