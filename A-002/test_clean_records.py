import clean_records as cr

def test_normalize_phone():
    assert cr.normalize_phone("") == ""
    assert cr.normalize_phone("4443214583") == "+14443214583"
    assert cr.normalize_phone("12948562058") == "+12948562058"
    assert cr.normalize_phone("49034935034") == "49034935034"


def test_normalize_name():
    assert cr.normalize_name("danzel    waggs") == "danzel waggs"
    assert cr.normalize_name(" Samanta inks  ") == "Samanta inks"

test_dict = [{"name": "Ike Studios","phone": "+15550180000","city": "Santa Clarita","source_url": "<https://example.com/dir?page=3>", "sources": 1},
             {"name": "Ike Studios","phone": "+15550180000","city": "Santa Clarita","source_url": "<https://example.com/dir?page=3>", "sources": 1},
             {"name": "Ike Plumbing","phone": "","city": "Abilene","source_url": "<https://example.com/dir?page=4>", "sources": 1}]

def test_dedupe_duplicate():
    assert cr.dedupe(test_dict) == [{"name": "Ike Studios","phone": "+15550180000","city": "Santa Clarita","source_url": "<https://example.com/dir?page=3>", "sources": 2},
                                    {"name": "Ike Plumbing","phone": "","city": "Abilene","source_url": "<https://example.com/dir?page=4>", "sources": 1}]

def test_dedupe_unchanged():
    new_dict = cr.dedupe(test_dict)
    assert test_dict == [{"name": "Ike Studios","phone": "+15550180000","city": "Santa Clarita","source_url": "<https://example.com/dir?page=3>", "sources": 1},
                         {"name": "Ike Studios","phone": "+15550180000","city": "Santa Clarita","source_url": "<https://example.com/dir?page=3>", "sources": 1},
                         {"name": "Ike Plumbing","phone": "","city": "Abilene","source_url": "<https://example.com/dir?page=4>", "sources": 1}]

    assert cr.dedupe(test_dict)  == [{"name": "Ike Studios","phone": "+15550180000","city": "Santa Clarita","source_url": "<https://example.com/dir?page=3>", "sources": 2},
                                     {"name": "Ike Plumbing","phone": "","city": "Abilene","source_url": "<https://example.com/dir?page=4>", "sources": 1}]

def test_check_row():
    assert cr.check_row({"name": "Ike Studios","phone": "+15550180000","city": "Santa Clarita","source_url": "<https://example.com/dir?page=3>"}) == ''
    assert cr.check_row({"name": "Ike Studios","phone": "+15550180000","city": "Santa Clarita","source_url": None}) == 'short row'
    assert cr.check_row({"name": "    ","phone": "+15550180000","city": "Santa Clarita","source_url": "<https://example.com/dir?page=3>"}) == 'blank name'
    assert cr.check_row({"name": "Ike Studios","phone": "+15550180000","city": "Santa Clarita","source_url": " "}) == 'blank source_url'
    cr.check_row({"name": "", "phone": "+15550180000", "city": None, "source_url": "https://example.com"}) == 'short row'