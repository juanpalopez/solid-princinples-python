from src.dependency_inversion_princinple.stage_2_0_dependency_injection import user_searcher
from src.dependency_inversion_princinple.stage_2_0_dependency_injection import hardcoded_inmemory_user_repository


def test_find_existing_user():
    userRepository = hardcoded_inmemory_user_repository.HardcodedInMemoryUsersRepository()
    userSearcher = user_searcher.UserSearcher(userRepository)
    existingUserId = 1
    expectedUser = User(id=1, name='Rafa')

    assert expectedUser == userSearcher.search(existingUserId)


def test_find_existing_user():
    userRepository = hardcoded_inmemory_user_repository.HardcodedInMemoryUsersRepository()
    userSearcher = user_searcher.UserSearcher(userRepository)
    nonExistingUserId = 5
    expectedEmptyResult = None

    assert expectedEmptyResult == userSearcher.search(nonExistingUserId)
