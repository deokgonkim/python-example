# -*- coding: utf-8 -*-

import Tkinter as tk
import threading

import datetime
import time

import urllib

running = True

class SimpleClock(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.var_date1 = tk.StringVar()
        self.var_date2 = tk.StringVar()

        self.frame = tk.Frame(self)
        self.frame.pack()

        self.lbl_clock = tk.Label(self.frame, text='Clocks')
        self.lbl_clock.pack(expand='yes', fill='both')

        self.txt_clock = tk.Entry(self.frame, textvariable=self.var_date1)
        self.txt_clock.pack(side='left', expand='yes', fill='both')

        self.txt_clock2 = tk.Entry(self.frame, textvariable=self.var_date2)
        self.txt_clock2.pack(side='right', expand='yes', fill='both')

        self._event_binding()

        t = threading.Thread(target=update_localdate, args=(self.var_date1,))
        t.setDaemon(True)
        t.start()

        t = threading.Thread(target=update_serverdate, args=(self.var_date2,))
        t.setDaemon(True)
        t.start()

    def terminate(self, event=None):
        running = False
        self.destroy()

    def _event_binding(self):
        self.bind('<Escape>', self.terminate)
        self.bind('<Control-q>', self.terminate)
        self.bind('<Control-Q>', self.terminate)

def update_localdate(var):
    while running:
        d = datetime.datetime.now()
        print('Updating localdate %s' % d)
        var.set(d)
        time.sleep(1)

def update_serverdate(var):
    while running:
        d = urllib.urlopen('https://www.ossfsc.net/test1/').read()
        print('Updating serverdate %s' % d)
        var.set(d)
        time.sleep(1)

if __name__ == '__main__':
    app = SimpleClock()
    app.mainloop()
