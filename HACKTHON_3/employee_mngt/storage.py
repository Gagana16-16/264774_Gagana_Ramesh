import os
import pickle

class Storage:
    def __init__(self, filename="employs.pkl"):
        self.filename = filename

    def save(self, employee_list):
        with open(self.filename, "wb") as f:
            pickle.dump(employee_list, f)


    def load(self):
        try:
            with open(self.filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []
