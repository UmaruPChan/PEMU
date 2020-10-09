""" CEMU Launcher written on Python created by Linkachus17 in help with OldManOZ, Agilly1985, and FailedShack the creator of WiiU USBHelper
The plan on this program is to launch CEMU, that's all.
Schematic
Program lauched -> Asks for CEMU.exe using GUI -> if exist -> Launch CEMU and exit the program -> Also saves the path somewhere in system
                                                  if not   -> User will select cancel and exits the program

2nd time Program launched -> finds the config file is exist -> if exist -> reads the path and open file from saved path
                                                               if not   -> will ask for CEMU.exe path
"""

from tkinter import filedialog
from tkinter import *
from time import sleep
import subprocess
import os
import tkinter as tk

# Checks if config file is exist
def checking_config():
    print('Checnking the config......')
    sleep(1)
    config_path = 'C:/Users/Public/Documents/config_pemu.txt'
    exist = os.path.exists(config_path)
    print(exist)
    f = open('C:/Users/Public/Documents/config_pemu.txt', 'r')
    read_path = f.read()
    cemu_path = print(read_path)
    cemu_path
    subprocess.call(cemu_path) # Problem -> NoneType object is not iterable -> add quote on start and end path will fix


# Writes the path into a file and save it somewhere on Public Documents where nobody will ever disturb it
def write_config():
    print('Creating a config file, please wait.......')
    sleep(1)
    f = open('C:/Users/Public/Documents/config_pemu.txt', 'w')
    f.write(str(path))
    f.close




# Main code
# If there's problem this code can't continue(obviously)
checking_config() # If config file is exist and path to CEMU is exist on file, opens CEMU using saved path. if not /shrug maybe it'll pass?
print('Please select CEMU from the GUI')
sleep(1)
file = Tk()
# Why i need this? if i don't write this then a big empty TKinter GUI appears which is annoying
cemu = tk.Label(text=' ')
cemu.pack()
file.filename = filedialog.askopenfilename(filetypes=[('Cemu', 'Cemu.exe')])
path = file.filename
write_config() # Write the path into a file and save it somewhere so you don't need to find CEMU path everytime you open the file