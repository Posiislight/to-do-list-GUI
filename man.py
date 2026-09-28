from dataclasses import dataclass, field
from typing import Sequence


EMPTY_TASK_WARNING = "Please enter a task"
NO_SELECTION_WARNING = "Please select a task"


@dataclass
class TaskStore:
    tasks: list[str] = field(default_factory=list)

    def add(self, task: str) -> bool:
        if task == "":
            return False

        self.tasks.append(task)
        return True

    def delete_selection(self, selection: Sequence[int]) -> int | None:
        if not selection:
            return None

        index = selection[0]
        if index < 0 or index >= len(self.tasks):
            return None

        del self.tasks[index]
        return index


class TodoApp:
    def __init__(self, root, tk_module, messagebox_module):
        self.root = root
        self.tk = tk_module
        self.messagebox = messagebox_module
        self.store = TaskStore()

        root.title("To-do-list")
        root.geometry("400x300")

        self.task_entry = tk_module.Entry(root, width=50)
        self.task_entry.pack(pady=20)

        self.task_listbox = tk_module.Listbox(root, width=50)
        self.task_listbox.pack(pady=10)

        self.task_addtask = tk_module.Button(root, text="Add task", command=self.add_task)
        self.task_addtask.pack(padx=10)

        self.task_deltask = tk_module.Button(root, text="Delete task", command=self.del_task)
        self.task_deltask.pack(padx=5)

    def add_task(self) -> None:
        task = self.task_entry.get()
        if self.store.add(task):
            self.task_listbox.insert(self.tk.END, task)
            self.task_entry.delete(0, self.tk.END)
            return

        self.messagebox.showwarning("Warning", EMPTY_TASK_WARNING)

    def del_task(self) -> None:
        deleted_index = self.store.delete_selection(self.task_listbox.curselection())
        if deleted_index is None:
            self.messagebox.showwarning("Warning", NO_SELECTION_WARNING)
            return

        self.task_listbox.delete(deleted_index)


def main() -> None:
    import tkinter as tk
    from tkinter import messagebox

    root = tk.Tk()
    TodoApp(root, tk, messagebox)
    root.mainloop()


if __name__ == "__main__":
    main()
