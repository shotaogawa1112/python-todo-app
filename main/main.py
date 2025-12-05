from todo_storage import load_todos, save_todos
from todo_models import Todo

FILE_PATH = "storage.json"

def show_menu():
    print("\n===== ToDo アプリ =====")
    print("1. タスク一覧表示")
    print("2. タスク追加")
    print("3. タスク完了/未完了 切り替え")
    print("4. タスク削除")
    print("5. 終了")

def show_todos(todos):
    print("\n--- タスク一覧 ---")
    if not todos:
        print("タスクがありません")
        return
    for todo in todos:
        status = "✔" if todo.done else "✖"
        print(f"{todo.id}. {todo.title} [{status}]")

def add_todo(todos):
    title = input("追加するタスク名を入力： ")
    if not title.strip():
        print("空白のみの入力は不可です。")
        return
    new_id = max([t.id for t in todos], default=0) + 1
    todo = Todo(new_id, title, False)
    todos.append(todo)
    print(f"タスク '{title}' を追加しました！")

def toggle_todo(todos):
    try:
        task_id = int(input("完了状態を切り替えるタスクIDを入力： "))
        for todo in todos:
            if todo.id == task_id:
                todo.done = not todo.done
                print(f"タスク {todo.id} の状態を変更しました！")
                return
        print("指定されたIDのタスクがありません。")
    except ValueError:
        print("整数値を入力してください。")

def delete_todo(todos):
    try:
        task_id = int(input("削除するタスクIDを入力： "))
        for todo in todos:
            if todo.id == task_id:
                todos.remove(todo)
                print(f"タスク {task_id} を削除しました！")
                return
        print("指定されたIDのタスクがありません。")
    except ValueError:
        print("整数値を入力してください。")

def main():
    todos = load_todos(FILE_PATH)

    while True:
        show_menu()
        choice = input("番号を選択してください： ")

        if choice == "1":
            show_todos(todos)

        elif choice == "2":
            add_todo(todos)
            save_todos(FILE_PATH, todos)

        elif choice == "3":
            toggle_todo(todos)
            save_todos(FILE_PATH, todos)

        elif choice == "4":
            delete_todo(todos)
            save_todos(FILE_PATH, todos)

        elif choice == "5":
            print("終了します。")
            break

        else:
            print("正しい番号を入力してください。")


if __name__ == "__main__":
    main()
