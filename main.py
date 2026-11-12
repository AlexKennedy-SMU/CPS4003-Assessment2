import csv

def open_csv(csv):
    with open(csv, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(", ".join(row))

if __name__ == "__main__":
    csv = "healthcare_dataset.csv"
    open_csv(csv)