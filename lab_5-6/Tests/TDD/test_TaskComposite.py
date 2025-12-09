import unittest
from unittest.mock import patch

from datetime import datetime

from Tasks.TaskFactory import TaskFactory
from Tasks.Tasks import TaskType
from Tasks.CompositeTask import CompositeTask


class TestTaskComposite(unittest.TestCase):
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
        home_tasks = CompositeTask('Home Tasks')

        home_tasks.add_component(self.factory.create_task(TaskType.SIMPLE, 'Cook soup'))
        home_tasks.add_component(self.factory.create_task(TaskType.SIMPLE, 'Cut vegetables'))

        correct_status = [
            ['Simple Task', 'Description: Cook soup'],
            ['Simple Task', 'Description: Cut vegetables']
        ]

        self.assertEqual(home_tasks.get_status(), correct_status)

    @patch('Tasks.Tasks.datetime')
    def test_get_status_complex_composite_task(self, mock_datetime):
        fixed_time = datetime(2025, 12, 9, 16, 16, 44)
        mock_datetime.now.return_value = fixed_time

        deadline = datetime(2025, 12, 9, 17)
        
        home_task = CompositeTask('Home Tasks')

        cook_dinner_task = self.factory.create_task(TaskType.COMPOSITE, 'Cook dinner')
        cook_dinner_task.add_component(self.factory.create_task(TaskType.URGENT, 'Cook soup', deadline))
        cook_dinner_task.add_component(self.factory.create_task(TaskType.SIMPLE, 'Cut vegetables'))

        clean_house_task = self.factory.create_task(TaskType.SIMPLE, 'Clean the house')

        home_task.add_component(cook_dinner_task)
        home_task.add_component(clean_house_task)

        correct_status = [
            [
                ['Urgent Task', 'Description: Cook soup', 'Time left: 0:43:16'],
                ['Simple Task', 'Description: Cut vegetables']
            ],
            ['Simple Task', 'Description: Clean the house']
        ]

        self.assertEqual(home_task.get_status(), correct_status)

