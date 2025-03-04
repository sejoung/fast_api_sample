from sejoung.repositories.user import UserRepository


def test_user_repository(session):
    repository = UserRepository(session)
    actual = repository.get_user(1)
    assert actual is None
