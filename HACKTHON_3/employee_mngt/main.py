from employee_management import Employee_management

from storage import Storage

def main():
    def display_employee(employee: list) -> None:
        if not employee:
            print("No Employees to display.")
        else:
            for emp in employee:
                print(f"[{emp.id}] Name: {emp.name}, department: {emp.department},designation: {emp.designation} ,Gross_salary: {emp.gross_salary},tax :{emp.tax},bonus:{emp.bonus},net_salary:{emp.net_salary}")


    emp = Employee_management()
    store = Storage()

    saved_employees = store.load()
    emp.load_employee(saved_employees)

    while True:
        print("\n=== employeee Management System ===")
        print("1. Add new employee")
        print("2. View all employee")
        print("3. Search employee by ID")
        print("4. Delete a employee")
        print("5. Exit")

        choice = input("Choice -> ")

        if choice == '1':
            name = input("Enter name :").strip()
            department = input("Enter Department :").strip()
            designation = input("Enter Designation :").strip()
            gross_salary = float(input('Enter gross_salary :'))
            tax = float(input('Enter tax :'))
            bonus = float(input('Enter bonus : '))

            if name:
                employee = emp.add_employee(name,department, designation, gross_salary,tax,bonus)
                store.save(emp.to_dict_list())
                print(f"employee added with ID: {employee.id}")
            else:
                print("Name cannot be empty.")

        elif choice == '2':
            employee = emp.get_all_employee()
            display_employee(employee)

        elif choice == '3':
            eid = input("Enter the Employee ID to search: ").strip()
            employee = emp.search_employee(eid)
            if employee:
                print(f"Found: Name: {employee.name}, department: {employee.department}, designation: {employee.designation} ,Gross_salary: {employee.gross_salary},tax :{employee.tax},bonus:{employee.bonus},net_salary:{employee.net_salary}")
            else:
                print("employeee ID not found.")

        elif choice == '4':
            eid = input("Enter the Employee ID to  delete: ").strip()
            if emp.delete_employee(eid):
                store.save(emp.to_dict_list())
                print(" employee deleted.")
            else:
                print(" employee ID not found.")

        elif choice == '5':
            print("EXIT!")
            break

        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
