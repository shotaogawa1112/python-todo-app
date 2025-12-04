
import json
from todo_models import Todo

def load_todos(path:str) -> list[Todo]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    todos = []
    for item in data:
        todos.append(Todo(item["id"], item["title"], item["done"]))

    return todos

def save_Todos(path:str, todos:list[Todo]):
    data = []
    for todo in todos:
        data.append(todo.to_dict())

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)