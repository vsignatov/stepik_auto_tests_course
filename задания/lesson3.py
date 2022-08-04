def test_substring(full_string, substring):
    assert substring in full_string , f"expected 'some_value' to be substring of 'fulltext'"


test_substring ("каждый", "жак")
