from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import os
from dotenv import load_dotenv
class Command(BaseCommand):
    help = 'Creates a superuser.'
    def handle(self, *args, **options):
        load_dotenv()

        username = os.getenv('SUPERUSER_USERNAME', 'admin')
        password = os.getenv('SUPERUSER_PASSWORD', 'complexpassword123')
        email = os.getenv('SUPERUSER_EMAIL', 'admin@example.com')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
            username=username,
            password=password,
            email=email,
            )
        print('Superuser has been created.')