"""List Averages Comparison"""


class ListComparison:
    """Calculate averages of two lists and compare them."""

    def __init__(self, list_1: list[int], list_2: list[int]) -> None:
        self.list_1 = list_1
        self.list_2 = list_2
        self._avg_1 = None
        self._avg_2 = None

    @property
    def avg_1(self) -> float | None:
        """Return the average of the first list"""
        if self._avg_1 is None and self.list_1:
            self._avg_1 = sum(self.list_1) / len(self.list_1)
        return self._avg_1

    @property
    def avg_2(self) -> float | None:
        """Return the average of the second list"""
        if self._avg_2 is None and self.list_2:
            self._avg_2 = sum(self.list_2) / len(self.list_2)
        return self._avg_2

    def avg_compare(self) -> str:
        """Compare averages of two lists"""
        if None in (self.avg_1, self.avg_2):
            raise ValueError("Сравнение невозможно, когда один из списков пуст")
        if self.avg_1 > self.avg_2:
            return "Первый список имеет большее среднее значение"
        if self.avg_2 > self.avg_1:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
