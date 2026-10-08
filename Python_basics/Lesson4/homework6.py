# Create an abstract class employee with an abstract method calculate_salary().
# Create subclasses intern, fulltime employee, contractemployee and 
# that implement the method differently

from abc import ABC, abstractmethod

class employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class intern(employee):
    def calculate_salary(self):
        print(f"Salary for intern is: {25_000}")

class fulltime_employee(employee):
    def calculate_salary(self):
        print(f"Salary for fulltime employee is: {95_000}")

class contract_employee(employee):
    def calculate_salary(self):
        print(f"Salary for contract employee is: {50_000}")

intern1 = intern()
fulltime_employee1 = fulltime_employee()
contract_employee1 = contract_employee()

intern1.calculate_salary()
fulltime_employee1.calculate_salary()
contract_employee1.calculate_salary()