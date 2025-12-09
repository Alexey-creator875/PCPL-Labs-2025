import unittest
from ToDoList import SimpleTask

# from ToDoList import TaskFactory, TaskType

class TestSimpleTask(unittest.TestCase):
    def test_create_task(self):
        task = SimpleTask("Cook dinner")

        self.assertEqual(task.description, "Cook dinner")




# class TestTaskFactory(unittest.TestCase):
#     def test_create_task(self):
#         factory = TaskFactory()

#         task = factory.create_task(TaskType.SIMPLE, "processing", "homework", "do homework")

#         self.assertEqual(task.name, "homework")
    
