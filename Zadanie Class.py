class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades_len = 0
        finished_courses_str = ', '.join(self.finished_courses)
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        for x in self.grades:
            grades_len += len(self.grades[x])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_len
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
                f'Курсы в процессе изучения: {courses_in_progress_str}\n' \
                f'Завершенные курсы: {finished_courses_str}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Некорректное сравнение')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        grades_len = 0
        for x in self.grades:
            grades_len += len(self.grades[x])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_len
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Некорректное сравнение')
            return
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res



cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['GIT']

cool_reviewer_2 = Reviewer('Adam', 'Smith')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['GIT']

print('Проверяющие:')
print(cool_reviewer_1)
print()
print(cool_reviewer_2)
print()
print()

student_1 = Student('Roy', 'Eman')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Ivan', 'Gorbach')
student_2.courses_in_progress += ['GIT']
student_2.finished_courses += ['Введение в программирование']


lecturer_1 = Lecturer('Edward', 'Emilf')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Sim', 'Verdish')
lecturer_2.courses_attached += ['GIT']

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 9)

student_2.rate_lecturer(lecturer_2, 'GIT', 10)
student_2.rate_lecturer(lecturer_2, 'GIT', 7)
student_2.rate_lecturer(lecturer_2, 'GIT', 8)

cool_reviewer_1.rate_hw(student_1, 'Python', 10)
cool_reviewer_1.rate_hw(student_1, 'Python', 8)
cool_reviewer_1.rate_hw(student_1, 'Python', 9)

cool_reviewer_2.rate_hw(student_2, 'GIT', 10)
cool_reviewer_2.rate_hw(student_2, 'GIT', 10)
cool_reviewer_2.rate_hw(student_2, 'GIT', 7)

print('Студенты:')
print(student_1)
print()
print(student_2)
print()
print()

print('Лекторы:')
print(lecturer_1)
print()
print(lecturer_2)
print()
print()

print(f'Сравнение студентов по средним оценкам за ДЗ: '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()
print()

print(f'Сравнение лекторов по средним оценкам за лекции: '
      f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 > lecturer_2}')
print()
print()

student_list = [student_1, student_2]

lecturer_list = [lecturer_1, lecturer_2]

def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

print(f"Средняя оценка для всех студентов по курсу {'GIT'}: {student_rating(student_list, 'GIT')}")
print()
print()

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()
print()