class Book:
    def __init__(self, isbn, auteur, titel, plaats, **kwargs):
        self.isbn = isbn
        self.auteur = auteur
        self.titel = titel
        self.plaats = plaats
        # Store any additional fields
        for k, v in kwargs.items():
            setattr(self, str(k).lower(), v)

    def __repr__(self):
        return f"<Book ISBN: {self.isbn}, Auteur: {self.auteur}, Title: {self.titel}, Plaats: {self.plaats}>"
