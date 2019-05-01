from src.dependency_inversion_princinple.user import User
from src.dependency_inversion_princinple.stage_1_instatiating_from_clients.hardcoded_inmemory_user_repository import HardcodedInMemoryUsersRepository


class UserSearcher:
    def __init__(self):
        self.userRepository = HardcodedInMemoryUsersRepository()

    def search(self, id: int):
        return self.userRepository.search(id)
