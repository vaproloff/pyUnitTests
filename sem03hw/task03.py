import unittest


# Задание 3.
# Добавьте функцию в класс UserRepository, которая разлогинивает всех пользователей, кроме администраторов.
# Для этого вам потребуется расширить класс User новым свойством,
# указывающим, обладает ли пользователь админскими правами.
# Протестируйте данную функцию.


class User:
    def __init__(self, name: str, password: str, is_admin: bool) -> None:
        self.name = name
        self.password = password
        self.is_admin = is_admin
        self.is_authenticated = False

    def authenticate(self, name: str, password: str) -> bool:
        return False


class UserRepository:
    def __init__(self) -> None:
        self.data: list[User] = []

    def add_user(self, user: User):
        self.data.append(user)

    def find_by_name(self, username: str) -> bool:
        for user in self.data:
            if user.name == username:
                return True
        return False

    def logout_users(self):
        for user in self.data:
            if not user.is_admin:
                self.data.remove(user)


class TestUserRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.user_repository = UserRepository()
        self.user_1 = User('Name_1', 'Password_1', False)
        self.user_2 = User('Name_2', 'Password_2', True)
        self.user_3 = User('Name_3', 'Password_3', False)
        self.user_repository.add_user(self.user_1)
        self.user_repository.add_user(self.user_2)
        self.user_repository.add_user(self.user_3)

    def tearDown(self) -> None:
        self.user_repository = None
        self.user_1 = None
        self.user_2 = None
        self.user_3 = None

    def test_find_user_by_name(self):
        """Проверка поиска пользователей по именам"""
        for user in [self.user_1, self.user_2, self.user_3]:
            with self.subTest(user=user):
                self.assertTrue(self.user_repository.find_by_name(user.name))

    def test_find_user_by_name_fail(self):
        """Проверка поиска пользователей по несуществующему имени"""
        self.assertFalse(self.user_repository.find_by_name("Noname"))

    def test_logout_all(self):
        """Проверка разлогинивания всех пользователей кроме админов"""
        self.user_repository.logout_users()

        self.assertListEqual(self.user_repository.data, [self.user_2])
