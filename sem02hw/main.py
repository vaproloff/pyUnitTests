import unittest

from sem02hw.abstract_vehicle import Vehicle
from sem02hw.car import Car
from sem02hw.motorcycle import Motorcycle

"""
Домашнее задание к семинару №2 JUnit:
    1. Настроить новый проект:
        a) Нужно создать новый проект, со следующей структурой классов (3 отдельных класса):

        b) Настроить тестовую среду
            (создать тестовый класс VehicleTest, пометить папку как Test sources (зеленая папка),
            импортировать необходимые для тестов библиотеки (JUnit, assertJ - все что было на семинаре))

        c) Написать следующие тесты:
            - проверка того, что экземпляр объекта Car также является экземпляром транспортного средства; (instanceof)
            - проверка того, объект Car создается с 4-мя колесами
            - проверка того, объект Motorcycle создается с 2-мя колесами
            - проверка того, объект Car развивает скорость 60 в режиме тестового вождения (testDrive())
            - проверка того, объект Motorcycle развивает скорость 75 в режиме тестового вождения (testDrive())
            - проверить, что в режиме парковки (сначала testDrive, потом park, т.е эмуляция движения транспорта)
              машина останавливается (speed = 0)
            - проверить, что в режиме парковки (сначала testDrive, потом park, т.е эмуляция движения транспорта)
              мотоцикл останавливается (speed = 0)
"""


class TestCar(unittest.TestCase):

    def setUp(self) -> None:
        self.car = Car('Lotus', 'Elise', 2005)

    def tearDown(self) -> None:
        self.car = None

    def test_instance_of(self):
        """Тест на наследование"""
        self.assertTrue(isinstance(self.car, Vehicle))

    def test_wheels(self):
        """Тест количества колёс"""
        self.assertEqual(self.car.num_wheels, 4)

    def test_drive(self):
        """Тест скорости тестового вождения"""
        self.assertEqual(self.car.speed, 0)
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60)

    def test_park(self):
        """Тест остановки"""
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0)


class TestMotorcycle(unittest.TestCase):

    def setUp(self) -> None:
        self.motorcycle = Motorcycle('Harley-Davidson', 'Sportster', 2021)

    def tearDown(self) -> None:
        self.motorcycle = None

    def test_instance_of(self):
        """Тест на наследование"""
        self.assertTrue(isinstance(self.motorcycle, Vehicle))

    def test_wheels(self):
        """Тест количества колёс"""
        self.assertEqual(self.motorcycle.num_wheels, 2)

    def test_drive(self):
        """Тест скорости тестового вождения"""
        self.assertEqual(self.motorcycle.speed, 0)
        self.motorcycle.test_drive()
        self.assertEqual(self.motorcycle.speed, 75)

    def test_park(self):
        """Тест остановки"""
        self.motorcycle.test_drive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
