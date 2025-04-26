import os
import uuid

from sejoung.configuration import log


def test_setup(setup):
    url = os.getenv("DATABASE_URL")
    log.debug("DATABASE_URL %s", url)
    assert url is not None

def test_uuid(generate_uuid):
    assert generate_uuid is not None
    log.debug(generate_uuid.hex)
    assert isinstance(generate_uuid, uuid.UUID)
    assert len(generate_uuid.hex) == 32
