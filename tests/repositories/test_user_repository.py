from sejoung.repositories.user_repository import UserRepository


def test_user_repository(session):
    repository = UserRepository(session)
    actual = repository.find_one()
    assert actual is None

def test_create_user(session):
    repository = UserRepository(session)
    user = repository.create("zolla@abc.com", "beni")
    assert user.email == "zolla@abc.com"
    assert user.name == "beni"
    assert user.id is not None
