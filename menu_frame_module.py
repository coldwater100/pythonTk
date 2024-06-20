import tkinter as tk

###################################################
# 좌측에 보이는 메뉴 버튼들을 위한 class
# view_other_frame_callback(main.py 의 view_other_frame함수)를 수정하고 싶으면 팀장에 문의
# 이 파일 외에 다른 파일의 내용은 절대 수정하지 말고, 수정 원하면 팀장에 문의
###################################################

class MenuFrame(tk.Frame):
    def __init__(self, parent, view_other_frame_callback, frame_list, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.view_other_frame_callback = view_other_frame_callback
        self.frame_list = frame_list
        self.configure(relief="solid", bd=2)
        self.create_widgets()

    # menu의 button들을 만들고 lambda 함수 설정    
    def create_widgets(self):
        for frame_name, frame in self.frame_list.items():
            button = tk.Button(self, text=frame_name, command=lambda f=frame: self.view_other_frame_callback(f))
            #button = tk.Button(self, text=frame_name, command=lambda : self.view_other_frame_callback(frame)) => 작동안됨
            # 위처럼 하면 f의 값으로 current value가 들어가고, 아래처럼 하면 frame의 값으로 reference value가 들어감
            # loop가 돌면서 frame의 reference value는 바뀌어 있음. 즉 마지막 frame의 값이 저장되어 있음
            # f=frame에서 frame의 value가 f에 저장 되는 듯 함
            button.pack(fill="x", pady=5, padx=10)


