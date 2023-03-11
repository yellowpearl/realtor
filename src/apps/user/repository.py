from django.contrib.auth.models import User


class UserRepository:

    def __init__(self):
        self.model = User

    def create_from_email(self, email: str):
        self.model.objects.get_or_create(email=email, defaults={"username": email.split("@")[0]})
