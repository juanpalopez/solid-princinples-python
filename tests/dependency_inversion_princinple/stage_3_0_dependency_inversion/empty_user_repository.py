from src.dependency_inversion_princinple.stage_3_0_dependency_inversion import user_repository


class EmptyUsersRepository(user_repository.UserRepository):
    def __init__(self):
        self.users = {}

    def search(self, id: int):
        return None
