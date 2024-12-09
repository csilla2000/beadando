import json
import os
from project_dataclasses import Person, Vehicle, HouseholdItem


def read_people_json(path: str, file_name: str = "people.json") -> list[Person]:
    with open(os.path.join(path, file_name), mode="r", encoding="utf-8") as file:
        return [Person(**person) for person in json.load(file)]


def write_people_json(people: list[Person], path: str, file_name: str = "people.json") -> None:
    with open(os.path.join(path, file_name), mode="w", encoding="utf-8") as file:
        json.dump([person.to_dict() for person in people], file, indent=2)


def read_vehicles_json(path: str, file_name: str = "vehicles.json") -> list[Vehicle]:
    with open(os.path.join(path, file_name), mode="r", encoding="utf-8") as file:
        return [Vehicle(**vehicle) for vehicle in json.load(file)]


def write_vehicles_json(vehicles: list[Vehicle], path: str, file_name: str = "vehicles.json") -> None:
    with open(os.path.join(path, file_name), mode="w", encoding="utf-8") as file:
        json.dump([vehicle.to_dict() for vehicle in vehicles], file, indent=2)


def read_household_items_json(path: str, file_name: str = "household_items.json") -> list[HouseholdItem]:
    with open(os.path.join(path, file_name), mode="r", encoding="utf-8") as file:
        return [HouseholdItem(**item) for item in json.load(file)]


def write_household_items_json(household_items: list[HouseholdItem], path: str, file_name: str = "household_items.json") -> None:
    with open(os.path.join(path, file_name), mode="w", encoding="utf-8") as file:
        json.dump([item.to_dict() for item in household_items], file, indent=2)
