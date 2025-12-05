
import json
from todo_models import Todo

def load_todos(path:str) -> list[Todo]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

    except FileNotFoundError:
        print("ファイルが存在しません。空のリストを作成します。")
        return []

    except json.JSONDecodeError:
        print("JSONファイルの読み込みに失敗しました。空のリストを作成します。")
        return []

    todos = []
    for item in data:
        todos.append(Todo(item["id"], item["title"], item["done"]))
    return todos

def save_todos(path:str, todos:list[Todo]):
    data = []
    for todo in todos:
        data.append(todo.to_dict())

    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"ファイル保存中にエラーが発生しました。: {e}")