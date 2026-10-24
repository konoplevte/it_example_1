import json
from pathlib import Path

STORAGE_FILE = Path("data", "tasks.json")
STORAGE_FILE.parent.mkdir(parents=True, exist_ok=True)

def save_storage(data: list[dict]) -> None:
    with STORAGE_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_storage() -> list[dict]:
    try:
        with STORAGE_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileExistsError:
        return []     