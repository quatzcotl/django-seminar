# /user/factories.py
# pip install factory-boy
import factory
from typing import Final
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

FACTORY_USER_PASSWORD: Final = "abc"


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ("username",)

    username = factory.Iterator(["bob", "alice", "trudy", "mallory", "eve", "grumpy"])
    email = factory.Faker("email")
    password = factory.LazyFunction(lambda: make_password(FACTORY_USER_PASSWORD))
