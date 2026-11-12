import csv
import datetime
import re
import pytest

def name_fix(name):
    regex_pattern_prefix = r"^(Mr|Mrs|Ms|Dr|Miss)\.?\s+"
    regex_pattern_suffix = r",?\s+(DDS|MD|PhD|DVM)\.?$"
    name_fixed_prefix = re.sub(regex_pattern_prefix, "", name, flags=re.IGNORECASE)
    name_fixed_suffix = re.sub(regex_pattern_suffix, "", name_fixed_prefix, flags=re.IGNORECASE)
    name_no_whitespace = " ".join(name_fixed_suffix.split())
    return name_no_whitespace.title()

@pytest.mark.parametrize("name, expected", [
    ("dR. JoHn SmiTH, Md", "John Smith"),
    ("jACqUeLINE jORdaN", "Jacqueline Jordan"),
    ("DR. LaUreN ClaRk DDs","Lauren Clark"),
    ("   robiN   coX   ","Robin Cox"),
    ("ms. Jane Doe","Jane Doe"),
    ("", ""),
])
def test_name_fix(name, expected):
    assert name_fix(name) == expected


def open_csv(filename):
    reformattedData = []
    with open(filename, "r", encoding="latin-1") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            row["Name"] = name_fix(row["Name"])
            print(row)
            

if __name__ == "__main__":
    csvfile = "healthcare_dataset.csv"
    open_csv(csvfile)