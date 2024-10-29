import tkinter as tk
from tkinter import messagebox

from PIL.ImageOps import expand


class TodoApp:
    def __init__(self, root):
        self.task_entry = None
        self.delete_task_button = None
        self.add_task_button = None
        self.tasks_listbox = None
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []
        self.create_widgets()
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

    def create_widgets(self):
        self.task_entry = tk.Entry(self.root, width=90)
        self.task_entry.pack(pady=20)
        self.task_entry.pack(padx=40)
        self.task_entry.pack(expand=True)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=20)
        self.add_task_button.pack(expand=True)

        self.tasks_listbox = tk.Listbox(self.root, width=90, height=10)
        self.tasks_listbox.pack(pady=20)
        self.tasks_listbox.pack(expand=True)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=20)
        self.delete_task_button.pack(expand=True)
    

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


