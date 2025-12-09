import unittest

from Tasks.TaskFactory import TaskFactory
from Tasks.Tasks import TaskType
from Tasks.TaskComposite import TaskComposite


class TestTaskComposite(unittest.TestCase):
    def setUp(self):
        self.factory = TaskFactory()
    
    def test_add_component(self):
        tasks_type = TaskType.SIMPLE
        simple_tasks = TaskComposite('Simple Tasks')

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
        simple_tasks = TaskComposite('Simple Tasks')

        cook_soup_task = self.factory.create_task(tasks_type, 'Cook soup')

        simple_tasks.add_component(cook_soup_task)
        simple_tasks.remove_component(cook_soup_task)

        self.assertFalse(simple_tasks.components)

    def test_get_status(self):
        home_tasks = TaskComposite('Home Tasks')

        home_tasks.add_component(self.factory.create_task(TaskType.SIMPLE, 'Cook soup'))
        home_tasks.add_component(self.factory.create_task(TaskType.SIMPLE, 'Cut vegetables'))

        correct_status = [
            ['Simple Task', 'Description: Cook soup'],
            ['Simple Task', 'Description: Cut vegetables']
        ]

        self.assertEqual(home_tasks.get_status(), correct_status)

