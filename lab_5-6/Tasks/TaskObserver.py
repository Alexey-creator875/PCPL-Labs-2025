from abc import ABC, abstractmethod


class TaskObserver(ABC):
    @abstractmethod
    def update_status(self):
        pass
