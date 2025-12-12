import json
import os
from datetime import datetime


FILE = "expenses.json"


# create file if it doesn't exist
if not os.path.exists(FILE):
with open(FILE, 'w') as f:
json.dump([], f)


def load():
with open(FILE, 'r') as f:
return json.load(f)


def save(data):
with open(FILE, 'w') as f:
json.dump(data, f, indent=4)


def add_expense(amount, category):
data = load()
entry = {"amount": amount, "category": category, "timestamp": datetime.utcnow().isoformat()}
data.append(entry)
save(data)


def get_total():
data = load()
return sum(item['amount'] for item in data)


def get_all():
return load()


def reset_data():
save([])