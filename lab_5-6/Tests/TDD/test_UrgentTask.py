import unittest
from unittest.mock import patch

from datetime import datetime

from Tasks.Tasks import UrgentTask, TaskType


class TestUrgentTask(unittest.TestCase):
    def test_create_task(self):
        task = UrgentTask('Do homework', datetime(2025, 12, 9, 16))

        self.assertEqual(task.description, 'Do homework')
        self.assertFalse(task.completed)
        self.assertEqual(task.deadline, datetime(2025, 12, 9, 16))

    def test_create_task_deadline_with_microsecs(self):
        task = UrgentTask('Do homework', datetime(2025, 12, 9, 16, 0, 0, 200))

        self.assertEqual(task.deadline, datetime(2025, 12, 9, 16))

    @patch('Tasks.Tasks.datetime')
    def test_get_status(self, mock_datetime):
        fixed_time = datetime(2025, 12, 9, 16, 16, 44)
        mock_datetime.now.return_value = fixed_time

        deadline = datetime(2025, 12, 9, 17)
        task = UrgentTask('Do homework', deadline)
        status = task.get_status()

        correct_status = {
            'Description': 'Do homework',
            'Task type': TaskType.URGENT,
            'Completed': False,
            'Time left': '0:43:16'
        }

        self.assertEqual(status, correct_status)


    @patch('Tasks.Tasks.datetime')
    def test_get_status_deadline_more_than_month(self, mock_datetime):
        fixed_time = datetime(2025, 11, 9, 16, 16, 44)
        mock_datetime.now.return_value = fixed_time

        deadline = datetime(2025, 12, 15, 16)
        task = UrgentTask('Do homework', deadline)
        status = task.get_status()

        correct_status = {
            'Description': 'Do homework',
            'Task type': TaskType.URGENT,
            'Completed': False,
            'Time left': '35 days, 23:43:16'
        }

        self.assertEqual(status, correct_status)

    def test_get_status_expired_task(self):
        deadline = datetime(2020, 12, 9)
        task = UrgentTask('Do homework', deadline)
        status = task.get_status()

        correct_status = {
            'Description': 'Do homework',
            'Task type': TaskType.URGENT,
            'Completed': False,
            'Time left': 'expired'
        }

        self.assertEqual(status, correct_status)

    @patch('Tasks.Tasks.datetime')
    def test_get_status_expired_just_now_task(self, mock_datetime):
        fixed_time = datetime(2025, 12, 9, 16, 16, 44, 200)
        mock_datetime.now.return_value = fixed_time

        deadline = datetime(2025, 12, 9, 16, 16, 44)
        task = UrgentTask('Do homework', deadline)
        status = task.get_status()

        correct_status = {
            'Description': 'Do homework',
            'Task type': TaskType.URGENT,
            'Completed': False,
            'Time left': 'expired'
        }

        self.assertEqual(status, correct_status)