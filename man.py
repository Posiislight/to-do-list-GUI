# Import the necessary modules from tkinter
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

from todo_store import load_tasks, save_tasks

TASKS_PATH = Path(__file__).with_name("tasks.json")

# Create the main application window
root = tk.Tk()
root.title("To-do-list")  # Set the window title
root.geometry("400x300")  # Set the window size


def current_tasks():
    return list(task_listbox.get(0, tk.END))


def save_current_tasks():
    save_tasks(TASKS_PATH, current_tasks())


# Function to add a task to the listbox
def add_task():
    task = task_entry.get()  # Get the task from the entry widget
    if task != "":  # Check if the task is not empty
        task_listbox.insert(tk.END, task)  # Insert the task at the end of the listbox
        task_entry.delete(0, tk.END)  # Clear the entry widget
        save_current_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task")  # Show a warning if the task is empty

# Function to delete the selected task from the listbox
def del_task():
    try:
        task_listbox.delete(task_listbox.curselection()[0])  # Delete the selected task
        save_current_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task")  # Show a warning if no task is selected

# Create the entry widget for task input
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=20)  # Add padding on the y-axis

# Create the listbox to display tasks
task_listbox = tk.Listbox(root, width=50)
task_listbox.pack(pady=10)  # Add padding on the y-axis
for task in load_tasks(TASKS_PATH):
    task_listbox.insert(tk.END, task)

# Create the button to add tasks
task_addtask = tk.Button(root, text="Add task", command=add_task)
task_addtask.pack(padx=10)  # Add padding on the x-axis

# Create the button to delete tasks
task_deltask = tk.Button(root, text="Delete task", command=del_task)
task_deltask.pack(padx=5)  # Add padding on the x-axis

# Run the main application loop
root.mainloop()