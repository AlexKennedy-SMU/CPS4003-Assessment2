import csv
import datetime
import re

# Fixes the "name" field of the dataset
def name_fix(name):
    '''function name_fix(name)
    
    parameters:
    name: desired name to fix (required)
    
    returns:
    name with select prefixes, suffixes, and whitespace removed and capitalisation corrected
    '''
    regex_pattern_prefix = r"^(Mr|Mrs|Ms|Dr|Miss)\.?\s+"
    regex_pattern_suffix = r",?\s+(DDS|MD|PhD|DVM)\.?$"
    name_fixed_prefix = re.sub(regex_pattern_prefix, "", name, flags=re.IGNORECASE)
    name_fixed_suffix = re.sub(regex_pattern_suffix, "", name_fixed_prefix, flags=re.IGNORECASE)
    name_no_whitespace = " ".join(name_fixed_suffix.split())
    return name_no_whitespace.title()

def date_converter(date):
    '''Converts dates given in format %d/%m/%Y to datetime objects'''
    date_string = date
    date_obj = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    return date_obj

def open_csv(filename):
    '''function open_csv
    
    parameters:
    filename: desired file to open in csv format (required)
    
    returns:
    list of dictionaries containing every entry in the dataset, with standardised formatting
    '''
    reformattedData = []
    # only csv files that share the same columns as the dataset can be read in this implementation
    with open("data_cleaning_log", "w") as error_log:
        with open(filename, "r", encoding="latin-1") as csvfile:
            csvreader = csv.DictReader(csvfile)
            for rowid, row in enumerate(csvreader, start=2):
                try:
                    row["Name"] = name_fix(row["Name"])
                    row["Age"] = int(row["Age"])
                    row["Date of Admission"] = date_converter(row["Date of Admission"])
                    temp_billing_amount = float(row["Billing Amount"]
                                                .replace("£","")
                                                .replace(",","")
                                                .replace(" ",""))
                    if temp_billing_amount < 0:
                        error_log.write(f"Warning: Row {rowid}: Negative billing amount ({temp_billing_amount}). Skipped\n")
                        continue
                    row["Billing Amount"] = round(temp_billing_amount, 2)
                    row["Room Number"] = int(row["Room Number"])
                    row["Discharge Date"] = date_converter(row["Discharge Date"])
                    print(row)
                    reformattedData.append(row)
                except ValueError as e:
                    error_log.write(f'Error: Row {rowid}: Type conversion failed ({e}). Skipped.\n')

            

if __name__ == "__main__":
    csvfile = "healthcare_dataset.csv"
    open_csv(csvfile)