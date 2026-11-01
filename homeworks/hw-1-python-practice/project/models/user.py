import uuid


class User:
    def __init__(self, name: str) -> None:
        self.id = uuid.uuid4()
        self.name = name
        self.comments_count = 0
        self.rate = 0
        self.is_banned = False

    def edit_name(self, new_name: str) -> None:
        self.name = new_name

    def increment_rate(self) -> None:
        self.rate += 1

    def ban_user(self) -> None:
        self.is_banned = True

    def unban_user(self) -> None:
        self.is_banned = False

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, rate={self.rate}, banned={self.is_banned})"
