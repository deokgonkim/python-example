#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#
# $Id: TkApp.py,v 1.1 2017/10/19 deokgonkim Exp $
#

import Tkinter as tk


class TkApp(tk.Tk):
    def __init__(self):
        #super(TkApp, self).__init__()
        tk.Tk.__init__(self)

        button = tk.Button(self, text='Button', command=self.hello)
        button.pack(expand=tk.YES, fill=tk.BOTH)

        btnQuit = tk.Button(self, text="Quit", command=self.end)
        btnQuit.pack(expand=tk.YES, fill=tk.BOTH)

    def hello(self):
        print("hello")

    def end(self):
        self.quit()


if __name__ == '__main__':
    app = TkApp()
    app.mainloop()
    app.destroy()

