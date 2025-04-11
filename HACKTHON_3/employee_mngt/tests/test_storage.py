import unittest
import os
from employee_mngt.storage import Storage

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.file = "employs.pkl"
        self.storage = Storage(self.file)

    def tearDown(self):
        if os.path.exists(self.file):
            os.remove(self.file)

    def test_save_and_load(self):
        data = [{
            "id": "1",
            "name": "gagana",
            "department": "Finance",
            "designation": "Associate",
            "gross_salary": 500000,
            "tax": 0,
            "bonus": 15000,
            "net_salary": 485000
        }]

        self.storage.save(data)
        loaded = self.storage.load()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["name"], "gagana")


if __name__ == "__main__":
    unittest.main()
