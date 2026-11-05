# S1

## A-001: clean_companies.py

**Python 3.14**

- **[clean_companies.py](A-001/clean_companies.py)** - Program that delivers a deduplicated CSV with blanks left blank, normalised phones, a source URL on every row and a QA count.

### The cleaning rules
- Columns in: `name`, `phone`, `city`, `source_url`, in this order.
- Columns out: `name`, `phone`, `city`, `source_url`, `sources`, in this order.
- **Name**: remove spaces at both ends, and replace every run of two or more spaces inside with one space. Keep the letter case.
- **Phone**:
	- Remove spaces at both ends. If nothing is left, the phone is blank: return ''.
	- Take only the digit characters 0–9, in order.
	- If there are exactly 10 digits, the result is +1 followed by the 10 digits.
	- If there are exactly 11 digits and the first one is 1, the result is + followed by the 11 digits.
	- Otherwise, return the text from rule 1 unchanged. Do not guess and do not invent digits. This phone counts as "not normalised".
- **City**, **source_url**: remove spaces at both ends. A blank value stays blank. Never fill a blank.
- **Sources**: the number of input rows in the row's duplicate group, the kept row included, as a whole number (1, 2, 3 …). A row with no duplicates has 1.
- **Duplicates**: two rows are duplicates when their cleaned names, compared in lowercase, are equal and their cleaned phones are equal. A blank phone is a phone value too: two rows with the same name and both phones blank are duplicates. Keep the first row of each group, exactly as cleaned, and drop the later ones. Output rows stay in input order.
- **QA summary**: the script prints exactly these 6 lines and nothing else:
```bash
Rows in: 12
Duplicates removed: 4
Rows out: 8
Blank phones: 1
Phones not normalised: 2
Confirmed in 2+ sources: 4
```

## Getting Started
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

python3 "A-001/clean_companies.py" ./A-001/companies_raw.csv ./A-001/companies_clean.csv
```