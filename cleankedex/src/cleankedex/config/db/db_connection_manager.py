from cleankedex.config.db.db_session import SessionLocal
from sqlalchemy.orm import Session


class DbConnectionManager:
    """
    Db connection manager (context manager)
    """

    __session: Session

    def __init__(self):
        self.__session = None

    def __enter__(self):
        # Initialize database
        self.__session = SessionLocal()
        return self

    def __exit__(self, exc_type, exc_value, exc_tracceback):
        self.__session.close()

    @property
    def session(self):
        """
        Return a session to operate with the database
        """
        return self.__session
