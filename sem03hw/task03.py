import unittest


# Задание 3.
# Добавьте функцию в класс UserRepository, которая разлогинивает всех пользователей, кроме администраторов.
# Для этого вам потребуется расширить класс User новым свойством,
# указывающим, обладает ли пользователь админскими правами.
# Протестируйте данную функцию.


class User:
    def __init__(self, name: str, password: str, is_admin: bool = False) -> None:
        self.name = name
        self.password = password
        self.is_admin = is_admin

        self.is_authenticated = False

    def authenticate(self, name: str, password: str) -> bool:
        if not self.is_authenticated:
            self.is_authenticated = self.name == name and self.password == password
        return self.is_authenticated

    def logout(self) -> None:
        self.is_authenticated = False


class UserRepository:
    def __init__(self) -> None:
        self.users: list[User] = []

    def add_user(self, user: User):
        self.users.append(user)

    def find_by_name(self, username: str) -> User | None:
        for user in self.users:
            if user.name == username:
                return user

    def logout_all(self):
        for user in self.users:
            if not user.is_admin:
                user.logout()


class TestUserRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.user_repository = UserRepository()
        self.user_1 = User('Name_1', 'Password_1')
        self.user_2 = User('Name_2', 'Password_2', True)
        self.user_3 = User('Name_3', 'Password_3')

    def tearDown(self) -> None:
        self.user_repository = None
        self.user_1 = None
        self.user_2 = None
        self.user_3 = None

    def test_add_user(self):
        """Проверка добавления пользователей"""
        self.user_repository.add_user(self.user_1)
        self.user_repository.add_user(self.user_2)
        self.user_repository.add_user(self.user_3)

        self.assertListEqual(self.user_repository.users, [self.user_1, self.user_2, self.user_3])

    def test_find_user_by_name(self):
        """Проверка поиска пользователей по именам"""
        self.user_repository.add_user(self.user_1)
        self.user_repository.add_user(self.user_2)
        self.user_repository.add_user(self.user_3)

        for user in [self.user_1, self.user_2, self.user_3]:
            with self.subTest(user=user):
                self.assertTrue(self.user_repository.find_by_name(user.name))

    def test_find_user_by_name_fail(self):
        """Проверка поиска пользователей по несуществующему имени"""
        self.user_repository.add_user(self.user_1)

        self.assertFalse(self.user_repository.find_by_name("Noname"))

    def test_logout_all(self):
        """Проверка разлогинивания всех пользователей кроме админов"""
        self.user_repository.add_user(self.user_1)
        self.user_1.authenticate('Name_1', 'Password_1')

        self.user_repository.add_user(self.user_2)
        self.user_2.authenticate('Name_2', 'Password_2')

        self.user_repository.add_user(self.user_3)
        self.user_3.authenticate('Name_3', 'Password_3')

        self.user_repository.logout_all()

        for user in self.user_repository.users:
            with self.subTest(user=user):
                self.assertTrue(user.is_admin == user.is_authenticated)
