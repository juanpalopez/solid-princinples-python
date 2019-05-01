from src.dependency_inversion_princinple.stage_1_instatiating_from_clients import user_searcher


def test_find_existing_user():
    userSearcher = user_searcher.UserSearcher()
    existingUserId = 1
    expectedUser = User(id=1, name='Rafa')

    assert expectedUser == userSearcher.search(existingUserId)


def test_find_existing_user():
    userSearcher = user_searcher.UserSearcher()
    nonExistingUserId = 5
    expectedEmptyResult = None

    assert expectedEmptyResult == userSearcher.search(nonExistingUserId)
