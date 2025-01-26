# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

delimiter = ","
line_terminator = "\n"
with open(INPUT_FILENAME, 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file, delimiter=delimiter)
    data = [row for row in csv_reader]


with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(json.dumps(data, indent=4, ensure_ascii=False), end="")