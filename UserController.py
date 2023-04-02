from interface import IUser


class UserController:
    def __init__(self,user:IUser) -> None:
        self.user_model=user

    def get_by_id(self,id:int):
        return self.user_model.get_by_id(id)