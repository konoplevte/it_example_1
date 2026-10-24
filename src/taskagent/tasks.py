_tasks: list[dict] = []

def init_tasks(tasks: list[dict]) -> None:
    global _tasks
    _tasks = tasks

def get_tasks() -> list[dict]:
    return _tasks

def add_task(name: str) -> None:
    _tasks.append({"name": name, "done": False})

def list_tasks() -> str:
    result = ""
    for i, task in enumerate(_tasks):
        result += f"{i + 1}. [{'X' if task['done'] else ' '}] {task['name']}\n"

    return result


def done_task(idx: int) -> None:
    _tasks[idx]["done"] = True

def delete_task(idx: int) -> dict | None:
    try:
        return _tasks.pop(idx)
    except IndexError:
        return None

def get_help() -> str:
    return """
ИИ агент управления задачами

Функциональность:
1. add, которая добавляет задачи
1. list, которая выводит список задач
1. done, которая помечает задачу как выполненную
1. help, которая выводит справку
1. exit, которая позволяет выйти из приложения
"""
