class User:
    count = 0

    def __init__(self, name, login, password, grade):
        self._name = name
        self._login = login
        self._password = password
        self._grade = grade
        if type(self) == User:
            User.count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, _):
        print("Невозможно изменить логин!")

    @property
    def grade(self):
        return "Неизвестное свойство grade"

    @grade.setter
    def grade(self, _):
        print("Неизвестное свойство grade")

    @property
    def password(self):
        # return "*" * len(self._password)
        return "********"

    @password.setter
    def password(self, value):
        self._password = value

    def show_info(self):
        print(f"Name: {self._name}, Login: {self._login}")

    def __lt__(self, other):
        return self._grade < other._grade

    def __eq__(self, other):
        return self._grade == other._grade


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role, grade):
        super().__init__(name, login, password, grade)
        self._role = role
        if type(self) == SuperUser:
            SuperUser.count += 1

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value


user1 = User("Paul McCartney", "paul", "1234", 3)
user2 = User("George Harrison", "george", "5678", 2)
user3 = User("Richard Starkey", "ringo", "8523", 3)
admin = SuperUser("John Lennon", "john", "0000", "admin", 5)

user1.show_info()
admin.show_info()

users = User.count
admins = SuperUser.count

print(f"Всего обычных пользователей: {users}")
print(f"Всего супер-пользователей: {admins}")

print(user1 < user2)
print(admin > user3)
print(user1 == user3)

user3.name = "Ringo Starr"
user1.password = "Pa$$w0rd"

print(user3.name)
print(user2.password)
print(user2.login)

user2.login = "geo"

print(user1.grade)
admin.grade = 10