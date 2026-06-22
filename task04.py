# python3

import json
import re

INPUT_FILE = "data.csv"
OUTPUT_FILE = "clean_data.json"


def clean_value(value):
    if not value:
        return ""

    value = value.strip()

    if "@" in value:
        value = value.lower()

    value = re.sub(r"[^\w@.\- ]", "", value)

    return value


def read_file():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines() if line.strip()]


def extract_headers(lines):
    return [h.strip().lower() for h in lines[0].split(",")]


def process_rows(lines, headers):
    rows = [line.split(",") for line in lines[1:]]

    return [
        {
            headers[i]: clean_value(row[i]) if i < len(row) else ""
            for i in range(len(headers))
        }
        for row in rows
    ]


def remove_corrupted(data):
    return [
        record for record in data
        if any(value != "" for value in record.values())
    ]


def save_json(data):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def main():
    print("📥 Reading CSV...")
    lines = read_file()

    if not lines:
        print("❌ File is empty or missing!")
        return

    headers = extract_headers(lines)

    print("⚙️ Processing data...")
    raw_data = process_rows(lines, headers)
    clean_data = remove_corrupted(raw_data)

    print("💾 Saving JSON...")
    save_json(clean_data)

    print("✅ DONE! Check clean_data.json")


if __name__ == "__main__":
    main()