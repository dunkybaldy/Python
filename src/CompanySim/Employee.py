import src.CompanySim.Enums as Enums

class Employee:
    company = ""
    salary = 0.00
    name = ""
    jobRole = Enums.JobRole.NoRole

    def __init__(self, company, salary, name, jobRole):
        self.company = company
        self.salary = salary
        self.name = name
        self.jobRole = jobRole

    def Salary(self, salary):
        if salary != self.salary:
            self.salary = salary
        return

    def Company(self, company):
        if company != self.company:
            self.company = company
        return
        
    