from todo_store import load_tasks, save_tasks


def test_save_and_load_round_trip(tmp_path):
    path = tmp_path / "tasks.json"
    tasks = ["buy milk", "write tests"]

    save_tasks(path, tasks)

    assert load_tasks(path) == tasks


def test_load_missing_file_returns_empty_list(tmp_path):
    assert load_tasks(tmp_path / "missing.json") == []


def test_load_corrupt_file_returns_empty_list(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text("{not valid json", encoding="utf-8")

    assert load_tasks(path) == []
