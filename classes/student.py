from classes.person import Person
import csv

#Student class is in charge of talking to the student 'database'
class Student(Person):
    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password)
        self.role = role
        self.school_id = school_id
    
    def all_students():
        with open('data/students.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            all_students = list()
            student_info = dict()
            next(reader)
            for row in reader:
                student_info['name'] = row[0]
                student_info['age'] = row[1]
                student_info['password'] = row[2]
                student_info['role'] = row[3]
                student_info['school_id'] = row[4]
                all_students.append(Student(**student_info))
            return all_students


