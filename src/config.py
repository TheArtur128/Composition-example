from act import val, io

from typing import Type, Any, Callable

from src import orm, periphery, types_


# Если тип аннотирован через _ToUpcast,
# то при аннотации этим типом какого нибудь ресурса
# будет сокрыто все публичное поведение этого ресурса (апкастен до Any)
# (Как минимум логично такое поведение, я пока не проверял на тайпчекерах).
type _ToUpcast = Type[Any]


@val
class di:
    type _User = orm.User

    UserID: _ToUpcast = types_.Email

    User: _ToUpcast = orm.User
    RegisteredUser: _ToUpcast = _User
    AuthorizedUser: _ToUpcast = _User

    user_of: Callable[UserID, AuthorizedUser] = periphery.user_of
    registered: Callable[User, RegisteredUser] = io(periphery.register)
    authorized: Callable[RegisteredUser, AuthorizedUser] = io(periphery.authorize)
