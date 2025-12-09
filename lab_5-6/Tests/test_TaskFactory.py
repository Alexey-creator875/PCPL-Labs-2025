import unittest

from datetime import datetime


from Tasks.Tasks import TaskType
from Tasks.TaskFactory import TaskFactory


class TestTaskFactory(unittest.TestCase):
    def setUp(self):
        self.factory = TaskFactory()

    def test_create_simple_task(self):
        simple_task = self.factory.create_task(TaskType.SIMPLE, 'Cook dinner')

        self.assertEqual(simple_task.description, 'Cook dinner')
        self.assertFalse(simple_task.completed)

    def test_create_urgent_task(self):
        simple_task = self.factory.create_task(TaskType.URGENT, 'Do homework', datetime(2025, 12, 9, 16))

        self.assertEqual(simple_task.description, 'Do homework')
        self.assertFalse(simple_task.completed)
        self.assertEqual(simple_task.deadline, datetime(2025, 12, 9, 16))

    def test_raise_exception_when_create_task_(self):
        with self.assertRaises(ValueError):
            task = self.factory.create_task(1, 'Cook dinner')

