from src.interface_segregation_principle.stage_1_header_interface import user_repository


class MySQLUsersRepository(user_repository.UserRepository):
    def save(self, user) -> None:
        print("Saves a user in MySQL but doesn't commit it to DB")

    def commit(self, user) -> None:
        print("commit a user in MySQL")

    def saveAll(self, user) -> None:
        print("Saves a list of users in MySQL")
