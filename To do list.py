import tkinter as tk
from tkinter import messagebox

tasks = []

# Add Task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

# Remove Task
def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
        tasks.pop(selected_task_index[0])
    else:
        messagebox.showwarning("Warning", "Select a task to remove!")

# Create the GUI Window
app = tk.Tk()
app.title("To-Do List")

# Task Entry Field
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=10)

# Add Button
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack()

# Task List Box
task_listbox = tk.Listbox(app, width=50)
task_listbox.pack()

# Remove Button
remove_button = tk.Button(app, text="Remove Task", command=remove_task)
remove_button.pack()

# Run the Application
app.mainloop()
