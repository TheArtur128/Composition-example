from src.config import di


def logic(user_id: di.UserID) -> di.AuthorizedUser:
    return di.authorized(di.registered(di.user_of(user_id)))
