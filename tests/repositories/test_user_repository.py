from sejoung.repositories.user import UserRepository


def test_user_repository(session):
    repository = UserRepository(session)
    actaul = repository.get_user(1)

