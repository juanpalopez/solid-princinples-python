class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __eq__(self, other) -> bool:
        if self == other:
            return True

        if not isinstance(other, self.__class__):
            return False

        return self.id == other.id and self.name == other.name
