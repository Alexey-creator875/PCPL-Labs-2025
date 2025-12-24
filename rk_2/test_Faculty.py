import unittest

from Faculty import *


class TestFirstRequest(unittest.TestCase):
    def setUp(self):
        self.faculties = [
            Faculty(1, 'Информатика и системы управления'),
            Faculty(2, 'Специальное машиностроение'),
            Faculty(3, 'Инженерный бизнес и менеджмент'),

            Faculty(11, '(Другие) Информатика и системы управления'),
            Faculty(12, '(Другое) Специальное машиностроение'),
            Faculty(13, '(Другой) Инженерный бизнес и менеджмент'),
        ]

        self.departments = [
            Department(1, 'ИУ5', 449000, 1),
            Department(2, 'СМ12', 539000, 2),
            Department(3, 'ИУ7', 549000, 1),
            Department(4, 'ИБМ3', 439000, 3),
            Department(5, 'СМ7', 459000, 2)
        ]

        self.facultyDepartments = [
            FacultyDepartment(1, 1),
            FacultyDepartment(2, 2),
            FacultyDepartment(1, 3),
            FacultyDepartment(3, 4),
            FacultyDepartment(2, 5),

            FacultyDepartment(11, 1),
            FacultyDepartment(12, 2),
            FacultyDepartment(11, 3),
            FacultyDepartment(13, 4),
            FacultyDepartment(12, 5)
        ]

        self.one_to_many = JoinFacultyToDepartmentIfOneToManyRelationship(self.departments, self.faculties)
        self.many_to_many = JoinFacultyToDepartmentIfManyToManyRelationship(self.departments, self.faculties, self.facultyDepartments)
    
    def test_FirstRequest(self):
        result = PerformFirstRequest(self.one_to_many)

        correct_result = [
            ('ИУ5', 449000, 'Информатика и системы управления'),
            ('ИУ7', 549000, 'Информатика и системы управления'),
            ('ИБМ3', 439000, 'Инженерный бизнес и менеджмент')
        ]

        self.assertEqual(result, correct_result)

    def test_SecondRequest(self):
        result = PerformSecondTask(self.faculties, self.one_to_many)

        correct_result = [
            ('Инженерный бизнес и менеджмент', 439000),
            ('Информатика и системы управления', 449000),
            ('Специальное машиностроение', 459000)
        ]

        self.assertEqual(result, correct_result)

    def test_ThirdRequest(self):
        result = PerformThirdTask(self.many_to_many)

        correct_result = [
            ('ИБМ3', 439000, 'Инженерный бизнес и менеджмент'),
            ('ИБМ3', 439000, '(Другой) Инженерный бизнес и менеджмент'),
            ('ИУ5', 449000, 'Информатика и системы управления'),
            ('ИУ5', 449000, '(Другие) Информатика и системы управления'),
            ('ИУ7', 549000, 'Информатика и системы управления'),
            ('ИУ7', 549000, '(Другие) Информатика и системы управления'),
            ('СМ12', 539000, 'Специальное машиностроение'),
            ('СМ12', 539000, '(Другое) Специальное машиностроение'),
            ('СМ7', 459000, 'Специальное машиностроение'),
            ('СМ7', 459000, '(Другое) Специальное машиностроение')
        ]

        self.assertEqual(result, correct_result)


if __name__ == "__main__":
    unittest.main()
