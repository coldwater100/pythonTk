import tkinter as tk
from PIL import Image, ImageTk

class ListBookFrame(tk.Frame):
    def __init__(self, master, book_list, **kwargs):
        super().__init__(master, **kwargs)
        self.book_list = book_list
        self.create_widgets()

    def create_widgets(self):
        title_frame = tk.Frame(self, bg='blue')
        title_frame.pack(pady=10, fill=tk.X)
        title_label = tk.Label(title_frame, text="List of Books", font=("Helvetica", 16, "bold"), bg='blue', fg='white')
        title_label.pack(padx=10, pady=10)

        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.canvas.xview, width=60)  # 스크롤바 크기 조정
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        self.book_frame = tk.Frame(self.canvas, bg='white')
        self.canvas.create_window((0, 0), window=self.book_frame, anchor='nw')

        self.book_frame.bind("<Configure>", self.on_frame_configure)

        self.update_book_list(self.book_list)

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def update_book_list(self, new_book_list):
        for widget in self.book_frame.winfo_children():
            widget.destroy()

        self.book_list = new_book_list

        if not self.book_list:
            no_books_label = tk.Label(self.book_frame, text="No books available.", font=("Helvetica", 12), bg='white')
            no_books_label.pack(fill=tk.X, padx=10, pady=5)
        else:
            for idx, (title, author, pages, genres, cover_path) in enumerate(self.book_list, start=1):
                book_frame = tk.Frame(self.book_frame, padx=10, pady=5, relief=tk.RIDGE, borderwidth=2, bg='white')
                book_frame.pack(side=tk.LEFT, padx=10, pady=5)

                cover_image = Image.open(cover_path)
                cover_image = cover_image.resize((100, 150), Image.LANCZOS)
                cover_photo = ImageTk.PhotoImage(cover_image)

                cover_label = tk.Label(book_frame, image=cover_photo, bg='white')
                cover_label.image = cover_photo
                cover_label.pack()

                title_frame = tk.Frame(book_frame, bg='lightgray', relief=tk.RIDGE, borderwidth=1)
                title_frame.pack(fill=tk.X)
                title_label = tk.Label(title_frame, text=title, font=("Helvetica", 12), cursor="hand2", bg='lightgray')
                title_label.pack(padx=5, pady=5)

                title_label.bind("<Button-1>", lambda e, t=title, a=author, p=pages, g=genres: self.show_book_details(t, a, p, g))

    def show_book_details(self, title, author, pages, genres):
        details_window = tk.Toplevel(self)
        details_window.title(f"Details of {title}")

        details_label = tk.Label(details_window, text=f"Title: {title}\nAuthor: {author}\nPages: {pages}\nGenres: {genres}", font=("Helvetica", 12))
        details_label.pack(padx=10, pady=10)

