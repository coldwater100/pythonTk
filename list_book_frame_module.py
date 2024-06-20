import tkinter as tk

###################################################
# book_list의 내용을 display해주는 Class
# book_list의 구조는 main.py를 참고하세요
# 이 파일 외에 다른 파일의 내용은 절대 수정하지 말고, 수정 원하면 팀장에 문의
###################################################

class ListBookFrame(tk.Frame):
    def __init__(self, master, book_list, **kwargs):
        super().__init__(master, **kwargs)
        #넘어온 book_list를 self.book_list에 저장해 놓음
        self.book_list = book_list
        #내용 표시를 위한 위젯들 생성
        self.create_widgets()

    #내용 표시를 위한 위젯들 생성
    def create_widgets(self):
        # title label
        title_label = tk.Label(self, text="List of Books", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # book list를 display할 frame 생성
        self.book_frame = tk.Frame(self)
        self.book_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        # booklist의 내용을 표시
        self.update_book_list(self.book_list)

    # booklist의 내용을 표시
    def update_book_list(self, new_book_list):
        # 현재 있는 widget을 없애고
        for widget in self.book_frame.winfo_children():
            widget.destroy()

        # 새로은 book list를 self.book_list에 저장
        self.book_list = new_book_list

        # 책이 하나도 없으면(empty list이면)
        if not self.book_list:
            no_books_label = tk.Label(self.book_frame, text="No books available.", font=("Helvetica", 12))
            no_books_label.pack(fill=tk.X, padx=10, pady=5)
        else:
            # 아니면 내용을 하나씩 순차적으로 표시
            for idx, (title, author, pages) in enumerate(self.book_list, start=1):
                # Create labels for each book's information
                book_info = f"Book {idx}: {title} by {author}, {pages} pages"
                book_label = tk.Label(self.book_frame, text=book_info, anchor="w", justify="left")
                book_label.pack(fill=tk.X, padx=10, pady=5)

        
