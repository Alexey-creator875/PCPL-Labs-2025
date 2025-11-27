import unittest
from ToDoList import TaskFactory, TaskType


class TestTaskFactory(unittest.TestCase):
    def test_create_task(self):
        factory = TaskFactory()

        task = factory.create_task(TaskType.SIMPLE, "processing", "homework", "do homework")

        self.assertEqual(task.name, "homework")
    
