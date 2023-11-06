from src import orm, types_


def user_of(email: types_.Email) -> orm.User:
    ...


def register(user: orm.User) -> None:
    ...


def authorize(user: orm.User) -> None:
    ...
