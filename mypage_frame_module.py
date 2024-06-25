import tkinter as tk
from tkinter import Label, Frame
from user_data_manage import UserDataManage

class MyPageFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(bg="#f0f0f0")
        self.create_widgets()
        self.update_user_data(UserDataManage.now_user)

    def create_widgets(self):
        self.label_title = tk.Label(self, text="My Page", font=("Arial", 24, "bold"), bg="#f0f0f0")
        self.label_title.pack(pady=10)
        
        self.label_username = tk.Label(self, text="Username:", font=("Arial", 12), bg="#f0f0f0")
        self.label_username.pack(pady=5)

        self.label_password = tk.Label(self, text="Password:", font=("Arial", 12), bg="#f0f0f0")
        self.label_password.pack(pady=5)

        self.label_genre = tk.Label(self, text="Favorite Genre:", font=("Arial", 12), bg="#f0f0f0")
        self.label_genre.pack(pady=5)

        self.label_pages = tk.Label(self, text="Preferred Page Length:", font=("Arial", 12), bg="#f0f0f0")
        self.label_pages.pack(pady=5)

    def update_user_data(self, user_data):
        if user_data:
            self.label_username.config(text=f"Username: {user_data[0]}")
            self.label_password.config(text=f"Password: {user_data[1]}")
            self.label_genre.config(text=f"Favorite Genre: {user_data[2]}")
            self.label_pages.config(text=f"Preferred Page Length: {user_data[3]}")
        else:
            self.label_username.config(text="Username: N/A")
            self.label_password.config(text="Password: N/A")
            self.label_genre.config(text="Favorite Genre: N/A")
            self.label_pages.config(text="Preferred Page Length: N/A")