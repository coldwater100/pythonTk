import tkinter as tk
from tkinter import messagebox

###################################################
# 새로운 책을 book_list에 추가하는 Class
# add_book_callback 함수(add_book in main.py)를 수정하고 싶으면 팀장에게 문의
# 이 파일 외에 다른 파일의 내용은 절대 수정하지 말고, 수정 원하면 팀장에 문의
###################################################

class AddBookFrame(tk.Frame):
    def __init__(self, master, add_book_callback, **kwargs):
        super().__init__(master, **kwargs)
        self.add_book_callback = add_book_callback

        self.create_widgets()

    def create_widgets(self):
        # title 입력을 위한 label, entry
        title_label = tk.Label(self, text="Title:")
        title_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.title_entry = tk.Entry(self)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

        # author 입력을 위한 label, entry
        author_label = tk.Label(self, text="Author:")
        author_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.author_entry = tk.Entry(self)
        self.author_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

        # pages 입력을 위한 label, entry
        pages_label = tk.Label(self, text="Pages:")
        pages_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.pages_entry = tk.Entry(self)
        self.pages_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")

        # Button - add book
        add_button = tk.Button(self, text="Add Book", command=self.add_book)
        add_button.grid(row=3, columnspan=2, pady=10)

    def add_book(self):
        # entry에서 각각의 value를 가져옴
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        pages = self.pages_entry.get().strip()

        # 입력의 값을 validation
        if title and author and pages.isdigit():
            # Convert pages to integer
            pages = int(pages)
            
            # book list에 새책(new_book)을 추가, main.py에서 넘어온 callback 함수를 이용 추가한다.
            new_book = (title, author, pages)
            self.add_book_callback(new_book)

            # entry fields 초기화
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
            self.pages_entry.delete(0, tk.END)
        else:
            # 형식에 맞지 않거나 pages 에 숫자가 아니면 오류 메시지
            messagebox.showerror("오류", "유효한 값을 다시 입력하세요.")



