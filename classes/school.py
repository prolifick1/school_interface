from .student import Student
from .staff import Staff
class School:
    def __init__(self, name):
        self.name = name
        self.students = Student.all_students()
        self.staff = Staff.all_staff()
    def list_students(self):
        for i, student in enumerate(self.students):
            print(f"{i+1}. {student.name} {student.school_id}")
    def find_student_by_id(self, student_id):
        for student in Student.all_students():
            if student.school_id == student_id:
                return student.__str__()
    def add_student(self, student):
        print('called')
        the_student = Student(**student) 
        self.students.append(the_student)
    def delete_student(self, input_id):
        for i, student in enumerate(self.students):
            if student.school_id == input_id:
                self.students.pop(i)
