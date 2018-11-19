# -*- coding: utf-8 -*-
#
# $Id: app.py,v 1.0 2018/10/09 dgkim Exp $
#
# $Log: app.py,v $
# Revision 1.0
# 최초 구현
#

import Tkinter as tk

from grid import Grid

import logging

logging.basicConfig(level=logging.DEBUG)

class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.grid1 = Grid(self)
        self.grid1.pack()
        self.grid1.grid_propagate(0)


if __name__ == '__main__':
    app = App()
    app.mainloop()