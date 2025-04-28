import os
import uuid


def test_setup(setup):
    url = os.getenv("DATABASE_URL")
    print("DATABASE_URL %s", url)
    assert url is not None


def test_uuid(generate_uuid):
    assert generate_uuid is not None
    print(generate_uuid.hex)
    assert isinstance(generate_uuid, uuid.UUID)
    assert len(generate_uuid.hex) == 32
