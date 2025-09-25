from user.factories import UserFactory

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

User = get_user_model()


class Command(BaseCommand):

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "-n",
            "--number",
            type=int,
            help="Amount of users to be generated",
            required=True,
        )

        parser.epilog = "Usage: python manage.py create_users -n 10"

    @transaction.atomic
    def handle(self, *args, **options):

        number = options.get("number")

        print("Deleting users...")
        User.objects.exclude(username="admin").delete()

        if number and number > 0:
            for _ in range(number):
                p = UserFactory()
                print(f"=> {p}")

        print(f"{number} User erfolgreich angelegt!")
