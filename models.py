class Book:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"<Book ISBN: {self.isbn}, Title: {self.titel}>"
