# Fake Data
# Faker library

from home.models import * 
from faker import Faker
import random

fake = Faker('en_IN')

# For college fake data
# def dbSeeder(records = 10)->None:
#     college_names = ['IIT Madras', 'VIT Pune', 'IISc Banglore', 'IIT Bombay', 'DY', 'IIT Ropar', 'NIT', 'IIIT', 'JSPM']
#     for i in college_names:
#         address = fake.address()
#         College.objects.create(college_name = i, college_address=address)



# For fake data in Student table
def dbSeeder(records = 10)->None:
    colleges = College.objects.all()

    for i in range(records):
        college = random.choice(colleges)
        gender_choice = random.choice(['Male', 'Female'])
        name = fake.name()
        mobile_number = fake.phone_number()
        email = fake.email()
        gender = gender_choice
        age = random.randint(18, 30)
        student_bio = fake.text()

        Student.objects.create(
            college = college,
            name=name,
            mobile_number=mobile_number,
            email=email,
            gender=gender,
            age=age,
            student_bio=student_bio
        )

# dbSeeder(100) => for 100 records creation