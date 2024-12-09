class Person:
    id: str
    name: str
    age: int
    male: bool

    def __init__(self, id: str, name: str, age: int, male: bool = True):
        self.id = id
        self.name = name
        self.age = age
        self.male = male


class Vehicle:
    id: str
    type: str
    model: str
    owner_id: str

    def __init__(self, id: str, type: str, model: str, owner_id: str):
        self.id = id
        self.type = type
        self.model = model
        self.owner_id = owner_id


class HouseholdItem:
    id: str
    name: str
    category: str
    owner_id: str

    def __init__(self, id: str, name: str, category: str, owner_id: str):
        self.id = id
        self.name = name
        self.category = category
        self.owner_id = owner_id
