class Image:
    def __init__(self, name, url, public_id):
        self.name = name
        self.url = url
        self.public_id = public_id

    def __repr__(self):
        return f"Image(name={self.name}, url={self.url}, public_id={self.public_id})"
