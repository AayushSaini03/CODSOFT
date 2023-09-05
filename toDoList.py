import tkinter as tk
from tkinter import messagebox

#function to add tasks to the list
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

#funtion to remove tasks from the list
def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

#function to clear tasks from the list
def clear_tasks():
    listbox.delete(0, tk.END)
    save_tasks()

#function to save list in a text file labelled as tasks.txt
def save_tasks():
    with open("tasks.txt", "w") as file: #writes to file and if not found, first creates it
        tasks = listbox.get(0, tk.END)
        file.write("\n".join(tasks))

#function to read tasks.txt file upon opening the to-do list application
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
            for task in tasks:
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10,padx=10,side=tk.TOP, fill=tk.BOTH, expand=True)

entry = tk.Entry(frame, font=("Nunito Sans", 12))
entry.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

add_btn = tk.Button(frame, text="Add Task", font=("Nunito Sans", 12), command=add_task)
add_btn.pack(fill=tk.BOTH, expand=True, padx=5, side=tk.LEFT)

listbox = tk.Listbox(root, font=("Nunito Sans", 12), selectmode=tk.SINGLE)
listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

remove_btn = tk.Button(root, text="Remove Task", font=("Nunito Sans", 12), bg="#F71142", command=remove_task)
remove_btn.pack(fill=tk.BOTH, expand=True, padx=10)

clear_btn = tk.Button(root, text="Clear All", font=("Nunito Sans", 12), command=clear_tasks)
clear_btn.pack(fill=tk.BOTH, expand=True, padx=10, pady=(5, 10))

load_tasks()  # Load saved tasks when the application starts

root.mainloop()
