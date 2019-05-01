from src.interface_segregation_principle.stage_1_header_interface import user_repository


class RedisUsersRepository(user_repository.UserRepository):
    def save(self, user) -> None:
        print("Saves a user in Redis")

    def commit(self, user) -> None:
        pass

    def saveAll(self, user) -> None:
        print("Saves a list of users in Redis")
