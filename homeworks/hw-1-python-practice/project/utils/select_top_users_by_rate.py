from models.user import User

def select_top_users_by_rate(users: list[User], top_size: int) -> list[User]:
    return sorted(users, key=lambda u: u.rate, reverse=True)[:top_size]
