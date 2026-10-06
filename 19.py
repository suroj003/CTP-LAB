import sqlite3
import tkinter as tk
from tkinter import messagebox


class Library:
    def __init__(self):
        self.con = sqlite3.connect("library.db")
        self.cur = self.con.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY,
            name TEXT,
            author TEXT,
            status TEXT
        )
        """)

        self.con.commit()

        self.root = tk.Tk()
        self.root.title("Library Management")
        self.root.geometry("400x450")

        tk.Label(self.root, text="Book ID").pack()
        self.id_box = tk.Entry(self.root)
        self.id_box.pack()

        tk.Label(self.root, text="Book Name").pack()
        self.name_box = tk.Entry(self.root)
        self.name_box.pack()

        tk.Label(self.root, text="Author").pack()
        self.author_box = tk.Entry(self.root)
        self.author_box.pack()

        tk.Button(
            self.root,
            text="Add Book",
            command=self.add
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Issue Book",
            command=self.issue
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Return Book",
            command=self.return_book
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Search Book",
            command=self.search
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Show All",
            command=self.show
        ).pack(pady=5)

        self.result = tk.Text(self.root, height=10, width=45)
        self.result.pack(pady=10)

        self.root.mainloop()

    def add(self):
        bid = int(self.id_box.get())
        name = self.name_box.get()
        author = self.author_box.get()

        self.cur.execute(
            "INSERT INTO books VALUES (?, ?, ?, ?)",
            (bid, name, author, "Available")
        )

        self.con.commit()
        messagebox.showinfo("Message", "Book added")

    def issue(self):
        bid = int(self.id_box.get())

        self.cur.execute(
            "UPDATE books SET status = 'Issued' WHERE id = ?",
            (bid,)
        )

        self.con.commit()
        messagebox.showinfo("Message", "Book issued")

    def return_book(self):
        bid = int(self.id_box.get())

        self.cur.execute(
            "UPDATE books SET status = 'Available' WHERE id = ?",
            (bid,)
        )

        self.con.commit()
        messagebox.showinfo("Message", "Book returned")

    def search(self):
        bid = int(self.id_box.get())

        self.cur.execute(
            "SELECT * FROM books WHERE id = ?",
            (bid,)
        )

        data = self.cur.fetchone()

        self.result.delete("1.0", tk.END)

        if data:
            self.result.insert(tk.END, str(data))
        else:
            self.result.insert(tk.END, "Book not found")

    def show(self):
        self.cur.execute("SELECT * FROM books")

        data = self.cur.fetchall()

        self.result.delete("1.0", tk.END)

        for book in data:
            self.result.insert(tk.END, str(book) + "\n")


obj = Library()