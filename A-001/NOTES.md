## Predict-then-run
# 1
Prediction: It will create function add_one and when I run print(add_one(2)) I would see 3.
Actual: I saw None.
Why: Cause in function there is not 'return' word or something that it do out of function.

# 2
Prediction: I don't what function isdigit() do but i think it will be False, True, False.
Actual: False, True, False
Why: I think this function show True if its number and false if not.

# 3
Prediction: I think it will show "Delta Auto" including the spaces in the middle.
Actual: "Delta Auto"
Why: Couse strip delete spaces only on the ends of the string.

# 4
Prediction: It will show None. It will show KeyError: 'phone'.
Actual: None, KeyError: 'phone'.
Why: I see KeyError cause element 'phone' is not exist in dict d. I see None cause get() method show None if element is not exist in dict.

# 5
Prediction: It will show 2, True, False.
Actual: 1 True False
Why: I forget that sets "is an unordered collection with no duplicate elements", so ("acme", "") element was added only once. The two others I was right. I saw True cause ("acme", "") is in set, and ("Acme", "") is not in set.

# 6
Prediction: It will dive 3 parts. And other one will give 2 fields for the same line.
Actual: 
['"Fox & Sons', ' Movers"', 'Tulsa']
['name', 'city']
['Fox & Sons, Movers', 'Tulsa']
Why: I was right. First .split(",") is understanding all "," as delimiter even in "". Reader understand that "Fox & Sons, Movers" is one.

# 7
Prediction: First it will be
1 
2 None
Second will be
11
22
Actual:
1
2 None

&

11
22
Why: Cause in first script there is comma in second line what created two fields "1" and "". In third line there are not comma so it see onle first element "2" and "If a non-blank row has fewer fields than fieldnames, the missing values are filled-in with the value of restval (which defaults to None)". In the second experiment we didn't format string values "1" and "2" so string+string = stringstring.

# 8
Prediction: It prints all python versions on PC. After activation it will show only one 3.14.10. After deactivation again all python versions on PC.
Actual:
/Library/Frameworks/Python.framework/Versions/3.14/bin/python3
/Users/ivankyrylko/mentor-lab/work/s1/.venv/bin/python
python not found
Why: It showed where python on PC. First should show folder on PC. Second showed folder in virtual environment. Last showed that python (not pyhton3) is not found. 

## My test file
2 None
3 (a)
4 (b)
5 None
6 (c)
7 (d)
8 (e)
9 (f)
10 (g)
11 (h)

Rows in: 10
Duplicates removed: 2
Rows out: 2
Blank phones: 2
Phones not normalised: 1

## AI use
none

## Time
