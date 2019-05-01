from src.dependency_inversion_princinple.stage_3_0_dependency_inversion import user_searcher
from tests.dependency_inversion_princinple.stage_3_0_dependency_inversion import codelytv_staff_user_repository, empty_user_repository
from src.dependency_inversion_princinple import user


def test_find_existing_user():
    userRepository = codelytv_staff_user_repository.CodelyTvStaffUsersRepository()
    userSearcher = user_searcher.UserSearcher(userRepository)
    existingUserId = 1
    expectedUser = user.User(id=1, name='Rafa')

    assert expectedUser == userSearcher.search(existingUserId)


def test_find_existing_user():
    userRepository = empty_user_repository.EmptyUsersRepository()
    userSearcher = user_searcher.UserSearcher(userRepository)
    nonExistingUserId = 5
    expectedEmptyResult = None

    assert expectedEmptyResult == userSearcher.search(nonExistingUserId)
