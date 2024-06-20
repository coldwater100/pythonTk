import tkinter as tk
from tkinter import messagebox

###################################################
# book_list에서 책을 하나 삭제하는 Class
# delete_book_callback 함수(delete_book in main.py)를 수정하고 싶으면 팀장에게 문의
# 이 파일 외에 다른 파일의 내용은 절대 수정하지 말고, 수정 원하면 팀장에 문의
###################################################

class DeleteBookFrame(tk.Frame):
    def __init__(self, master, delete_book_callback, **kwargs):
        super().__init__(master, **kwargs)
        self.delete_book_callback = delete_book_callback

        self.create_widgets()

    def create_widgets(self):
        # label, entry for book index
        index_label = tk.Label(self, text="Book Index:")
        index_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.index_entry = tk.Entry(self)
        self.index_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

        # Button - delete book
        delete_button = tk.Button(self, text="Delete Book", command=self.delete_book)
        delete_button.grid(row=1, columnspan=2, pady=10)

    def delete_book(self):
        # entry에 입력된 값을 가져옴
        index = self.index_entry.get().strip()

        # 입력값이 숫자인지 확인
        if index.isdigit():
            index = int(index)
            self.delete_book_callback(index)

            # 입력 필드 초기화
            self.index_entry.delete(0, tk.END)
        else:
            # 숫자가 아니면 오류 메시지
            messagebox.showerror("오류", "유효한 값을 다시 입력하세요.")
