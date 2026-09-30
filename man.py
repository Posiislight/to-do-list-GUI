# Import the necessary modules from tkinter
import tkinter as tk
from tkinter import messagebox

from todo_logic import clear_all, is_duplicate

# Create the main application window
root = tk.Tk()
root.title("To-do-list")  # Set the window title
root.geometry("400x300")  # Set the window size

# Function to add a task to the listbox
def add_task():
    task = task_entry.get()  # Get the task from the entry widget
    if task != "":  # Check if the task is not empty
        if is_duplicate(task, task_listbox.get(0, tk.END)):
            messagebox.showwarning("Warning", "Task already exists")  # Show a warning for duplicate tasks
            return
        task_listbox.insert(tk.END, task)  # Insert the task at the end of the listbox
        task_entry.delete(0, tk.END)  # Clear the entry widget
    else:
        messagebox.showwarning("Warning", "Please enter a task")  # Show a warning if the task is empty

# Function to delete the selected task from the listbox
def del_task():
    try:
        task_listbox.delete(task_listbox.curselection()[0])  # Delete the selected task
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task")  # Show a warning if no task is selected

# Function to clear all tasks from the listbox
def clear_tasks():
    if messagebox.askyesno("Confirm", "Clear all tasks?"):
        remaining_tasks = clear_all(task_listbox.get(0, tk.END))
        task_listbox.delete(0, tk.END)
        for task in remaining_tasks:
            task_listbox.insert(tk.END, task)

# Create the entry widget for task input
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=20)  # Add padding on the y-axis

# Create the listbox to display tasks
task_listbox = tk.Listbox(root, width=50)
task_listbox.pack(pady=10)  # Add padding on the y-axis

# Create the button to add tasks
task_addtask = tk.Button(root, text="Add task", command=add_task)
task_addtask.pack(padx=10)  # Add padding on the x-axis

# Create the button to delete tasks
task_deltask = tk.Button(root, text="Delete task", command=del_task)
task_deltask.pack(padx=5)  # Add padding on the x-axis

# Create the button to clear all tasks
task_clearall = tk.Button(root, text="Clear all", command=clear_tasks)
task_clearall.pack(padx=5)  # Add padding on the x-axis

# Run the main application loop
root.mainloop()
