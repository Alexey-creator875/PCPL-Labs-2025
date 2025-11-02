class Department():
    def __init__(self, id, name, tuitionFee, facultyId):
        self.id = id
        self.name = name
        self.tuitionFee = tuitionFee
        self.facultyId = facultyId

class Faculty():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class FacultyDepartment():
    def __init__(self, facultyId, departmentId):
        self.facultyId = facultyId
        self.departmentId = departmentId

    '''
    Вариант В
    1. «Отдел» и «Сотрудник» связаны соотношением один-ко-многим. Выведите
        список всех сотрудников, у которых фамилия начинается с буквы «А», и названия
        их отделов.
    2. «Отдел» и «Сотрудник» связаны соотношением один-ко-многим. Выведите
        список отделов с минимальной зарплатой сотрудников в каждом отделе,
        отсортированный по минимальной зарплате.
    3. «Отдел» и «Сотрудник» связаны соотношением многие-ко-многим. Выведите
        список всех связанных сотрудников и отделов, отсортированный по сотрудникам,
        сортировка по отделам произвольная.
    '''

    '''
    Вариант В
    1. «Факультет» и «Кафедра» связаны соотношением один-ко-многим. Выведите
        список всех кафедр, у которых название начинается с буквы «И», и названия
        их факультетов.
    2. «Факультет» и «Кафедра» связаны соотношением один-ко-многим. Выведите
        список факультетов с минимальной платой за обучение на кафедре в каждом факультете,
        отсортированный по минимальной плате.
    3. «Факультет» и «Кафедра» связаны соотношением многие-ко-многим. Выведите
        список всех связанных кафедр и факультетов, отсортированный по кафедрам,
        сортировка по факультетам произвольная.
    '''

def JoinFacultyToDepartmentIfOneToManyRelationship(departments, faculties):
    one_to_many = [
        (department.name, department.tuitionFee, faculty.name)
        for faculty in faculties
        for department in departments
        if department.facultyId == faculty.id
    ]

    return one_to_many

def JoinFacultyToDepartmentIfManyToManyRelationship(departments, faculties, facultyDepartments):
    many_to_many_temp = [
        (faculty.name, facultyDepartment.facultyId, facultyDepartment.departmentId)
        for faculty in faculties
        for facultyDepartment in facultyDepartments
        if facultyDepartment.facultyId == faculty.id
    ]

    many_to_many = [
        (department.name, department.tuitionFee, facultyName)
        for facultyName, _, departmentId in many_to_many_temp
        for department in departments
        if department.id == departmentId
    ]

    return many_to_many

def PrintTaskNumber(number):
    print(f'\nЗадание {number}')

def PerformFirstRequest(one_to_many):
    PrintTaskNumber('B1')
    resB1 = list(filter(lambda row: row[0].startswith('И'), one_to_many))
    print(*resB1, sep='\n')

def PerformSecondTask(faculties, one_to_many):
    PrintTaskNumber('B2')

    resA2Unsorted = []

    for faculty in faculties:
        facultyDepartments = list(filter(lambda row: row[2] == faculty.name, one_to_many))
        if facultyDepartments:
            facultyTuitionFees = [row[1] for row in facultyDepartments]
            resA2Unsorted.append((faculty.name, min(facultyTuitionFees)))

    resB2 = sorted(resA2Unsorted, key=lambda row : row[1])
    print(*resB2, sep='\n')

def PerformThirdTask(many_to_many):
    PrintTaskNumber('B3')
    resA3 = sorted(many_to_many, key=lambda row : row[0])
    print(*resA3, sep='\n')

def main():
    faculties = [
        Faculty(1, 'Информатика и системы управления'),
        Faculty(2, 'Специальное машиностроение'),
        Faculty(3, 'Инженерный бизнес и менеджмент'),

        Faculty(11, 'ИУ'),
        Faculty(12, 'СМ'),
        Faculty(13, 'ИБМ'),
    ]

    departments = [
        Department(1, 'ИУ5', 449000, 1),
        Department(2, 'СМ12', 539000, 2),
        Department(3, 'ИУ7', 549000, 1),
        Department(4, 'ИБМ3', 439000, 3),
        Department(5, 'СМ7', 459000, 2)
    ]

    facultyDepartments = [
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

    one_to_many = JoinFacultyToDepartmentIfOneToManyRelationship(departments, faculties)
    many_to_many = JoinFacultyToDepartmentIfManyToManyRelationship(departments, faculties, facultyDepartments)

    PerformFirstRequest(one_to_many)
    PerformSecondTask(faculties, one_to_many)
    PerformThirdTask(many_to_many)

if __name__ == "__main__":
    main()
