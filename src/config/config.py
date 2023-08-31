from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnection:

    def __init__(self) -> None:
        self.__connection= 'your connection string'
        self.session = None
    
    def __enter__(self):
        engine = create_engine(self.__connection)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()