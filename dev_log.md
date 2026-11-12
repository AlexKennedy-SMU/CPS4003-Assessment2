Traceback (most recent call last):
  File "c:\Users\light\Documents\GitHub Repos\CPS4003-Assessment2\main.py", line 11, in <module>
    open_csv(csv)
    ~~~~~~~~^^^^^
  File "c:\Users\light\Documents\GitHub Repos\CPS4003-Assessment2\main.py", line 4, in open_csv
    with open(csv, r) as csvfile:
                   ^
NameError: name 'r' is not defined

Fix: added double quotes "" around r

Traceback (most recent call last):
  File "c:\Users\light\Documents\GitHub Repos\CPS4003-Assessment2\main.py", line 11, in <module>
    open_csv(csv)
    ~~~~~~~~^^^^^
  File "c:\Users\light\Documents\GitHub Repos\CPS4003-Assessment2\main.py", line 5, in open_csv
    csvreader = csv.reader(csvfile)
                ^^^^^^^^^^
AttributeError: 'str' object has no attribute 'reader'

Fix: changed parameter name "csv" to "filename" and changed variable name "csv" to "csvfile"

Traceback (most recent call last):
  File "c:\Users\light\Documents\GitHub Repos\CPS4003-Assessment2\main.py", line 11, in <module>
    open_csv(csvfile)
    ~~~~~~~~^^^^^^^^^
  File "c:\Users\light\Documents\GitHub Repos\CPS4003-Assessment2\main.py", line 6, in open_csv
    for row in csvreader:
               ^^^^^^^^^
  File "<frozen codecs>", line 325, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa3 in position 265: invalid start byte

Fix: change default "utf-8" encoding of open() function to "latin-1"

Problem: I used .capitalize() to fix the capitalisation of the "Name" column but it only capitalised the first letter of the first name and not the first letter of both names
Fix: change .capitalize() to .title()

Problem: Inconsistent titles, such as mr, ms, dr and variations, and name endings, such as jr, sr and md, remain in the patient name dataset which will break analysis and search code later on
Fix: use the re library to remove the titles and suffixes

Using pytest to test function name_fix()
current function code:
def name_fix(name):
    regex_pattern_prefix = r"^(Mr|Mrs|Ms|Dr|Miss)\.?\s+"
    regex_pattern_suffix = r",?\s+(DDS|MD|PhD|Jr|Sr)$"
    name_fixed_prefix = re.sub(regex_pattern_prefix, "", name, flags=re.IGNORECASE)
    name_fixed_suffix = re.sub(regex_pattern_suffix, "", name_fixed_prefix, flags=re.IGNORECASE)
    print(f'half fixed name: {name_fixed_prefix}')
    print(f'fully fixed name: {name_fixed_suffix}')

test code:
@pytest.mark.parametrize("name, expected", [
    ("dR. JoHn SmiTH, MMd", "John Smith"),
    ("jACqUeLINE jORdaN", "Jacqueline Jordan"),
    ("DR. LaUreN ClaRk DDs","Lauren Clark"),
    ("   robiN   coX   ","Robin Cox"),
    ("ms. Jane Doe","Jane Doe"),
    ("", ""),
])
def test_name_fix(name, expected):
    assert name_fix(name) == expected

test 1
========================== short test summary info ==========================
FAILED main.py::test_name_fix[dR. JoHn SmiTH, Md-John Smith] - AssertionError: assert None == 'John Smith'
FAILED main.py::test_name_fix[jACqUeLINE jORdaN-Jacqueline Jordan] - AssertionError: assert None == 'Jacqueline Jordan'
FAILED main.py::test_name_fix[DR. LaUreN ClaRk DDs-Lauren Clark] - AssertionError: assert None == 'Lauren Clark'
FAILED main.py::test_name_fix[   robiN   coX   -Robin Cox] - AssertionError: assert None == 'Robin Cox'
FAILED main.py::test_name_fix[ms. Jane Doe-Jane Doe] - AssertionError: assert None == 'Jane Doe'
FAILED main.py::test_name_fix[-] - AssertionError: assert None == ''
============================= 6 failed in 0.12s =============================

problem: function doesnt return anything
fix: added "return name_fixed_suffix" to end of function

test 2
========================== short test summary info ==========================
FAILED main.py::test_name_fix[dR. JoHn SmiTH, Md-John Smith] - AssertionError: assert 'JoHn SmiTH' == 'John Smith'
FAILED main.py::test_name_fix[jACqUeLINE jORdaN-Jacqueline Jordan] - AssertionError: assert 'jACqUeLINE jORdaN' == 'Jacqueline Jordan'
FAILED main.py::test_name_fix[DR. LaUreN ClaRk DDs-Lauren Clark] - AssertionError: assert 'LaUreN ClaRk' == 'Lauren Clark'
FAILED main.py::test_name_fix[   robiN   coX   -Robin Cox] - AssertionError: assert '   robiN   coX   ' == 'Robin Cox'
======================== 4 failed, 2 passed in 0.15s ========================

problem: function doesnt fix excess whitespace
fix: used " ".join(name_fixed_suffix.split()) to remove whitespace

test 3
========================== short test summary info ==========================
FAILED main.py::test_name_fix[dR. JoHn SmiTH, Md-John Smith] - AssertionError: assert 'JoHn SmiTH' == 'John Smith'
FAILED main.py::test_name_fix[jACqUeLINE jORdaN-Jacqueline Jordan] - AssertionError: assert 'jACqUeLINE jORdaN' == 'Jacqueline Jordan'
FAILED main.py::test_name_fix[DR. LaUreN ClaRk DDs-Lauren Clark] - AssertionError: assert 'LaUreN ClaRk' == 'Lauren Clark'
FAILED main.py::test_name_fix[   robiN   coX   -Robin Cox] - AssertionError: assert 'robiN coX' == 'Robin Cox'
======================== 4 failed, 2 passed in 0.10s ========================

problem: function doesnt correct capitalisation
fix: moved capitalisation logic from open_csv() to name_fix() as it makes more sense for it to be in this function

============================ test session starts ============================
platform win32 -- Python 3.15.2, pytest-9.2.0, pluggy-1.7.0
rootdir: C:\Users\light\Documents\GitHub Repos\CPS4003-Assessment2
collected 6 items                                                            

main.py ......                                                         [100%]

============================= 6 passed in 0.03s =============================

Decided to change regex regarding suffixes as realised that professional suffixes (md, dds, etc) wouldnt particularly matter for patients as it is more important to get the patients name correct than to preserve their titles. Suffixes like Jr and Sr are kept as they are used to differentiate between different people

moved the pytests to a dedicated testing python file to declutter main.py

Traceback (most recent call last):
  File "c:\Users\light\Documents\GitHub Repos\CPS4003-Assessment2\main.py", line 48, in <module>
    open_csv(csvfile)
    ~~~~~~~~^^^^^^^^^
  File "c:\Users\light\Documents\GitHub Repos\CPS4003-Assessment2\main.py", line 42, in open_csv
    row["Billing Amount"] = float(row["Billing Amount"].strip("£"))
                            ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: could not convert string to float: '18,856.28'

Problem: trying to remove £ and commas from string to convert it into float but running into errors.
Fix: used replace() to remove the comma

A negative value was found in the "Billing Amount" column of the dataset. A decision was made to log the negative value and skip it since it would skew any analysis run on the dataset. A new file "data_cleaning_log" will be created and updated on each run of open_csv() file detailing what rows are skipped so any other rows with the same error are accounted for automatically

Decided to change the strip() in the "billing amount" column to replace() as strip() only removes from outer edges of string, so symbols like "-" can stop others from being stripped

Decided to standardise billing amounts to two decimal places to avoid floating point errors and to align more with standard financial practices