import tkinter as tk
from PIL import Image, ImageTk
import pygame
import os
#class 정의
class HomeFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # 프레임 크기 설정
        self.width = 800
        self.height = 600
        self.config(width=self.width, height=self.height)

        # Canvas를 사용하여 배경 이미지 설정
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.pack(fill="both", expand=True)

        # 배경 이미지 로드 및 크기 조절
        image_path = "books.jpg"
        if os.path.exists(image_path):
            self.bg_image = Image.open(image_path)
            self.bg_image = self.bg_image.resize((self.width, self.height), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            # 이미지 배치
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo)
        else:
            print(f"Error: Image file '{image_path}' not found.")

        # 반투명 박스 설정
        self.create_transparent_box()

        # 음악 재생 기능
        self.play_music()

    def create_transparent_box(self):
        # 반투명 박스 이미지 생성
        box_width = 300
        box_height = 100
        box_x = (self.width - box_width) // 2 - 100  # 박스 위치를 왼쪽으로 100 이동
        box_y = 50
        box_color = '#000000'
        box_opacity = 0.5
        self.canvas.create_rectangle(
            box_x, box_y, box_x + box_width, box_y + box_height,
            fill=box_color, stipple="gray50", outline=""
        )

        # 텍스트 라벨 설정
        label_x = self.width // 2 - 100  # 텍스트 위치를 왼쪽으로 100 이동
        self.label_title = tk.Label(self, text='도서관리 프로그램', font=("Arial", 24, "bold"), bg=box_color, fg='white')
        self.label_title_window = self.canvas.create_window(label_x, box_y + box_height // 2, window=self.label_title, anchor="center")

    def play_music(self):
        music_path = "./waterfall.mp3"
        if os.path.exists(music_path):
            pygame.mixer.init()
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(-1)  # -1은 무한 반복을 의미
        else:
            print(f"Error: Music file '{music_path}' not found.")



