import os
import csv
from project_dataclasses import Person, Vehicle, HouseholdItem


def read_people(path: str, file_name: str = "people", extension: str = ".csv", delimiter: str = ";") -> list[Person]:
    with open(os.path.join(path, file_name + extension), "r", encoding="utf-8") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        return [Person(row["id"], row["name"], int(row["age"]), bool(row["male"])) for row in rows]


def write_people(people: list[Person], path: str, file_name: str = "people", extension: str = ".csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name + extension), "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "age", "male"], delimiter=delimiter)
        writer.writeheader()
        for person in people:
            writer.writerow(person.to_dict())


def read_vehicles(path: str, file_name: str = "vehicles", extension: str = ".csv", delimiter: str = ";") -> list[Vehicle]:
    with open(os.path.join(path, file_name + extension), "r", encoding="utf-8") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        return [Vehicle(row["id"], row["type"], row["model"], row["owner_id"]) for row in rows]


def write_vehicles(vehicles: list[Vehicle], path: str, file_name: str = "vehicles", extension: str = ".csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name + extension), "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "type", "model", "owner_id"], delimiter=delimiter)
        writer.writeheader()
        for vehicle in vehicles:
            writer.writerow(vehicle.to_dict())


def read_household_items(path: str, file_name: str = "household_items", extension: str = ".csv", delimiter: str = ";") -> list[HouseholdItem]:
    with open(os.path.join(path, file_name + extension), "r", encoding="utf-8") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        return [HouseholdItem(row["id"], row["name"], row["category"], row["owner_id"]) for row in rows]


def write_household_items(household_items: list[HouseholdItem], path: str, file_name: str = "household_items", extension: str = ".csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name + extension), "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "category", "owner_id"], delimiter=delimiter)
        writer.writeheader()
        for item in household_items:
            writer.writerow(item.to_dict())
