from app import add, is_tee_time_available


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_is_tee_time_available():
    assert is_tee_time_available(["9:00", "9:30", "10:00"], "9:30") is True
    assert is_tee_time_available(["9:00", "9:30", "10:00"], "11:00") is False
