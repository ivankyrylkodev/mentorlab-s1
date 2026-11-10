import re
import csv
import sys

def normalize_name(text):
    return ' '.join(text.split())

def normalize_phone(text):
    result = re.sub(r'\D', '', text)
    if len(result) == 10:
        return f"+1{result}"
    elif len(result) == 11 and result.startswith('1'):
        return f"+{result}"
    else:
        return text.strip()

def clean_row(row):
    return {
        "name": normalize_name(row["name"]),
        "phone": normalize_phone(row["phone"]),
        "city": row["city"].strip(),
        "source_url": row["source_url"].strip(),
        "sources": 1
    }


def  check_row(row):
    if row["name"] is None or row["phone"] is None or row["city"] is None or row["source_url"] is None:
        return 'short row'
    elif row["name"].strip() == '':
        return 'blank name'
    elif row["source_url"].strip() == '':
        return 'blank source_url'
    else:
        return ''

def dedupe(rows):
    result = []
    add = False
    for row in rows:
        if len(result) == 0:
            result.append(dict(row))
        else:
            for r in result:
                if row["name"].lower() == r["name"].lower() and row["phone"] == r["phone"]:
                    r["sources"] += 1
                    add = False
                    break
                else:
                    add = True
            if add:
                result.append(dict(row))
    return result

def read_rows(path):
    result = []
    with open(path,  newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            result.append(clean_row(row))
    return dedupe(result)

def write_rows(path, rows):
    with open(path, mode='w', newline='', encoding='utf-8') as f:
        fieldnames = [ "name", "phone", "city", "source_url",  "sources"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in rows:
             writer.writerow({"name": row["name"], "phone": row["phone"], "city": row["city"], "source_url": row["source_url"],  "sources": row["sources"]})


def main():
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    file = read_rows(input_path)
    write_rows(output_path, file)
    rows_in = 0
    rows_out = 0
    blank_phones = 0
    phones_not_normalized = 0
    more_sources = 0
    with open(input_path, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows_in += 1

    with open(output_path, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows_out += 1
                if row['phone'] == '':
                    blank_phones += 1
                elif not row["phone"].startswith('+1') or not len(re.sub(r'\D', '', row["phone"])) == 11:
                    phones_not_normalized += 1
                if int(row["sources"]) > 1:
                    more_sources += 1
    print(f"Rows in: {rows_in}")
    print(f"Duplicates removed: {rows_in - rows_out}")
    print(f"Rows out: {rows_out}")
    print(f"Blank phones: {blank_phones}")
    print(f"Phones not normalised: {phones_not_normalized}")
    print(f"Confirmed in 2+ sources: {more_sources}")




if __name__ == "__main__":
    main()