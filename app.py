import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Select a task to delete")

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    messagebox.showinfo("Success", "Tasks saved successfully!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

# GUI Setup
app = tk.Tk()
app.title("To-Do List App")
app.geometry("400x400")

frame = tk.Frame(app)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=40, height=10)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(app, width=30)
entry.pack(pady=5)

btn_add = tk.Button(app, text="Add Task", command=add_task)
btn_add.pack(pady=5)

btn_delete = tk.Button(app, text="Delete Task", command=delete_task)
btn_delete.pack(pady=5)

btn_save = tk.Button(app, text="Save Tasks", command=save_tasks)
btn_save.pack(pady=5)

btn_load = tk.Button(app, text="Load Tasks", command=load_tasks)
btn_load.pack(pady=5)

load_tasks()
app.mainloop()

