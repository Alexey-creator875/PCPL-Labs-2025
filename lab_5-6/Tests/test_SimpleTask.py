import unittest

from Tasks.Tasks import SimpleTask

class TestSimpleTask(unittest.TestCase):
    def test_create_task(self):
        task = SimpleTask('Cook dinner')

        self.assertEqual(task.description, 'Cook dinner')
        self.assertFalse(task.completed)

    def test_mark_as_completed(self):
        task = SimpleTask('Cook dinner')

        task.mark_as_completed()
        self.assertTrue(task.completed)

    def test_is_completed(self):
        task = SimpleTask('Cook dinner')
        self.assertFalse(task.is_completed())

        task.mark_as_completed()
        self.assertTrue(task.is_completed())

    def test_get_status(self):
        task = SimpleTask('Cook dinner')
        status = task.get_status()

        correct_status = [
            '\nSimple Task\n',
            'Description: Cook dinner'
        ]

        self.assertEqual(status, correct_status)
