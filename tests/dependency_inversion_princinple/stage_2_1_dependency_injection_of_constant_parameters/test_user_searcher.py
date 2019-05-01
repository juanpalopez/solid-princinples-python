from src.dependency_inversion_princinple.stage_2_1_dependency_injection_of_constant_parameters import user_searcher
from src.dependency_inversion_princinple.stage_2_1_dependency_injection_of_constant_parameters import hardcoded_inmemory_user_repository
from src.dependency_inversion_princinple import user


def test_find_existing_user():
    rafaId = 1
    rafa = user.User(id=rafaId, name="Rafa")
    users = {rafaId: rafa}
    userRepository = hardcoded_inmemory_user_repository.HardcodedInMemoryUsersRepository(
        users)
    userSearcher = user_searcher.UserSearcher(userRepository)
    existingUserId = 1
    expectedUser = User(id=1, name='Rafa')

    assert expectedUser == userSearcher.search(existingUserId)


def test_find_existing_user():
    users = {}
    userRepository = hardcoded_inmemory_user_repository.HardcodedInMemoryUsersRepository(
        users)
    userSearcher = user_searcher.UserSearcher(userRepository)
    nonExistingUserId = 5
    expectedEmptyResult = None

    assert expectedEmptyResult == userSearcher.search(nonExistingUserId)
