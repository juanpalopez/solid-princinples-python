from abc import ABC


class UserRepository(ABC):
    def save(self, user) -> None:
        raise NotImplementedError

    def commit(self, user) -> None:
        raise NotImplementedError

    def saveAll(self, users) -> None:
        raise NotImplementedError
