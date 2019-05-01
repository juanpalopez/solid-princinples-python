from src.dependency_inversion_princinple.stage_3_0_dependency_inversion import user_repository
from tests.dependency_inversion_princinple.stage_3_0_dependency_inversion.user_stub import UserStub


class CodelyTvStaffUsersRepository(user_repository.UserRepository):
    def __init__(self):
        self.users = {
            UserStub.RAFA_ID: UserStub.rafa(),
            UserStub.JAVI_ID: UserStub.javi()
        }

    def search(self, id: int):
        return self.users.get(id, None)
