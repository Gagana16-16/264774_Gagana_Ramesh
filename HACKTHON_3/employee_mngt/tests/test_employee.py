import unittest
import os
from employee_mngt.employee import Employee
class Testemployee(unittest.TestCase):
    def test_create_employee(self):
        s = Employee("Gagana", 'Validation', "T1",500000,2,0)
        self.assertEqual(s.name, "Gagana")
        self.assertEqual(s.department, "Validation")
        self.assertEqual(s.designation, "T1")
        self.assertEqual(s.gross_salary, 500000)
        self.assertEqual(s.tax, 10000.0)
        self.assertEqual(s.bonus, 0)

    def test_dict_conversion(self):
        e = Employee("ANU", 'Development', "Associate",500000,1,10000)
        d = e.to_dict()
        e2 = Employee.from_dict(d)
        self.assertEqual(e.id, e2.id)

    def test_net_salary(self):
        e = Employee("John", 'Development', "Associate",600000,3,10000)
        self.assertEqual(e.net_salary,572000.0)


if __name__ == "__main__":
    unittest.main()
