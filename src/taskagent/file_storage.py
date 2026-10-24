import json
from pathlib import Path

_storage_file = Path("data", "tasks.json")

def init_storage(path: Path) -> None:
    global _storage_file
    _storage_file = path
    _storage_file.parent.mkdir(parents=True, exist_ok=True)

def save_storage(data: list[dict]) -> None:
    with _storage_file.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_storage() -> list[dict]:
    try:
        with _storage_file.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileExistsError:
        return []     