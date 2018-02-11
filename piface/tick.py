
import Tkinter as tk
import threading
import pifacedigitalio as pfd
import time

class relayplayer(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.board = pfd.PiFaceDigital()

        self.buttonStart = tk.Button(self, text="Start", command=self.start)
        self.buttonStart.pack(fill=tk.BOTH)

        self.buttonInc1 = tk.Button(self, text="Inc1", command=self.inc1)
        self.buttonInc1.pack(fill=tk.BOTH)
        self.buttonDec1 = tk.Button(self, text="Dec1", command=self.dec1)
        self.buttonDec1.pack(fill=tk.BOTH)
        self.buttonInc2 = tk.Button(self, text="Inc2", command=self.inc2)
        self.buttonInc2.pack(fill=tk.BOTH)
        self.buttonDec2 = tk.Button(self, text="Dec2", command=self.dec2)
        self.buttonDec2.pack(fill=tk.BOTH)

        self.buttonQuit = tk.Button(self, text="Quit", command=self.end)
        self.buttonQuit.pack(fill=tk.BOTH)

        self.tick1 = 0.5
        self.tick2 = 0.5

    def inc1(self, event=None):
        print("inc1")
        self.tt.tick1 += .1
    def dec1(self, event=None):
        print("dec1")
        self.tt.tick1 -= .1
    def inc2(self, event=None):
        print("inc2")
        self.tt.tick2 += .1
    def dec2(self, event=None):
        print("dec2")
        self.tt.tick2 -= .1

    def start(self):
        self.tt = ThreadedTask(self.board, self.tick1, self.tick2)
        self.tt.start()

    def end(self):
        self.tt.stop = True
        self.quit()

class ThreadedTask(threading.Thread):
    def __init__(self, board, tick1, tick2):
        threading.Thread.__init__(self)
        self.board = board
        self.tick1 = tick1
        self.tick2 = tick2
        self.stop = False

    def run(self):
        while True:
            b0 = self.board.relays[0].value
            b0 = 0 if b0 == 1 else 1
            self.board.relays[0].value = b0
            time.sleep(self.tick1)

            b1 = self.board.relays[1].value
            b1 = 0 if b1 == 1 else 1
            self.board.relays[1].value = b1
            time.sleep(self.tick2)

            if self.stop == True:
                break


if __name__ == '__main__':
    r = relayplayer()
    listener0 = pfd.InputEventListener()
    listener0.register(0, pfd.IODIR_BOTH, r.inc1)
    listener0.activate()
    listener1 = pfd.InputEventListener()
    listener1.register(1, pfd.IODIR_BOTH, r.dec1)
    listener1.activate()
    listener2 = pfd.InputEventListener()
    listener2.register(2, pfd.IODIR_BOTH, r.inc2)
    listener2.activate()
    listener3 = pfd.InputEventListener()
    listener3.register(3, pfd.IODIR_BOTH, r.dec2)
    listener3.activate()
    r.mainloop()
    listener0.deactivate()
    listener1.deactivate()
    listener2.deactivate()
    listener3.deactivate()
    r.destroy()
