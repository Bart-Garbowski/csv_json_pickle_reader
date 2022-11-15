import sys
import csv
import json
import pickle
import os

if len(sys.argv) < 3:
    print("Zbyt mało argumentow! \n"
    "Poprawna forma: python3 nazwa_pliku_otwieranego plik_input plik_output zmiany")
    sys.exit()

arg = sys.argv[1:]

input_file = arg[0]
output_file = arg[1]
instructions = arg[2:]


def read_csv(input_file):
    file_content = []
    with open(input_file, mode="r") as file:
        for row in file.readlines()[0:4]:
            row = row.replace("\n", "")
            row = row.split(",")
            file_content.append(row)
    return file_content


def write_csv(output_file, file_content):
    with open(output_file, mode="w", newline="") as f:
        writer = csv.writer(f)
        for line in file_content:
            writer.writerow(line)


def read_json(input_file):
    with open(input_file, mode="r") as file:
        return json.loads(file.read())


def write_json(output_file, file_content):
    with open(output_file, mode="w", newline="") as file:
        file.write(json.dumps(file_content))


def read_pickle(input_file):
    with open(input_file, mode="rb") as file:
        return pickle.loads(file.read())


def write_pickle(output_file, file_content):
    with open(output_file, mode="wb") as file:
        file.write(pickle.dumps(file_content))


if not os.path.exists(input_file) or not os.path.exists(output_file):
    print(f"Plik nie istnieje! Dostępne pliki w katalogu: {os.listdir()}")
    exit()


if input_file.endswith(".csv"):
    file_content = read_csv(input_file)
    print("Otwieramy plik csv")
elif input_file.endswith(".json"):
    file_content = read_json(input_file)
    print("Otwieramy plik jsno")
elif input_file.endswith(".pickle"):
    file_content = read_pickle(input_file)
    print("Otwieramy plik pickle")
else:
    print(f"Nie ma takiego pliku: {input_file} ")
    exit()

for p in instructions:
    pp = p.split(',')
    try:
        file_content[int(pp[0])][int(pp[1])] = pp[2]
    except IndexError:
        pass

if output_file.endswith(".csv"):
    write_csv(output_file, file_content)
    print("Zapisujemy plik csv")
elif output_file.endswith(".json"):
    write_json(output_file, file_content)
    print("Zapisujemy plik jsno")
elif output_file.endswith(".pickle"):
    write_pickle(output_file, file_content)
    print("Zapisujemy plik pickle")
else:
    print(f"Nie ma takiego pliku: {output_file} ")
