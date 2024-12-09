import random
from faker import Faker
from project_dataclasses import Person, Vehicle, HouseholdItem


def generate_people(n: int):
    fake = Faker()
    return [Person(f"P-{i:04}", fake.name(), random.randint(18, 80), bool(random.getrandbits(1))) for i in range(n)]


def generate_vehicles(n: int, people):
    types = ["Car", "Bike", "Truck"]
    models = ["Model A", "Model B", "Model C"]
    return [Vehicle(f"V-{i:04}", random.choice(types), random.choice(models), random.choice(people).id) for i in
            range(n)]


def generate_household_items(n: int, people):
    items = ["Chair", "Table", "Lamp"]
    categories = ["Furniture", "Electronics"]
    return [HouseholdItem(f"H-{i:04}", random.choice(items), random.choice(categories), random.choice(people).id) for i
            in range(n)]
