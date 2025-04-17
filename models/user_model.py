class User:
    def __init__(self, username, profile_pic):
        self.username = username
        self.profile_pic = profile_pic

    def __repr__(self):
        return f"User(username={self.username}, profile_pic={self.profile_pic})"
