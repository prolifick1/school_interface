import csv
from .person import Person

class Staff(Person):
    def __init__(self, name, age, password, role, employee_id):
        super().__init__(name, age, password)
        self.role = role
        self.employee_id = employee_id
    def all_staff():
        with open('data/staff.csv') as csvfile:
            reader = csv.reader(csvfile)
            all_staff = list()
            staff_info = dict()
            next(reader)
            for row in reader:
                staff_info['name'] = row[0]
                staff_info['age'] = row[1]
                staff_info['password'] = row[2]
                staff_info['role'] = row[3]
                staff_info['employee_id'] = row[4]
                all_staff.append(Staff(**staff_info))
            return all_staff


