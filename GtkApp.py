#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# $Id: GtkApp.py,v 1.0 2017/10/26 dgkim Exp $

import gi
from gi.repository import Gtk

gi.require_version('Gtk', '3.0')


class GtkApp(Gtk.Window):
    def __init__(self):
        super(Gtk.Window, self).__init__(title="GtkApp first application")

        self.set_border_width(10)

        self.boxLayout = Gtk.Box(spacing=6)
        self.add(self.boxLayout)

        self.btnHello = Gtk.Button(label="Hello")
        self.btnHello.connect("clicked", self.on_hello_clicked)

        self.boxLayout.pack_start(self.btnHello, True, True, 0)

        self.btnQuit = Gtk.Button(label="Quit")
        self.btnQuit.connect("clicked", self.on_quit_clicked)

        self.boxLayout.pack_start(self.btnQuit, True, True, 0)

    def on_hello_clicked(self, widget):
        print("아녕하세요")

    def on_quit_clicked(self, widget):
        Gtk.main_quit()

if __name__ == "__main__":
    app = GtkApp()
    app.connect("delete-event", Gtk.main_quit)
    app.show_all()
    Gtk.main()