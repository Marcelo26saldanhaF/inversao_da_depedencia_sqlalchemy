from abc import abstractmethod,ABC


class IUser(ABC):
    @abstractmethod
    def get_by_id(self,id):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass


    @abstractmethod
    def insert(self):
        pass
