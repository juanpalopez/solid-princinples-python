from src.dependency_inversion_princinple.user import User


class UserStub:
    RAFA_ID = 1
    JAVI_ID = 1

    RAFA_NAME = "Rafa"
    JAVI_NAME = "Javi"

    @staticmethod
    def rafa():
        return User(RAFA_ID, RAFA_NAME)

    @staticmethod
    def javi():
        return User(JAVI_ID, JAVI_NAME)
