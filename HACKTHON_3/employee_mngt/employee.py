import uuid

class Employee:
    def __init__(self, name:str, department:str, designation:str, gross_salary:float, tax:float, bonus:float, employee_id=None):
        self.id = employee_id if employee_id else str(uuid.uuid4())
        self.name = name
        self.department = department
        self.designation = designation
        self.gross_salary = gross_salary
        self.tax = (tax/100)*self.gross_salary
        self.bonus = bonus
        self.net=self.tax + self.bonus
        self.net_salary = self.gross_salary - self.net

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation,
            "gross_salary": self.gross_salary,
            "tax": self.tax,
            "bonus": self.bonus,
            "net_salary": self.net_salary
        }

    @staticmethod
    def from_dict(data):
        # Use get() to safely handle missing keys
        return Employee(
            name=data.get("name", ""),
            department=data.get("department", ""),
            designation=data.get("designation", ""),
            gross_salary=data.get("gross_salary", 0.0),
            tax=data.get("tax", 0.0),
            bonus=data.get("bonus", 0.0),
            employee_id=data.get("id")
        )


