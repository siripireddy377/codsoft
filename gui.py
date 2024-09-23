import tkinter as tk
from tkinter import messagebox
from tasks import TaskManager

# Update the task list in the Listbox
def update_task_list():
    task_list.delete(0, tk.END)
    for i, task in enumerate(manager.list_tasks()):
        status = "✓" if task.completed else "✗"
        task_list.insert(tk.END, f"{i}. {task.title} - {task.description} [{status}]")

# Add a new task
def add_task():
    title = title_entry.get()
    description = desc_entry.get()

    if not title or not description:
        messagebox.showwarning("Input Error", "Please enter both a title and description.")
        return

    manager.add_task(title, description)
    update_task_list()
    title_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)

# Delete a selected task
def delete_task():
    selected = task_list.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")
        return
    task_index = selected[0]
    manager.delete_task(task_index)
    update_task_list()

# Mark a selected task as completed
def toggle_complete_task():
    selected = task_list.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")
        return
    task_index = selected[0]
    manager.toggle_task_completed(task_index)
    update_task_list()

# Edit a selected task
def edit_task():
    selected = task_list.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")
        return
    task_index = selected[0]
    task = manager.list_tasks()[task_index]
    
    # Create a new window for editing
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Task")

    tk.Label(edit_window, text="Task Title:").pack()
    edit_title_entry = tk.Entry(edit_window)
    edit_title_entry.pack()
    edit_title_entry.insert(0, task.title)

    tk.Label(edit_window, text="Task Description:").pack()
    edit_desc_entry = tk.Entry(edit_window)
    edit_desc_entry.pack()
    edit_desc_entry.insert(0, task.description)

    # Save changes to the task
    def save_changes():
        new_title = edit_title_entry.get()
        new_description = edit_desc_entry.get()
        
        if not new_title or not new_description:
            messagebox.showwarning("Input Error", "Please enter both a title and description.")
            return

        manager.update_task(task_index, new_title, new_description)
        edit_window.destroy()
        update_task_list()

    save_button = tk.Button(edit_window, text="Save Changes", command=save_changes)
    save_button.pack()

# Initialize Task Manager
manager = TaskManager()

# Main Window
root = tk.Tk()
root.title("Advanced To-Do List")

# Input Fields for Adding Tasks
tk.Label(root, text="Task Title:").pack()
title_entry = tk.Entry(root)
title_entry.pack()

tk.Label(root, text="Task Description:").pack()
desc_entry = tk.Entry(root)
desc_entry.pack()

# Task Action Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack()

complete_button = tk.Button(root, text="Mark Task as Completed", command=toggle_complete_task)
complete_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

# Listbox to Display Tasks
task_list = tk.Listbox(root, selectmode=tk.SINGLE)
task_list.pack(fill=tk.BOTH, expand=True)

# Initial Task List Update
update_task_list()

# Start the Tkinter event loop
root.mainloop()
