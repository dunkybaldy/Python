import unittest
from src.CompanySim.Company import Company
from src.CompanySim.Enums import JobRole

class TestMethods(unittest.TestCase):
    def test_HireEmployee(self):
        company = Company("Company1")

        self.assertEqual(company.name, "Company1")

        company.HireEmployee(10000, "Long John Silver", JobRole.Boss)
        company.HireEmployee(5000, "Not So Long John Metal", JobRole.Goon)
        company.HireEmployee(1500, "Tiny John", JobRole.Goon) 

        total = 0
        for employee in company.employees:
            total += employee.salary

        self.assertEqual(total, 16500)
        self.assertEqual(company.requiredMonthlyIncomeToPayEmployees, total)

if __name__ == '__main__':
    unittest.main()