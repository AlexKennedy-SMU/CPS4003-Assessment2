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
