import json


def reading_users():
    try:
        with open("users.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def writing_users(users):
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=2)


class UserRepository:
    def __init__(self):
        self._users = reading_users()

    def get(self) -> json:
        return self._users

    def get_user(self, user_id: int) -> json:
        users = self._users
        for user in users:
            if user['id'] == user_id:
                return user
            else:
                raise NotImplementedError

    def create_user(self, data: dict, calculate_age) -> json:
        if data['firstName'] not in self._users or data['lastName'] not in self._users:
            users = self._users
            max_user_id = max((user["id"] for user in users), default=0)
            new_user_id = max_user_id + 1
            new_user = {
                "id": new_user_id,
                "name": data['firstName'],
                "lastname": data['lastName'],
                "age": calculate_age,
                "group": data["group"] if data["group"] in {"admin", "user", "premium"} else (_ for _ in ()).throw(NotImplementedError)

            }
            users.append(new_user)
            writing_users(users=users)
            return new_user
        else:
            raise NotImplementedError

    def update_user(self, user_id: int, data: dict, calculate_age) -> None:
        users = self._users
        for user in users:
            if user["id"] == user_id:
                if "name" in data:
                    user["firstName"] = data["firstName"]
                if "lastname" in data:
                    user["lastName"] = data["lastName"]
                if "birthYear" in data:
                    user["age"] = calculate_age
                if "group" in data:
                    user["group"] = data["group"]

                writing_users(users=users)
        raise NotImplementedError

    def delete_user(self, user_id: int) -> None:
        users = self._users

        for user in users:
            if user["id"] == user_id:
                users.remove(user)
                writing_users(users=users)

        raise KeyError("User not found")
