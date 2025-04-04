class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
   
    def get_details(self):
        return(f"name:{self.name},age:{self.age},gender:{self.gender}")
    
class Employee(Person):
    def __init__(self,name,age,gender,emp_id,department,salary):
        super().__init__(name,age,gender)
        self.emp_id=emp_id
        self.department=department
        self.salary=salary
   
    def get_details(self):
        super().get_details()
        return f"name:{self.name},age:{self.age},gender:{self.gender},emp_id:{self.emp_id},department:{self.department},salary:{self.salary}"
 
    def is_eligible_for_bonus(self):
        if self.salary<50000:
            return True
        else:
            return False
       
    @classmethod
    def from_string(cls,data_string):
        fdata = data_string.split(',')
        return cls(fdata[0], int(fdata[1]), fdata[2], fdata[3], fdata[4], float(fdata[5]))
 
    @staticmethod
    def bonus_policy():
        print("---------------------------Description-----------------------------------")
        print("Bonus Policy: Employees earning less than 50000 are eligible for a bonus.")
 
class Department():
    def __init__(self,name):
        self.name=name
        self.employees=[]
 
    def add_employee(self,employee):
        self.employees.append(employee)
 
    def get_average_salary(self):
        if self.employees:
            total_salary=sum(emp.salary for emp in self.employees)
            return total_salary/len(self.employees)
        return 0
   
    def get_all_employees(self):
        return [emp.get_details() for emp in self.employees]
 
import json
 
def save_to_json(employees, filename="save_to.json"):
    with open(filename, 'w') as file:
        employees_data = [emp.__dict__ for emp in employees]
        json.dump(employees_data, file, indent=4)
 

def load_from_json(filename="save_to.json"):
    with open(filename, 'r') as file:
        employees_data = json.load(file)
        employees = []
       
        for data in employees_data:
            emp = Employee(data['name'], data['age'], data['gender'], data['emp_id'], data['department'], data['salary'])
            employees.append(emp)
        return employees    




