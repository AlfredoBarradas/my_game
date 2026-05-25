class Entity():
    def __init__(self, id: int):
        self.id = [id]
        self.__it_exists = False

    def getId(self):
        return self.id

    def is_alive(self):
        return not self.__it_exists

    def killEntity(self):
        self.__it_exists = True
        
