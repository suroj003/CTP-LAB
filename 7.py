class LibraryItem:
    def __init__(self, name):
        self.name = name
        self.issued = False

    def issue(self):
        if self.issued:
            print(self.name, "already issued")
        else:
            self.issued = True
            print(self.name, "issued")

    def return_item(self):
        if self.issued:
            self.issued = False
            print(self.name, "returned")
        else:
            print(self.name, "was not issued")


class Book(LibraryItem):
    def show(self):
        print("Book:", self.name)


class Magazine(LibraryItem):
    def show(self):
        print("Magazine:", self.name)


class Journal(LibraryItem):
    def show(self):
        print("Journal:", self.name)


book = Book("Python Programming")
magazine = Magazine("Science Today")
journal = Journal("AI Research Journal")

items = [book, magazine, journal]

for obj in items:
    obj.show()

print("\nIssue operations:")
book.issue()
magazine.issue()

print("\nReturn operations:")
book.return_item()
magazine.return_item()
journal.return_item()