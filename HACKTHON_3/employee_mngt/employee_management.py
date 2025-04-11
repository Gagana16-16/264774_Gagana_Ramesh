from employee_mngt.employee import Employee

class Employee_management(object):

    def __init__(self):
        self.employee_list = []

    # add a task
    def add_employee(self,name,department, designation, gross_salary,tax,bonus):
        emp = Employee(name,department, designation, gross_salary,tax,bonus)
        self.employee_list.append(emp)
        return emp

    # get all tasks
    def get_all_employee(self):
        return self.employee_list

    def search_employee(self, employee_id):
        for emp in self.employee_list:
            if emp.id == employee_id:
                return emp
        else:
            print("NO ID IN EMPLOYEE RECORDS")

    # delete a task
    def delete_employee(self, employee_id):
        for emp in self.employee_list:
            if emp.id == employee_id:
                self.employee_list.remove(emp)
                return True
        return False

    # load tasks
    def load_employee(self, task_dicts):
        self.employee_list = [Employee.from_dict(td) for td in task_dicts]

    # list of tasks in dictionary format
    def to_dict_list(self):
        return [emp.to_dict() for emp in self.employee_list]

   
