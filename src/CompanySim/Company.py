from src.CompanySim.Employee import Employee

class Company:
    name = ""
    active = False
    requiredMonthlyIncomeToPayEmployees = 0.00
    wantedMonthlyProfit = 0.00
    employees = []
    employeesFired = []

    def __init__(self, name):
        self.name = name
        self.active = True

    def SetActive(self, active):
        self.active = active
        return self.active

    def HireEmployee(self, salary, name, jobRole):
        # add to employees
        emp = Employee(self.name, salary, name, jobRole)
        self.employees.append(emp)
        self.requiredMonthlyIncomeToPayEmployees += salary