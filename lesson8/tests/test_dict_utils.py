from lesson8.dictionary_util import dict2list


def test1():
    d = {
        'Science': [88, 89, 62, 95],
        'Language': [77, 78, 84, 80]
    }
    expected_val = \
        [{'Science': 88, 'Language': 77},
        {'Science': 89, 'Language': 78},
        {'Science': 62, 'Language': 84},
        {'Science': 95, 'Language': 80}]

    ret_val = dict2list(d)

    assert type(ret_val) == list
    assert ret_val == expected_val, \
        f"Returned value not as expected: \n" \
        f"Expected: {expected_val}\n" \
        f"Received: {ret_val}"


def test_empty_values():
    ret_val = dict2list({})
    assert ret_val == []
