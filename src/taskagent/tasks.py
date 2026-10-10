tasks: list = []

def add_task(title: str) -> None:
    tasks.append({
        "title": title,
        "done": False
    })

def list_tasks() -> str:
    result = ""
    for i, task in enumerate(tasks):
        result += f"{i + 1}. [{'X' if task["done"] else ' '}] {task["title"]}\n"

    return result    

def done_task(idx: int) -> None:
    tasks[idx]["done"] = True

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