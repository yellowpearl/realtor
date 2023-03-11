from apps.user.repository import UserRepository


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def create_from_email(self, email: str):
        self.repository.create_from_email(email)
