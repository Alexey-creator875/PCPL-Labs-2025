from abc import ABC, abstractmethod
from enum import Enum

from datetime import datetime


class TaskType(Enum):
    URGENT = 0
    SIMPLE = 1
    COMPOSITE = 2


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


class SimpleTask(Task):
    def __init__(self, description):
        super().__init__(description)

    def get_status(self):
        return [
            'Simple Task',
            f'Description: {self.description}'
        ]


class UrgentTask(Task):
    def __init__(self, description, deadline):
        super().__init__(description)
        self.deadline = deadline
        self.deadline = deadline.replace(microsecond=0)

    def get_status(self):
        time_left = self.deadline - datetime.now().replace(microsecond=0)

        return [
            'Urgent Task',
            f'Description: {self.description}',
            f'Time left: {time_left}'
        ]
