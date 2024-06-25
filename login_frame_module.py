import tkinter as tk
from tkinter import messagebox
import os
import pickle
from book_datas import BookDatas
from tkinter import ttk
from user_data_manage import UserDataManage

class LoginFrame(tk.Frame):
    def __init__(self, master, update_username, **kwargs):
        super().__init__(master, **kwargs)
        self.update_user_callback = update_username

        self.configure(bg="#f0f0f0")

        # Login form
        self.label_title = tk.Label(self, text="Login", font=("Arial", 24, "bold"), bg="#f0f0f0")
        self.label_title.pack(pady=10)
        
        self.label_username = tk.Label(self, text="Username:", font=("Arial", 12), bg="#f0f0f0")
        self.label_username.pack(pady=5)
        
        self.entry_username = tk.Entry(self, font=("Arial", 12), highlightbackground="#d1d1d1", highlightthickness=1)
        self.entry_username.pack(pady=5, ipady=5, ipadx=5)
        
        self.label_password = tk.Label(self, text="Password:", font=("Arial", 12), bg="#f0f0f0")
        self.label_password.pack(pady=5)
        
        self.entry_password = tk.Entry(self, show='*', font=("Arial", 12), highlightbackground="#d1d1d1", highlightthickness=1)
        self.entry_password.pack(pady=5, ipady=5, ipadx=5)
        
        self.button_login = tk.Button(self, text="Login", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.login)
        self.button_login.pack(pady=10, ipadx=10, ipady=5)

        self.button_toggle_register = tk.Button(self, text="Register", font=("Arial", 12, "bold"), bg="#2196F3", fg="white", command=self.show_register_form)
        self.button_toggle_register.pack(pady=10, ipadx=10, ipady=5)

        # Register form
        self.label_new_username = tk.Label(self, text="New Username:", font=("Arial", 12), bg="#f0f0f0")
        self.entry_new_username = tk.Entry(self, font=("Arial", 12), highlightbackground="#d1d1d1", highlightthickness=1)
        
        self.label_new_password = tk.Label(self, text="New Password:", font=("Arial", 12), bg="#f0f0f0")
        self.entry_new_password = tk.Entry(self, show='*', font=("Arial", 12), highlightbackground="#d1d1d1", highlightthickness=1)
        
        self.label_pages = tk.Label(self, text="Pages:", font=("Arial", 12), bg="#f0f0f0")
        self.entry_pages= tk.Entry(self, font=("Arial", 12), highlightbackground="#d1d1d1", highlightthickness=1)

        self.label_genres = tk.Label(self, text="Genres:", font=("Arial", 12), bg="#f0f0f0")
        self.genre_combobox = ttk.Combobox(self)       # 콤보박스 생성
        self.genre_combobox.config(height=5,values=BookDatas.genres,state="readonly")           
        self.genre_combobox.set(BookDatas.genres[0])           # 맨 처음 나타낼 값 설정 

        self.button_register_user = tk.Button(self, text="Register", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.register_user)
        
        self.button_toggle_login = tk.Button(self, text="Back to Login", font=("Arial", 12, "bold"), bg="#2196F3", fg="white", command=self.show_login_form)

        # 엔터 키 이벤트 바인딩
        self.entry_password.bind('<Return>', self.login_event)

        # user의 id 및 password list
        self.idpwd = UserDataManage.load_user_data()

    def login_event(self, event):
        self.login()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        for user_data in self.idpwd:
            if username == user_data[0] and password == user_data[1]:
                self.update_user_callback(username)
                self.entry_username.delete(0, tk.END)
                self.entry_password.delete(0, tk.END)
                UserDataManage.now_user=user_data
                return

        messagebox.showerror("Login Failed", "Invalid username or password")
        self.entry_password.delete(0, tk.END)

    def show_register_form(self):
        self.clear_form()
        self.label_title.config(text="Register")
        self.label_username.pack_forget()
        self.entry_username.pack_forget()
        self.label_password.pack_forget()
        self.entry_password.pack_forget()

        self.button_login.pack_forget()
        self.button_toggle_register.pack_forget()

        self.label_new_username.pack(pady=5)
        self.entry_new_username.pack(pady=5, ipady=5, ipadx=5)
        self.label_new_password.pack(pady=5)
        self.entry_new_password.pack(pady=5, ipady=5, ipadx=5)
        self.label_genres.pack(pady=5)
        self.genre_combobox.config(state="readonly")           
        self.genre_combobox.pack(pady=5, ipady=5, ipadx=5)
        self.label_pages.pack(pady=5)
        self.entry_pages.pack(pady=5, ipady=5, ipadx=5)
        self.button_register_user.pack(pady=10, ipadx=10, ipady=5)
        self.button_toggle_login.pack(pady=10, ipadx=10, ipady=5)

        # 엔터 키 이벤트 바인딩
        self.entry_new_password.bind('<Return>', self.register_event)

    def show_login_form(self):
        self.clear_form()
        self.label_title.config(text="Login")
        self.label_new_username.pack_forget()
        self.entry_new_username.pack_forget()
        self.label_new_password.pack_forget()
        self.entry_new_password.pack_forget()
        self.label_genres.pack_forget()
        self.genre_combobox.pack_forget()
        self.label_pages.pack_forget()
        self.entry_pages.pack_forget()
        self.button_register_user.pack_forget()
        self.button_toggle_login.pack_forget()
    

        self.label_username.pack(pady=5)
        self.entry_username.pack(pady=5, ipady=5, ipadx=5)
        self.label_password.pack(pady=5)
        self.entry_password.pack(pady=5, ipady=5, ipadx=5)
        self.button_login.pack(pady=10, ipadx=10, ipady=5)
        self.button_toggle_register.pack(pady=10, ipadx=10, ipady=5)

        # 엔터 키 이벤트 바인딩
        self.entry_password.bind('<Return>', self.login_event)

    def clear_form(self):
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.entry_new_username.delete(0, tk.END)
        self.entry_new_password.delete(0, tk.END)
        self.entry_pages.delete(0, tk.END)

    def register_event(self, event):
        self.register_user()

    def register_user(self):
        new_username = self.entry_new_username.get()
        new_password = self.entry_new_password.get()
        new_like_genre = self.genre_combobox.get()
        new_like_length = self.entry_pages.get()

        if not new_username or not new_password:
            messagebox.showerror("Error", "Username and Password cannot be empty")
            return

        for user_data in self.idpwd:
            if new_username == user_data[0]:
                messagebox.showerror("Error", "Username already exists")
                return

        self.idpwd.append((new_username, new_password, new_like_genre, new_like_length))
        UserDataManage.save_user_data(self.idpwd)
        messagebox.showinfo("Success", "User registered successfully")
        self.show_login_form()





        


