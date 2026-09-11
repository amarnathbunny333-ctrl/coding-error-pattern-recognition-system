import json
import os
from datetime import datetime

FILE = "reports/history.json"

os.makedirs("reports", exist_ok=True)

if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f)


def save_history(record):
    with open(FILE, "r") as f:
        data = json.load(f)

    record["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data.append(record)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def get_history():
    with open(FILE, "r") as f:
        return json.load(f)