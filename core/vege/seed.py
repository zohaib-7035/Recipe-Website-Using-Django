from faker import Faker
from vege.models import Vege
from django.contrib.auth.models import User
import random

fake = Faker()

def create_fake_veges(n=10):
    users = User.objects.all()
    for _ in range(n):
        user = random.choice(users) if users else None
        name = fake.word().capitalize()
        description = fake.paragraph()
        Vege.objects.create(
            user=user,
            name=name,
            description=description,
            image='vegetables/dummy.jpg'  # Provide a dummy image path
        )
