from models.comment import Comment
from models.user import User

def filter_comments_by_author(comments: list[Comment], author: User) -> list[Comment]:
    return [c for c in comments if c.author_id == author.id]
