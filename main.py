from UserController import UserController
from UserModel import UserModel


user=UserController(UserModel())
result=user.get_by_id(1)

print(result)



            