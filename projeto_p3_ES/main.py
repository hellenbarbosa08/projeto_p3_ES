from manager import TaskManager
from app.task_app import TaskApp

def main():
    manager = TaskManager()
    app = TaskApp(manager)
    app.run()

if __name__ == "__main__":
    main()
