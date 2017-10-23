
import Tkinter as tk

from model import UserDB

class UserViewer(tk.Tk):
    def __init__(self):
        #super(UserViewer, self).__init__()
        tk.Tk.__init__(self)

        self.user_db = UserDB()

        btnLoad = tk.Button(self, text="Load", command=self.draw_users)
        btnLoad.pack(expand=tk.YES, fill=tk.BOTH)

        btnQuit = tk.Button(self, text="Quit", command=self.end)
        btnQuit.pack(expand=tk.YES, fill=tk.BOTH)

        self.frameUserList = tk.Frame(self)
        self.frameUserList.pack(expand=tk.YES, fill=tk.BOTH)

        for i in range(1):
            uidLabel = tk.Label(self.frameUserList, text="uid")
            uidLabel.grid(row=i, column=0)

            loginLabel = tk.Label(self.frameUserList, text="login")
            loginLabel.grid(row=i, column=1)

            fullnameLabel = tk.Label(self.frameUserList, text="Full Name")
            fullnameLabel.grid(row=i, column=2)

    def draw_users(self):
        self.frameUserList.destroy()

        self.frameUserList = tk.Frame(self)

        self.frameUserList.pack(expand=tk.YES, fill=tk.BOTH)

        user_list = self.user_db.get_users()

        uidHeader = tk.Label(self.frameUserList, text="UID")
        uidHeader.grid(row=0, column=0)
        loginHeader = tk.Label(self.frameUserList, text="LOGIN")
        loginHeader.grid(row=0, column=1)
        fullnameHeader = tk.Label(self.frameUserList, text="FULLNAME")
        fullnameHeader.grid(row=0, column=2)

        for i, user in enumerate(user_list):
            uidLabel = tk.Label(self.frameUserList, text=user[0])
            uidLabel.grid(row=i+1, column=0)

            loginLabel = tk.Label(self.frameUserList, text=user[1])
            loginLabel.grid(row=i+1, column=1)

            fullnameLabel = tk.Label(self.frameUserList, text=user[2])
            fullnameLabel.grid(row=i+1, column=2)

    def end(self):
        self.quit()

if __name__ == "__main__":
    user_viewer = UserViewer()

    user_viewer.mainloop()
    user_viewer.destroy()