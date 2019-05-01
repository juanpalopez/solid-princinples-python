from src.dependency_inversion_princinple.user import User
from src.dependency_inversion_princinple.stage_2_1_dependency_injection_of_constant_parameters.hardcoded_inmemory_user_repository import HardcodedInMemoryUsersRepository


class UserSearcher:
    def __init__(self, userRepository):
        self.userRepository = userRepository

    def search(self, id: int):
        return self.userRepository.search(id)
