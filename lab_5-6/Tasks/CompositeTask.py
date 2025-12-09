from Tasks.Tasks import Task


class CompositeTask(Task):
    def __init__(self, description):
        super().__init__(description)
        self.components = []
    
    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def get_status(self):
        return [component.get_status() for component in self.components]
