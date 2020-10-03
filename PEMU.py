""" CEMU Launcher written on Python created by Linkachus17 in help with OldManOZ, Agilly1985, and FailedShack the creator of WiiU USBHelper
The plan on this program is to launch CEMU, that's all.
Schematic
Program lauched -> Asks for CEMU.exe using GUI -> if exist -> Launch CEMU and exit the program
                                                  if not   -> User will select cancel and exits the program
"""

from tkinter import filedialog
from tkinter import *
from time import sleep
import subprocess
import os
import tkinter as tk



print('Please select CEMU from the GUI')
sleep(1)
file = Tk()
cemu = tk.Label(text=' ')
cemu.pack()
file.filename = filedialog.askopenfilename(filetypes=[('Cemu', 'Cemu.exe')])
path = file.filename
subprocess.call(path)