from itertools import count


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = float()
        
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'        
    
    def __str__(self):
        count_grade = 0
        for k in self.grades:
            count_grade += len(self.grades[k])
        self.average_grade = sum(map(sum, self.grades.values()))/count_grade
        result = f'''Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self.average_grade}
        Курсы в процессе изучения: {self.courses_in_progress}
        Завершенные курсы" {self.finished_courses}'''
        return result    
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        return self.average_grade > other.average_grade
            
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
 
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_value = float()
        self.grades = {}
   
    def __str__(self):
        count_grade = 0
        for v in self.grades:
            count_grade += len(self.grades[v])
        self.average_value = sum(self.grades.values())/count_grade
        result = f'''Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {self.average_value}'''
        return result    
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не Лектор!')
            return
        return self.average_value > other.average_value     


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
                
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        result = f'''Имя: {self.name}
        Фамилия: {self.surname}''' 
        return result
    
    
    
lecturer_1 = Lecturer ('Dima', 'Smirnov')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer ('ilya', 'Zaycev')
lecturer_2.courses_attached += ['Python']


student_1 = Student ('Alexey','Kononenko', 'Male')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student ('Zina','Korableva', 'Female')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Введение в программирование']

reviewer_1 = Reviewer ('Olga', 'Ivanova')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer ('John', 'Wick')
reviewer_2.courses_attached += ['Python']


student_1.rate_lecture (lecturer_1, 'Python', 7)
student_1.rate_lecture (lecturer_2, 'Python', 9)
student_2.rate_lecture (lecturer_1, 'Python', 4)
student_2.rate_lecture (lecturer_2, 'Python', 5)

reviewer_1.rate_hw (student_1, 'Python',10 )
reviewer_1.rate_hw (student_2, 'Python', 6)
reviewer_2.rate_hw (student_1, 'Python', 7)
reviewer_2.rate_hw (student_2, 'Python', 9)


print(f'''Перечень студентов:
      {student_1}, 
      {student_2} ''')