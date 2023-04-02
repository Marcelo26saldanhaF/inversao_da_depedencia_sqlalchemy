from Dbhandle import Dbhandle
from sqlalchemy import Integer,String,select
from sqlalchemy.orm import Mapped,mapped_column
from interface import IUser



db=Dbhandle('sqlite:///teste.db')

class Meta(type(db.Base),type(IUser)):
    pass


class UserModel(db.Base,IUser,metaclass=Meta):
    __tablename__='usuarios'
    id:Mapped[int]=mapped_column(Integer(),primary_key=True,autoincrement=True)
    username:Mapped[str]=mapped_column(String(20),nullable=False)
    

    def get_by_id(self,id:int):
        with db.Session as s:
            stm=select(UserModel).where(UserModel.id==id)
            result=s.scalar(stm)
            return result
    
    def update(self):
        with db.Session as s:
            pass
    
    def delete(self):
        with db.Session as s:
            pass
    
    def insert(self):
        with db.Session as s:
            pass
    

    def __repr__(self) -> str:
        return f'{self.id}--{self.username}'
    


