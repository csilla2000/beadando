from dataclasses import dataclass, field


@dataclass
class Person:
    id: str
    name: str
    age: int
    male: bool

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "male": self.male
        }


@dataclass
class Vehicle:
    id: str
    type: str
    model: str
    owner_id: str

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "model": self.model,
            "owner_id": self.owner_id
        }


@dataclass
class HouseholdItem:
    id: str
    name: str
    category: str
    owner_id: str

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "owner_id": self.owner_id
        }
