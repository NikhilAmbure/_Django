import random

class Employee:
    company_name = "Google"

    # Method - 2 (Using decorator)
    @classmethod
    def change_company_name(cls):
        companies = ['Microsoft', 'Google', 'Spotify']
        company = random.choice(companies)
        cls.company_name = company
        print('Company changed')

Employee.change_company_name()

# Method - 1
Employee.company_name = 'Alphabay'