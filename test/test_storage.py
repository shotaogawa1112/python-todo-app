import os
import json
import unittest

from main.todo_models import Todo
from main.todo_storage import load_todos, save_todos


class TestTodoStorage(unittest.TestCase):

    def setUp(self):
        """テスト用の一時ファイルを作成"""
        self.test_file = "test_storage.json"

        # テスト用の JSON データ
        initial_data = [
            {"id": 1, "title": "散歩する", "done": False},
            {"id": 2, "title": "メール返信", "done": True},
        ]

        # ファイルに書き込み
        with open(self.test_file, "w", encoding="utf-8") as f:
            json.dump(initial_data, f, ensure_ascii=False, indent=2)

    def tearDown(self):
        """テスト後は一時ファイルを削除"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    # --------------------------
    # Todo クラス to_dict のテスト
    # --------------------------
    def test_todo_to_dict(self):
        todo = Todo(1, "散歩", False)
        expected = {"id": 1, "title": "散歩", "done": False}
        self.assertEqual(todo.to_dict(), expected)

    # --------------------------
    # load_todos のテスト
    # --------------------------
    def test_load_todos(self):
        todos = load_todos(self.test_file)

        self.assertEqual(len(todos), 2)
        self.assertEqual(todos[0].id, 1)
        self.assertEqual(todos[0].title, "散歩する")
        self.assertEqual(todos[0].done, False)

        self.assertEqual(todos[1].id, 2)
        self.assertEqual(todos[1].title, "メール返信")
        self.assertEqual(todos[1].done, True)

    # --------------------------
    # save_todos のテスト
    # --------------------------
    def test_save_todos(self):
        todos = [
            Todo(10, "勉強", True),
            Todo(20, "買い物", False),
        ]

        # 保存テスト
        save_todos(self.test_file, todos)

        # 書き込まれた内容をチェック
        with open(self.test_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["id"], 10)
        self.assertEqual(data[0]["title"], "勉強")
        self.assertEqual(data[0]["done"], True)

        self.assertEqual(data[1]["id"], 20)
        self.assertEqual(data[1]["title"], "買い物")
        self.assertEqual(data[1]["done"], False)


if __name__ == "__main__":
    unittest.main()
