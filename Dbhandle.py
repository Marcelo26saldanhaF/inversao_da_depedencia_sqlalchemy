from sqlalchemy import create_engine
from sqlalchemy.orm import Session,declarative_base


class Dbhandle:
    def __init__(self,urlstring) -> None:
        self.__engine=create_engine(urlstring)
        self.Session=Session(self.__engine)
        self.Base=declarative_base()

    def create_all(self):
        self.Base.metadata.create_all(self.__engine)


