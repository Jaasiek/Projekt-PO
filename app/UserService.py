from datetime import datetime
from repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def get_all_users(self):
        return self._repository.get()

    def get_user(self, user_id: int):
        return self._repository.get_user(user_id=user_id)

    def create_user(self, data: dict):
        return self._repository.create_user(data=data, calculate_age=self._calculate_age(data['birthYear']))

    def update_user(self, user_id, data):
        return self._repository.update_user(user_id=user_id, data=data, calculate_age=self._calculate_age(data['birthYear']))

    def delete_user(self, user_id):
        return self._repository.delete_user(user_id=user_id)

    @staticmethod
    def _calculate_age(birth_year):
        current_year = datetime.now().year
        return current_year - birth_year
