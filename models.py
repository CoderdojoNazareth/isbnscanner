class Book:
    def __init__(self, isbn, auteur, titel, plaatsing_omschrijving, **kwargs):
        self.isbn = isbn
        self.auteur = auteur
        self.titel = titel
        self.plaatsing_omschrijving = plaatsing_omschrijving
        # Store any additional fields
        for k, v in kwargs.items():
            setattr(self, str(k).lower(), v)

    def __repr__(self):
        return f"<Book ISBN: {self.isbn}, Auteur: {self.auteur}, Title: {self.titel}, Plaatsing omschrijving: {self.plaatsing_omschrijving}>"
