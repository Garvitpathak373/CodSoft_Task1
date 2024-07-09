import tkinter as tk
from tkinter import messagebox

class Task:
     def __init__(self, description):
          self.description = description
         self.completed = False

     def mark_as_completed(self):
         self.completed = True

     def __str__(self):
         status = "Completed" if self.completed else "Pending"
         return f"{self.description} ({status})"


 class ToDoList:
     def __init__(self):
         self.tasks = []

     def add_task(self, description):
         new_task = Task(description)
         self.tasks.append(new_task)

     def remove_task(self, task_number):
         try:
             del self.tasks[task_number - 1]
         except IndexError:
             pass

     def mark_task_as_completed(self, task_number):
         try:
             self.tasks[task_number - 1].mark_as_completed()
         except IndexError:
             pass

     def get_tasks(self):
         return [str(task) for task in self.tasks]


 class ToDoListApp:
     def __init__(self, root):
         self.root = root
         self.to_do_list = ToDoList()

         self.task_entry_label = tk.Label(root, text="Enter task description:")
         self.task_entry_label.pack()

         self.task_entry = tk.Entry(root, width=40)
         self.task_entry.pack()

         self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
         self.add_task_button.pack()

         self.task_list_label = tk.Label(root, text="To-Do List:")
         self.task_list_label.pack()

         self.task_list = tk.Listbox(root, width=40, height=10)
         self.task_list.pack()

         self.remove_task_button = tk.Button(root, text="Remove Task", command=self.remove_task)
         self.remove_task_button.pack()

         self.mark_as_completed_button = tk.Button(root, text="Mark as Completed", command=self.mark_task_as_completed)
         self.mark_as_completed_button.pack()

         self.update_task_list()
     root.mainloop()