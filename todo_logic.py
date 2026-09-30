def is_duplicate(task, tasks):
    normalized_task = task.strip().casefold()
    return any(normalized_task == existing_task.strip().casefold() for existing_task in tasks)


def clear_all(tasks):
    return []
