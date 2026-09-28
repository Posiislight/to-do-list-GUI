import json


def load_tasks(path) -> list[str]:
    try:
        with open(path, "r", encoding="utf-8") as tasks_file:
            tasks = json.load(tasks_file)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return []

    if not isinstance(tasks, list) or not all(isinstance(task, str) for task in tasks):
        return []

    return tasks


def save_tasks(path, tasks):
    with open(path, "w", encoding="utf-8") as tasks_file:
        json.dump(list(tasks), tasks_file)
