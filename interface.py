from abc import abstractmethod
class TodoInterface:
    @abstractmethod
    def get_todo_from_id(self, id: int):
        ...
    
    @abstractmethod
    def get(self):
        ...
    
    @abstractmethod
    def create(self, content:str):
        ...
    
    @abstractmethod
    def delete(self, id: int):
        ...
    
    @abstractmethod
    def update(self, id: int, content: str):
        ...