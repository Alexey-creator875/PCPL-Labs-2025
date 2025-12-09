import unittest
from unittest.mock import patch

from datetime import datetime

from Tasks.TaskFactory import TaskFactory
from Tasks.Tasks import TaskType
from Tasks.CompositeTask import CompositeTask


class TestCompositeTask(unittest.TestCase):
    def setUp(self):
        self.factory = TaskFactory()
    
    def test_add_component(self):
        tasks_type = TaskType.SIMPLE
        simple_tasks = CompositeTask('Simple Tasks')

        cook_soup_task = self.factory.create_task(tasks_type, 'Cook soup')
        cut_vegetables_task = self.factory.create_task(tasks_type, 'Cut vegetables')
        fry_meat_task = self.factory.create_task(tasks_type, 'Fry meat')

        simple_tasks.add_component(cook_soup_task)
        simple_tasks.add_component(cut_vegetables_task)
        simple_tasks.add_component(fry_meat_task)

        correct_components = [
            cook_soup_task,
            cut_vegetables_task,
            fry_meat_task
        ]

        for i in range(len(simple_tasks.components)):
            component = simple_tasks.components[i]
            correct_component = correct_components[i]

            self.assertEqual(component.description, correct_component.description)

    def test_remove_component(self):
        tasks_type = TaskType.SIMPLE
        simple_tasks = CompositeTask('Simple Tasks')

        cook_soup_task = self.factory.create_task(tasks_type, 'Cook soup')

        simple_tasks.add_component(cook_soup_task)
        simple_tasks.remove_component(cook_soup_task)

        self.assertFalse(simple_tasks.components)

    def test_get_status(self):
        cook_dinner_task = CompositeTask('Cook dinner')

        cook_dinner_task.add_component(self.factory.create_task(TaskType.SIMPLE, 'Cook soup'))
        cook_dinner_task.add_component(self.factory.create_task(TaskType.SIMPLE, 'Cut vegetables'))

        correct_status = {
            'Description': 'Cook dinner',
            'Task type': TaskType.COMPOSITE,
            'Completed': False,
            'Subtasks': [
                {
                    'Description': 'Cook soup',
                    'Task type': TaskType.SIMPLE,
                    'Completed': False,
                },
                {
                    'Description': 'Cut vegetables',
                    'Task type': TaskType.SIMPLE,
                    'Completed': False,
                }
            ]
        }

        self.assertEqual(cook_dinner_task.get_status(), correct_status)

    @patch('Tasks.Tasks.datetime')
    def test_get_status_complex_composite_task(self, mock_datetime):
        fixed_time = datetime(2025, 12, 9, 16, 16, 44)
        mock_datetime.now.return_value = fixed_time
        
        cook_dinner_task = self.factory.create_task(TaskType.COMPOSITE, 'Cook dinner')

        deadline = datetime(2025, 12, 9, 17)
        cook_dinner_task.add_component(self.factory.create_task(TaskType.URGENT, 'Cook soup', deadline))
        cook_dinner_task.add_component(self.factory.create_task(TaskType.SIMPLE, 'Cut vegetables'))

        clean_house_task = self.factory.create_task(TaskType.SIMPLE, 'Clean the house')

        home_task = CompositeTask('Home Tasks')

        home_task.add_component(cook_dinner_task)
        home_task.add_component(clean_house_task)

        correct_status = {
            'Description': 'Home Tasks',
            'Task type': TaskType.COMPOSITE,
            'Completed': False,
            'Subtasks': [
                {
                    'Description': 'Cook dinner',
                    'Task type': TaskType.COMPOSITE,
                    'Completed': False,
                    'Subtasks': [
                        {
                            'Description': 'Cook soup',
                            'Task type': TaskType.URGENT,
                            'Completed': False,
                            'Time left': '0:43:16'
                        },
                        {
                            'Description': 'Cut vegetables',
                            'Task type': TaskType.SIMPLE,
                            'Completed': False,
                        }
                    ]
                },
                {
                    'Description': 'Clean the house',
                    'Task type': TaskType.SIMPLE,
                    'Completed': False,
                }
            ]
        }

        self.assertEqual(home_task.get_status(), correct_status)

    def test_mark_as_completed_composite_task(self):
        cook_dinner_task = self.factory.create_task(TaskType.COMPOSITE, 'Cook dinner')
        cook_dinner_task.add_component(self.factory.create_task(TaskType.SIMPLE, 'Cook soup'))
        cook_dinner_task.add_component(self.factory.create_task(TaskType.SIMPLE, 'Cut vegetables'))

        self.assertFalse(cook_dinner_task.completed)

        for component in cook_dinner_task.components:
            self.assertFalse(component.completed)

        cook_dinner_task.mark_as_completed()

        self.assertTrue(cook_dinner_task.completed)

        for component in cook_dinner_task.components:
            self.assertTrue(component.completed)
