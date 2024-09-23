import json

class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks() 

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        self.save_tasks() 

    def update_task(self, index, title=None, description=None, completed=None):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if title is not None: task.title = title
            if description is not None: task.description = description
            if completed is not None: task.completed = completed
            self.save_tasks() 
        else:
            raise IndexError("Task index out of range")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()  
        else:
            raise IndexError("Task index out of range")

    def list_tasks(self):
        return self.tasks

    def list_grocery(self):
        grocery_tasks = [task for task in self.tasks if 'grocery' in task.title.lower() or 'grocery' in task.description.lower()]
        return grocery_tasks

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks() 
            return True
        return False

    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f)

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [Task(**task) for task in tasks_data]
        except FileNotFoundError:
            self.tasks = []
