from todo_logic import clear_all, is_duplicate


def test_is_duplicate_exact_duplicate():
    assert is_duplicate("Buy milk", ["Buy milk"])


def test_is_duplicate_with_different_case_and_spaces():
    assert is_duplicate("  buy MILK  ", ["Buy milk"])


def test_is_duplicate_non_duplicate():
    assert not is_duplicate("Buy eggs", ["Buy milk"])


def test_clear_all_returns_empty_list():
    assert clear_all(["Buy milk", "Buy eggs"]) == []
