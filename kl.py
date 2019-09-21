import sys
import os
import win32console
import win32gui
import pythoncom
import pyHook
import mp3play
import tkMessageBox
import Tkinter

if getattr(sys, "frozen", False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

root = Tkinter.Tk()
root.withdraw()

filename = application_path + r"\2081956.mp3"

clip = mp3play.load(filename)


def hide():
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window, 0)

    return True


def OnKeyboardEvent(event):
    # print repr(event.Ascii), repr(chr(event.Ascii)), '\n'
    allowed = 1

    if event.Ascii is 22 or event.Ascii is 24:  # ctrl+X or ctrl+C
        if clip.isplaying() is False:
            copyToClipBoard("Matador de Passarinho")
            PaPaPaPa()
    elif event.Ascii is 26:  # ctrl+Z
        allowed = 0
    else:
        pass

    return allowed


def PaPaPaPa():
    clip.play(1550, 2550)


def copyToClipBoard(txt):
    root.clipboard_clear()
    root.clipboard_append(txt)


# hide()
while True:
    hook = pyHook.HookManager()
    hook.KeyDown = OnKeyboardEvent
    hook.HookKeyboard()
    pythoncom.PumpMessages()

root.destroy()
