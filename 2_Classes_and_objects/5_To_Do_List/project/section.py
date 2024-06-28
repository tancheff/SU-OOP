from typing import List
from task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks: List[object] = []

    def add_task(self, new_task: Task) -> str:
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str) -> str:
        if task_name in self.tasks:
            task_name.completed = True
            return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        completed_tasks_counter = 0
        for task in self.tasks:
            if task.completed == True:
                completed_tasks_counter += 1
                self.tasks.remove(task)
        return f"Cleared {completed_tasks_counter} tasks."

    def view_section(self) -> str:
        all_task_details = "\n".join([t.details() for t in self.tasks])
        return (f"Section {self.name}:\n"
                f"{all_task_details}")
