import pytest

from sejoung.configuration import Database

@pytest.mark.skip
@pytest.mark.asyncio
async def test_data():
    db = Database("mysql+aiomysql://root:root@localhost:3306/test")
    await db.create_database()
