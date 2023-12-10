import pytest
from lists_averages import ListComparison


@pytest.fixture
def small_list():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def big_list():
    return [90, 100, 110, 120]


@pytest.fixture
def empty_list():
    return []


@pytest.fixture
def comparison_instance_lt(small_list, big_list):
    return ListComparison(small_list, big_list)


@pytest.fixture
def comparison_instance_gt(small_list, big_list):
    return ListComparison(big_list, small_list)


@pytest.fixture
def comparison_instance_eq(small_list):
    return ListComparison(small_list, list(reversed(small_list)))


@pytest.fixture
def comparison_instance_empty(small_list, empty_list):
    return ListComparison(small_list, empty_list)


def test_avg_1(comparison_instance_lt):
    assert comparison_instance_lt.avg_1 == 3, "Среднее значение первого списка должно быть равно 3"


def test_avg_2(comparison_instance_lt):
    assert comparison_instance_lt.avg_2 == 105, "Среднее значение второго списка должно быть равно 8"


def test_avg_compare_lt(comparison_instance_lt):
    assert comparison_instance_lt.avg_compare() == "Второй список имеет большее среднее значение", \
        "Проверка сравнения двух списков, когда среднее второго больше"


def test_avg_compare_gt(comparison_instance_gt):
    assert comparison_instance_gt.avg_compare() == "Первый список имеет большее среднее значение", \
        "Проверка сравнения двух списков, когда среднее первого больше"


def test_avg_compare_eq(comparison_instance_eq):
    assert comparison_instance_eq.avg_compare() == "Средние значения равны", \
        "Проверка сравнения двух списков, когда средние списков равны"


def test_avg_compare_empty(comparison_instance_empty):
    with pytest.raises(ValueError):
        comparison_instance_empty.avg_compare()


if __name__ == '__main__':
    pytest.main(['-v'])
