import tkinter as tk
from PIL import Image, ImageTk

###################################################
# book_list의 내용을 display해주는 클래스
# book_list의 구조는 main.py를 참고하세요
# 이 파일 외에 다른 파일의 내용은 절대 수정하지 말고,
# 수정이 필요하면 팀장에게 문의하세요
###################################################

class ListBookFrame(tk.Frame):

    def __init__(self, master, book_list, **kwargs):
        super().__init__(master, **kwargs)
        # 넘어온 book_list를 self.book_list에 저장
        self.book_list = book_list
        # 내용 표시를 위한 위젯들 생성
        self.create_widgets()

    # 내용 표시를 위한 위젯들 생성
    def create_widgets(self):
        # 제목 프레임과 라벨
        title_frame = tk.Frame(self, bg='blue')
        title_frame.pack(pady=10, fill=tk.X)
        title_label = tk.Label(title_frame, text="List of Books", font=("Helvetica", 16, "bold"), bg='blue', fg='white')
        title_label.pack(padx=10, pady=10)

        # 책 리스트를 표시할 프레임 생성
        self.book_frame = tk.Frame(self)
        self.book_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        # 책 리스트의 내용을 표시
        self.update_book_list(self.book_list)

    # 책 리스트의 내용을 표시
    def update_book_list(self, new_book_list):
        # 현재 있는 위젯을 없앰
        for widget in self.book_frame.winfo_children():
            widget.destroy()

        # 새로운 책 리스트를 self.book_list에 저장
        self.book_list = new_book_list

        # 책이 하나도 없으면 (empty list이면)
        if not self.book_list:
            no_books_label = tk.Label(self.book_frame, text="No books available.", font=("Helvetica", 12))
            no_books_label.pack(fill=tk.X, padx=10, pady=5)
        else:
            # 아니면 내용을 하나씩 순차적으로 표시
            for idx, (title, author, pages, genres, cover_path) in enumerate(self.book_list, start=1):
                # 각 책을 위한 프레임 생성
                book_frame = tk.Frame(self.book_frame, padx=10, pady=5, relief=tk.RIDGE, borderwidth=2)
                book_frame.pack(side=tk.LEFT, padx=10, pady=5)

                # 책 표지 이미지를 로드
                cover_image = Image.open(cover_path)
                cover_image = cover_image.resize((100, 150), Image.LANCZOS)
                cover_photo = ImageTk.PhotoImage(cover_image)

                # 책 표지 이미지 레이블 생성 및 배치
                cover_label = tk.Label(book_frame, image=cover_photo)
                cover_label.image = cover_photo  # 이미지를 참조하도록 유지
                cover_label.pack()

                # 직사각형 박스 내에 책 제목 레이블 생성 및 배치
                title_frame = tk.Frame(book_frame, bg='lightgray', relief=tk.RIDGE, borderwidth=1)
                title_frame.pack(fill=tk.X)
                title_label = tk.Label(title_frame, text=title, font=("Helvetica", 12), cursor="hand2", bg='lightgray')
                title_label.pack(padx=5, pady=5)

                # 책 제목 레이블에 클릭 이벤트 바인딩하여 책 세부 정보 표시
                title_label.bind("<Button-1>", lambda e, t=title, a=author, p=pages, g=genres: self.show_book_details(t, a, p, g))

    # 새 창에 책 세부 정보 표시
    def show_book_details(self, title, author, pages, genres):
        details_window = tk.Toplevel(self)
        details_window.title(f"Details of {title}")
        
        details_label = tk.Label(details_window, text=f"Title: {title}\nAuthor: {author}\nPages: {pages}\nGages: {genres}", font=("Helvetica", 12))
        details_label.pack(padx=10, pady=10)


        
