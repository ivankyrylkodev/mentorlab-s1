import re

def normalize_name(text):
    return text.strip().replace("  ", ' ').title()

def normalize_phone(text):
    result = re.sub(r'\D', '', text)
    if len(result) == 10:
        return f"+1{result}"
    elif len(result) == 11 and result.startswith('1'):
        return f"+{result}"
    else:
        return text.strip()