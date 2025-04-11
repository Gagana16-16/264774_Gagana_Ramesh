from employee_mngt.employee_management import Employee_management
import unittest
class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        self.emp = Employee_management()

    def test_add(self):
        self.emp.add_employee("Gagana", 'Validation', "T1", 500000, 2, 0)
        count = self.emp.get_all_employee()
        firstdata = len(count)
        self.emp.add_employee("ANU", 'Development', "Associate", 500000, 1, 10000)
        count1 = self.emp.get_all_employee()
        secounddata = len(count1)
        self.assertGreater(secounddata, firstdata)
        self.assertEqual(firstdata + 1, len(count1))

    def test_deleting(self):
        a = self.emp.add_employee("Gagana", 'Validation', "T1", 500000, 2, 0)
        id1 = a.id
        self.emp.add_employee("ANU", 'Development', "Associate", 500000, 1, 10000)
        self.emp.delete_employee(id1)
        total = self.emp.get_all_employee()
        self.assertNotIn(id1, [emp.id for emp in total])

    def test_find_by_id(self):
        a = self.emp.add_employee("Gagana", 'Validation', "T1", 500000, 2, 0)
        found = self.emp.search_employee(a.id)
        self.assertEqual(found.name, "Gagana")

    def tearDown(self):
        del self.emp

if __name__ == "__main__":
    unittest.main()
