from Tasks.Tasks import TaskType, SimpleTask, UrgentTask
from Tasks.CompositeTask import CompositeTask


class TaskFactory:
    def create_task(self, task_type, *args, **kwargs):
        if task_type == TaskType.URGENT:
            return UrgentTask(*args, **kwargs)
        elif task_type == TaskType.SIMPLE:
            return SimpleTask(*args, **kwargs)
        elif task_type == TaskType.COMPOSITE:
            return CompositeTask(*args, **kwargs)
        else:
            raise ValueError(f'Unknown task type: {task_type}')
