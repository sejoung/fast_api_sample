import os

from sejoung.configuration import log


def test_setup(setup):
    url = os.getenv("DATABASE_URL")
    log.debug("DATABASE_URL %s", url)
    assert url is not None
