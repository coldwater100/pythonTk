import pickle
import os
from book_datas import BookDatas

class UserDataManage:  
    now_user=[]
    def load_user_data():
        if os.path.exists("user_data.pkl"):
            with open("user_data.pkl", "rb") as file:
                return pickle.load(file)
        else:
            # Default user data
            return [("user1", "1111", BookDatas.genres[0], "100"), ("user2", "2222", BookDatas.genres[1], "200"), 
                    ("user3", "3333", BookDatas.genres[1], "150"), ("user3", "3333", BookDatas.genres[3], "450"), 
                    ("user3", "3333", BookDatas.genres[4], "50")]

    def save_user_data(idpwd):
        with open("user_data.pkl", "wb") as file:
            pickle.dump(idpwd, file)