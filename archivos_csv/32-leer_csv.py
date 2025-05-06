import csv

with open("datos.csv") as arhivo:
    reader = csv.reader(arhivo)
    for row in reader:
        print(row)