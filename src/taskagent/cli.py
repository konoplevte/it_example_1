from .tasks import add_task, done_task, get_help, list_tasks


def run() -> None:
    while True:
        try:
            command: str = input("> ").strip().lower()

            if command == "add":
                title: str = input("Input title > ")
                add_task(title)
            elif command == "list":
                print(list_tasks())
            elif command == "done":
                index = int(input("Input index > "))
                done_task(index)
            elif command == "help":
                print(get_help())
            elif command == "exit":
                break
            else:
                print("Unknown command")
        except IndexError:
            print('Кривой индекс')
        except ValueError:
            print('Кривое значение')    
