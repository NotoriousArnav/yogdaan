from faker import Faker
from django.contrib.auth.hashers import make_password
import random

faker = Faker()

people = [
            (
                faker.unique.user_name(),
                faker.unique.name(),
                faker.unique.email(),
                faker.unique.password()
            ) for x in range(100)
        ]

print(f"{len(people)=}")
print(f"{random.choice(people)=}")
