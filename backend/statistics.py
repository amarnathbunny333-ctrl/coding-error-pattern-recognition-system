from collections import Counter
import json
import os


REPORT_FILE = "reports/error_history.json"


# Ensure file exists
if not os.path.exists("reports"):
    os.makedirs("reports")

if not os.path.exists(REPORT_FILE):
    with open(REPORT_FILE, "w") as f:
        json.dump([], f)


def save_error(record):
    """Save each analyzed error"""

    with open(REPORT_FILE, "r") as f:
        data = json.load(f)

    data.append(record)

    with open(REPORT_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_errors():
    """Load all stored errors"""

    with open(REPORT_FILE, "r") as f:
        return json.load(f)


def get_statistics():
    """Generate error insights"""

    data = load_errors()

    error_types = [
        item.get("error_type")
        for item in data
        if item.get("error_type")
    ]

    counter = Counter(error_types)

    if not counter:
        return {
            "total_errors": 0,
            "most_common": None,
            "least_common": None
        }

    most_common = counter.most_common(1)[0]
    least_common = counter.most_common()[-1]

    return {
        "total_errors": len(error_types),
        "most_common": {
            "error": most_common[0],
            "count": most_common[1]
        },
        "least_common": {
            "error": least_common[0],
            "count": least_common[1]
        }
    }