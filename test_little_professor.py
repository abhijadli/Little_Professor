import professor_x


def test_generate_integer():
    assert 0 <= professor_x.generate_integer(1) <= 9
    assert 10 <= professor_x.generate_integer(2) <= 99
    assert 100 <= professor_x.generate_integer(3) <= 999


def test_get_operator():
    operators = ["+", "-", "/", "*"]
    assert professor_x.get_operator() in operators


def test_calculate_result():
    assert professor_x.calculate_result(2, 3, "+") == 5
    assert professor_x.calculate_result(8, 4, "-") == 4
    assert professor_x.calculate_result(6, 7, "*") == 42
    assert professor_x.calculate_result(10, 2, "/") == 5
