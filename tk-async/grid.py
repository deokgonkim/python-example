# -*- coding: utf-8 -*-
#
# $Id: grid.py,v 1.0 2018/10/09 dgkim Exp $
#
# $Log: grid.py,v $
# Revision 1.0
# 최초 작성
#

import threading

import Tkinter as tk
import Queue

from progress import Progress


class Grid(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=1)
        tk.Grid.rowconfigure(self, 2, weight=1)

        self.configure(width=600, height=400)

        self.progress = None

        self.btn1 = tk.Button(self, text='Show Progress')
        self.btn1.grid(row=0, column=0, sticky='news')
        self.btn2 = tk.Button(self, text='Sleep')
        self.btn2.grid(row=0, column=1, sticky='news')
        self.btn3 = tk.Button(self, text='mq sleep')
        self.btn3.grid(row=1, column=0, sticky='news')
        self.btn4 = tk.Button(self, text='thread sleep')
        self.btn4.grid(row=1, column=1, sticky='news')

        self._run = 0
        self.running_time = tk.StringVar()

        self.lbl_running_time = tk.Label(self, textvariable=self.running_time)
        self.lbl_running_time.grid(row=2, column=0, columnspan=2)

        self.btn1.configure(command=self.show_progress)
        self.btn2.configure(command=self.sleep)
        self.btn3.configure(command=self.mq_sleep)
        self.btn4.configure(command=self.thread_sleep)

        self.mq = Queue.Queue()

        self.main_show()

    def show_progress(self):
        if self.progress:
            self.hide_progress()

        self.progress = Progress(self)

        x = self.winfo_width() / 2
        y = self.winfo_height() / 2

        self.progress.place(relx=0.0, rely=0.0, x=x, y=y, anchor='center')


    def hide_progress(self):
        if self.progress:
            self.progress.destroy()
            self.progress = None

    def sleep(self):
        import time; time.sleep(5)

    def mq_sleep(self):
        self.mq.put('sleep')

    def thread_sleep(self):
        def sleep():
            import time;time.sleep(5)
            self._run = 0

        t = threading.Thread(target=sleep)
        t.setDaemon(True)
        t.start()

    def main_show(self):
        self.running_time.set(str(self._run))
        try:
            m = self.mq.get_nowait()
            if m == 'sleep':
                import time; time.sleep(5)
        except Queue.Empty, e:
            pass
        self._run += 1
        self.after(1000, self.main_show)
