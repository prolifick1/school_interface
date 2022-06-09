#interface

from classes.school import School

school = School('Ridgemont High')

mode = None

while(mode != '5'):
    mode = input("""
What would you like to do?
Options:
    1. List All Students
    2. View Individual Student <student_id>
    3. Add a Student
    4. Remove a Student <student_id>
    5. Quit
    """)

    if mode == '1':
        school.list_students()
        pass
    elif mode == '2':
        student_id = input('Enter student id: ')
        student = school.find_student_by_id(student_id)
        str(student)
        pass
    elif mode == '3':  
        student_data = {'role':'student'}
        student_data['name']      = input('Enter student name:\n')
        student_data['age']       = input('Enter student age: \n')
        student_data['school_id'] = input('Enter student school id: \n')
        student_data['password']  = input('Enter student password: \n')
        school.add_student(student_data)
    elif mode == '4':
        school_id = input('Enter an id to delete student\n')
        school.delete_student(school_id)
    elif mode == '5': 
            break
