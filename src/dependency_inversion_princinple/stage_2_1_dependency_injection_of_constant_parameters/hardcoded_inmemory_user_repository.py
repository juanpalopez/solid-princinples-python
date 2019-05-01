from src.dependency_inversion_princinple.user import User


class HardcodedInMemoryUsersRepository:
    def __init__(self, users):
        self.users = users

    def search(self, id: int):
        return self.users.get(id, None)
