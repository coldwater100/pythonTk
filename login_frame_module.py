import tkinter as tk
from tkinter import messagebox

###################################################
# Login용 화면을 만드는 class
# update_username의 구조는 main.py에서 참고하시고, 수정하고 싶으면 팀장에 문의
# 이 파일 외에 다른 파일의 내용은 절대 수정하지 말고, 수정 원하면 팀장에 문의
###################################################

class LoginFrame(tk.Frame):
    def __init__(self, master, update_username, **kwargs):
        super().__init__(master, **kwargs)
        self.update_user_callback = update_username
        
        # Login form
        self.label_title = tk.Label(self, text="Login", font=("Arial", 16))
        self.label_title.pack(pady=10)
        
        self.label_username = tk.Label(self, text="Username:")
        self.label_username.pack(pady=5)
        
        self.entry_username = tk.Entry(self)
        self.entry_username.pack(pady=5)
        
        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack(pady=5)
        
        self.entry_password = tk.Entry(self, show='*')
        self.entry_password.pack(pady=5)
        
        self.button_login = tk.Button(self, text="Login", command=self.login)
        self.button_login.pack(pady=10)

        # user의 id및 password list 
        # 개선하려면 db이용하거나 local file에 저장 후 암호화 해서 user 추가, 삭제, 변경 가능
        self.idpwd = (("user1", "1111"), ("user2", "2222"), ("user3", "3333"))

    def login(self):
        #login 기능,  main.py에서 넘어온 update_username 함수를 이용 username을 수정한다.
        username = self.entry_username.get()
        password = self.entry_password.get()
        #login에 성공한다면
        for user, pwd in self.idpwd:
            if username == user and password == pwd:
                self.update_user_callback(username)
                return
        #login에 실패한다면
        messagebox.showerror("Login Failed", "username 또는 password가 틀렸습니다")


        


