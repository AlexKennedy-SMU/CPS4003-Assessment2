import csv
import datetime

def open_csv(filename):
    with open(filename, "r", encoding="latin-1") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(", ".join(row))

if __name__ == "__main__":
    csvfile = "healthcare_dataset.csv"
    open_csv(csvfile)