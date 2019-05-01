from src.dependency_inversion_princinple.user import User


class HardcodedInMemoryUsersRepository:
    def __init__(self):
        self.users = {
            1: User(id=1, name="Rafa"),
            2: User(id=2, name="Javi")
        }

    def search(self, id: int):
        return self.users.get(id, None)
