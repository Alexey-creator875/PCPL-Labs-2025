from Tasks.Tasks import Task, TaskType
from Tasks.TaskObserver import TaskObserver

class CompositeTask(Task, TaskObserver):
    def __init__(self, description):
        super().__init__(description)
        self.components = []
    
    def add_component(self, component):
        if component not in self.components:
            self.components.append(component)
            component.add_observer(self)

    def remove_component(self, component):
        if component in self.components:
            self.components.remove(component)
            component.remove_observer(self)

    def mark_as_completed(self):
        super().mark_as_completed()
        for component in self.components:
            component.mark_as_completed()

    def update_status(self):
        if self.is_completed():
            return

        if all(component.is_completed() for component in self.components):
            self.mark_as_completed()

    def get_status(self):
        subtasks = [component.get_status() for component in self.components]

        status = {
            'Description': self.description,
            'Task type': TaskType.COMPOSITE,
            'Completed': self.completed,
            'Subtasks': subtasks
        }

        return status
