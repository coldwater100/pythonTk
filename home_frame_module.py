import tkinter as tk

###################################################
# Home 화면용 class
# 이 파일 외에 다른 파일의 내용은 절대 수정하지 말고, 수정 원하면 팀장에 문의
###################################################

class HomeFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.label_title = tk.Label(self, text="Hello World", font=("Arial", 16))
        self.label_title.pack(pady=10)
        


