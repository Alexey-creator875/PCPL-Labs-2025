import unittest

from Tasks.Tasks import SimpleTask

class TestSimpleTask(unittest.TestCase):
    def test_create_task(self):
        task = SimpleTask("Cook dinner")

        self.assertEqual(task.description, "Cook dinner")

    def test_mark_as_completed(self):
        task = SimpleTask("Cook dinner")
        self.assertEqual(task.completed, False)

        task.mark_as_completed()
        self.assertEqual(task.completed, True)

    def test_is_completed(self):
        task = SimpleTask("Cook dinner")
        self.assertEqual(task.is_completed(), False)

        task.mark_as_completed()
        self.assertEqual(task.is_completed(), True)

    def test_get_status(self):
        task = SimpleTask("Cook dinner")
        status = task.get_status()

        correct_status = [
            '\nSimple Task\n',
            'Description: Cook dinner'
        ]

        self.assertEqual(status, correct_status)
