from abc import ABC, abstractmethod
from enum import Enum

from datetime import datetime


class TaskType(Enum):
    URGENT = 0
    RECURRING = 1
    SIMPLE = 2


class Task(ABC):
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True
    
    def is_completed(self):
        return self.completed

    @abstractmethod
    def get_status(self):
        pass

    # @abstractmethod
    # def get_priority(self):
    #     pass



class SimpleTask(Task):
    def __init__(self, description):
        super().__init__(description)

    def get_status(self):
        return [
            '\nSimple Task\n',
            f'Description: {self.description}'
        ]

    # def get_priority(self):
    #     return int(TaskType.SIMPLE)


class UrgentTask(Task):
    def __init__(self, description, deadline):
        super().__init__(description)
        self.deadline = deadline
        self.deadline = deadline.replace(microsecond=0)

    def get_status(self):
        time_left = self.deadline - datetime.now().replace(microsecond=0)

        return [
            '\nUrgent Task\n',
            f'Description: {self.description}'
            f'Time left: {time_left}'
        ]

    # def get_priority(self):
    #     return int(TaskType.URGENT)

# class RecurringTask(Task):
#     def __init__(self, status, name, task, period):
#         super().__init__(status, name, task)
#         self.period = period

#     def get_priority(self):
#         return int(TaskType.RECURRING)


# class TaskFactory:
#     def create_task(self, task_type, *args, **kwargs):
#         if task_type == TaskType.URGENT:
#             return UrgentTask(*args, **kwargs)
#         elif task_type == TaskType.RECURRING:
#             return RecurringTask(*args, **kwargs)
#         elif task_type == TaskType.SIMPLE:
#             return SimpleTask(*args, **kwargs)
#         else:
#             raise ValueError(f'Unknown task type: {task_type}')
