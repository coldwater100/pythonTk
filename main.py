import tkinter as tk
from home_frame_module import HomeFrame
from login_frame_module import LoginFrame
from menu_frame_module import MenuFrame
from list_book_frame_module import ListBookFrame
from add_book_frame_module import AddBookFrame
from delete_book_frame_module import DeleteBookFrame
from mypage_frame_module import MyPageFrame
from tkinter import messagebox
import pickle
import os
from user_data_manage import UserDataManage
from book_datas import BookDatas

###################################################
# 전체 프로그램의 main part 입니다
# 혼자서 이 프로그램을 수정하시면 안됩니다
# 수정할 부분이 있으시면 팀장에 문의해 주세요
###################################################

# 우측 frame의 frame 교체 함수
def view_other_frame(frame_to_show):
    global login_state
    # 필요시 로그인 상태 체크
    if frame_to_show in [list_books_frame, add_book_frame, delete_book_frame, mypage_frame]:
        if not login_state:
            messagebox.showerror("알림", "로그인 후 이용가능합니다")
            return
    # 우측 프레임의 모든 프레임을 안보이게 하고     
    for frame in right_frames:
        frame.place_forget()
    # frame_to_show만 보이게 한다    
    frame_to_show.place(relx=0.2, rely=0.05, relwidth=0.8, relheight=0.95)

# username 을 바꾸는 함수, login_frame에서 사용한다, LoginFrame을 생성할 때 함수 전달
# LoginFrame에서 이 코드를 실행시킴
def update_username(new_username):
    global username
    global login_state
    global login_button
    username = new_username
    label_user.config(text=f"Username: {username}")
    login_state = True
    messagebox.showinfo("알림", "성공적으로 로그인 되었습니다")
    mypage_frame.update_user_data(next((user for user in UserDataManage.load_user_data() if user[0] == username), None))
    login_button.config(bg="#D0FC5C",text="다른 계정으로 로그인")
    view_other_frame(home_frame)

def suggest_book():
    pass

# program 시작시에 local file에서 book을 읽어 온다
def load_books():
    global book_list
    if os.path.exists("book_name_list.bn"):
        with open("book_name_list.bn", "rb") as file:
            book_list = pickle.load(file)
    else:
        book_list = [("Python Programing", "team 1", 342, BookDatas.genres[4], BookDatas.images[4]), 
                     ("apple", "chance", 232, BookDatas.genres[2], BookDatas.images[2])]  # default

# 현재의 book_list를 file로 저장한다
def save_books():
    global book_list
    with open("book_name_list.bn", "wb") as file:
        pickle.dump(book_list, file)    

# 새로운 책을 현재 book list에 추가한다 AddBookFrame의 변수로 이 함수를 넘겨 준다, 즉 AddBookFrame에서 실행 된다.
def add_book(new_book):
    global book_list
    book_list.append(new_book)
    # list_books_frame은 초기화 되고 나면 보이지는 않지만 생성되어 있는 상태이므로 list_books_frame instance의
    # update_book_list를 이용 list_books_frame의 내용을 update 해 준다
    list_books_frame.update_book_list(book_list)
    save_books()
    messagebox.showinfo("알림", "새 책이 추가 되었어요")

# 하나의 책을 삭제 한다. DeleteBookFrame의 변수로 이 함수를 넘겨 준다, 즉 DeleteBookFrame에서 실행된다.
# 변수로 list_book_frame에서 확인 할 수 있는 index를 넘겨 준다.
def delete_book(idx):
    global book_list
    if 0 <= idx < len(book_list):
        # index가 유효하면
        del book_list[idx]
        list_books_frame.update_book_list(book_list)
        save_books()
        messagebox.showinfo("알림", "지정한 책이 삭제 되었어요")
    else:
        # index가 유효하지 않으면 오류 메시지
        tk.messagebox.showerror("오류", "유효한 인덱스를 입력하세요.")

# 윈도우 생성 및 크기 지정
win = tk.Tk()
win.geometry("800x600")

# login user의 이름을 위한 변수
username = "guest"
login_state = False

# 현재 book-list를 가지는 변수, book_title, author, pages
load_books()

# 현재 로그인 사용자를 표시하는 frame
username_frame = tk.Frame(win, height=30, bg="lightgray")
username_frame.pack(fill="x")
label_user = tk.Label(username_frame, text=f"Username: {username}")
label_user.pack(side="left", padx=10, ipadx=20, ipady=5)

login_frame = LoginFrame(win, update_username, relief="solid", bd=2)
login_button = tk.Button(username_frame, text="login", command=lambda f=login_frame: view_other_frame(f) ,bg="#4CAF50")
login_button.pack(side="right", padx=10, ipadx=20, ipady=5)

# 필요한 frame 들을 생성
home_frame = HomeFrame(win, relief="solid", bd=2)
# 우측 패널을 home_frame으로 초기화 한다.
home_frame.place(relx=0.2, rely=0.05, relwidth=0.8, relheight=0.95)

# login_frame = LoginFrame(win, update_username, relief="solid", bd=2)
list_books_frame = ListBookFrame(win, book_list, relief="solid", bd=2)
add_book_frame = AddBookFrame(win, add_book, relief="solid", bd=2)
delete_book_frame = DeleteBookFrame(win, delete_book, relief="solid", bd=2)
mypage_frame = MyPageFrame(win, relief="solid", bd=2)

# 우측 에 필요한 frame들의 list
# right_frames = [home_frame, login_frame, list_books_frame, add_book_frame, delete_book_frame, mypage_frame]
right_frames = [home_frame, list_books_frame, add_book_frame, delete_book_frame, mypage_frame]


# MenuFrame(좌측) 생성에 변수로 들어갈 list.  "Button text" : frame name  의 구조 
frame_list = {
    "Home": home_frame,
    # "Login": login_frame,
    "My Page": mypage_frame,
    "View Books": list_books_frame,
    "Add a Book": add_book_frame,
    "Delete a Book": delete_book_frame
}

# MenuFrame 생성
menu_frame = MenuFrame(win, view_other_frame, frame_list, relief="solid", bd=2)
menu_frame.place(rely=0.05, relwidth=0.2, relheight=0.95)  

# 윈도우 시작
win.mainloop()

