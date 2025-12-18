class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __eq__(self, other):
        if self._get_average_grade() > 0 and other._get_average_grade() > 0:
            return self._get_average_grade() == other._get_average_grade()
        else:
            return 'Ошибка'

    def __gt__(self, other):
        if self._get_average_grade() > 0 and other._get_average_grade() > 0:
            return self._get_average_grade() > other._get_average_grade()
        else:
            return 'Ошибка'

    def _get_average_grade(self):
        if len(self.grades.values()) > 0:
            count = 0
            tot = 0
            for x in self.grades.values():
                n = sum(x) / len(x)
                count += 1
                tot += n
            return tot / count
        else:
            return 'Нет оценок'

    def _geta_course_st(self, course):
        if course in self.courses_in_progress and len(self.grades[course]) > 0:
            return (f'Средняя оценка студента на курсе {course}: {sum(self.grades[course]) / len(self.grades[course])}')
        elif course in self.courses_in_progress:
            return 'Пока нет оценок'
        else:
            return 'Студент не изучает этот курс'

    def _rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Фамилия: {self.surname} \nИмя: {self.name} \nСредняя оценка за домашние задания: {self._get_average_grade()} '
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}')
                # Сначала идет фамилия т.к. имена китайские

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor, Student):
    def __init__(self, name, surname):
        self.grades = {}
        super().__init__(name, surname)

    def __str__(self):
        return (f'Фамилия: {self.surname} \nИмя: {self.name} \nСредняя оценка за лекции: {self._get_average_grade()}')

    def geta_course_mt(self, course):
        if course in self.courses_attached and len(self.grades[course]) > 0:
            return (f'Средняя оценка преподавателя на {course}: {sum(self.grades[course]) / len(self.grades[course])}')
        elif course in self.courses_attached:
            return 'Пока нет оценок'
        else:
            return 'Не преподает на этом курсе'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return (f'Фамилия: {self.surname} \nИмя: {self.name}')

    def _rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


lecturer_1 = Lecturer('Cao', 'Cao')
lecturer_2 = Lecturer('Liang', 'Zhuge')
reviewer_1 = Reviewer('Yu', 'Guan')
reviewer_2 = Reviewer('Bu', 'Lu')
student_1 = Student('Bei', 'Liu', 'm')
student_2 = Student('Fei', 'Zhang', 'm')

student_1.courses_in_progress += ['Python', 'Git']
student_2.courses_in_progress += ['C++', 'Java']
lecturer_1.courses_attached += ['Python', 'Java']
lecturer_2.courses_attached += ['C++', 'Git']
reviewer_1.courses_attached += ['Python', 'Git', 'Java']
reviewer_2.courses_attached += ['C++', 'Java', 'Git']
student_1.finished_courses += ['Основы программирования']
student_2.finished_courses += ['Основы выживания в дикой природе']


student_1._rate_lecture(lecturer_1, 'Python', 10)
student_1._rate_lecture(lecturer_2, 'Git', 2)
student_2._rate_lecture(lecturer_2, 'C++', 10)
student_2._rate_lecture(lecturer_1, 'Python', 10)
student_2._rate_lecture(lecturer_1, 'Python', 10)
reviewer_1._rate_hw(student_1, 'Python', 9)
reviewer_2._rate_hw(student_1, 'Git', 10)
reviewer_1._rate_hw(student_2, 'Java', 6)
reviewer_2._rate_hw(student_2, 'C++', 1)