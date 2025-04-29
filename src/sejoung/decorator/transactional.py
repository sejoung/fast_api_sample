from functools import wraps

from dependency_injector.wiring import inject, Provide


class Transactional:
    commit: bool

    @inject
    def __init__(self, commit=False, session=Provide["database.provided.session"]):
        self.commit = commit
        self.session_f = session

    def __call__(self, func):
        @wraps(func)
        async def _transactional(*args, **kwargs):
            try:
                async with self.session_f as session:
                    async with session.begin():
                        result = await func(*args, **kwargs)
            except Exception as e:
                await session.rollback()
                raise e
            else:
                if self.commit:
                    await session.commit()

            return result

        return _transactional
