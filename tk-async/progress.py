# -*- coding: utf-8 -*-
#
# $Id: progress.py,v 1.0 2018/10/09 dgkim Exp $
#
# $Log: progress.py,v $
# Revision 1.0
# 최초 구현
#

import Tkinter as tk

import os

from log import Loggable

class Progress(tk.Label, Loggable):

    def __init__(self, parent):
        tk.Label.__init__(self)
        Loggable.__init__(self)

        self.icon = None
        self._num = 0

        self.file_path = '%s%s%s' % (os.path.dirname(__file__), os.sep, 'Bars-1s-50px.gif')

        self.show()

    def show(self):
        try:
            self.icon = tk.PhotoImage(file=self.file_path, format='gif -index {}'.format(self._num))
            self.configure(image=self.icon)
            self._num += 1
        except Exception, e:
            #self.logger.debug(e, exc_info=True)
            self._num = 0

        self.after(10, self.show)