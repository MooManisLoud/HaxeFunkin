import tkinter as tk
from tkinter import messagebox
import pyfiglet
import sys
import time
import os
import subprocess
import webbrowser
import win32com.shell.shell as shell
from pypresence import Presence

(icon_path) = "/" # dw about this, it is useless
(name) = "HaxeFunkin" # Name of the thing used for change the pyfiglet ascii art
(version) = "1.0.0" # just the version for the info section
(creator) = "MooMan" # dont change this plz
(editor) = "" # change this if your editing

def notext():
    print(" ")

if not shell.IsUserAnAdmin():
    print("Script is not running with administrator privileges. Requesting elevation...")
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=' '.join(sys.argv))

print("Script is running with administrator privileges.")
os.system('cls')

try:
    os.system("title HaxeFunkin")

    text = (name)
    width = 20

    ascii_art = pyfiglet.figlet_format(text)
    centered_art = ascii_art.center(width)  

    print(centered_art)

    def loading_animation():
        frames = ["[*     ]", "[ *    ]", "[  *   ]", "[   *  ]", "[    * ]", "[     *]", "[    * ]", "[   *  ]", "[  *   ]", "[ *    ]"]
        for i in range(10):
            time.sleep(0.3)
            sys.stdout.write("\r" + frames[i % len(frames)])
            sys.stdout.flush()

        sys.stdout.write("\n")

    loading_animation()

    os.system('cls')
    print(ascii_art)

    def menu():
        print("[1] Start Downloading | [2] Credits | [3] Github | [4] Info | [0] Exit")

    menu()
    option = -1
    while option != 0:
        option = int(input("Enter your option:"))

        if option == 1:
            os.system("title HaxeFunkin - Downloading")
            os.system('cls')
            print(ascii_art)

            print("Installing Libraries ", loading_animation())
            os.system("haxelib install hmm")
            os.system("haxelib run hmm install")
            os.system("haxelib install hxcpp > nul")
            os.system("haxelib install lime")
            os.system("haxelib install openfl")
            os.system("haxelib --never install flixel")
            os.system("haxelib run lime setup flixel")
            os.system("haxelib run lime setup")
            os.system("haxelib install flixel-tools")
            os.system("haxelib install flixel-ui")
            os.system("haxelib install flixel-addons")
            os.system("haxelib install tjson")
            os.system("haxelib install hxjsonast")
            os.system("haxelib install hscript")
            os.system("haxelib install hxcpp-debug-server")
            os.system("haxelib run flixel-tools setup")
            os.system("haxelib git polymod https://github.com/larsiusprime/polymod.git")
            os.system("haxelib git linc_luajit https://github.com/nebulazorua/linc_luajit")
            os.system("haxelib git hscript-ex https://github.com/ianharrigan/hscript-ex")
            os.system("haxelib git discord_rpc https://github.com/Aidan63/linc_discord-rpc")
            os.system("haxelib install hxCodec")

            messagebox.showinfo("HaxeFunkin", "Finished with Libraries now going to get VSCommunity")

            os.system("curl -# -O https://download.visualstudio.microsoft.com/download/pr/3105fcfe-e771-41d6-9a1c-fc971e7d03a7/8eb13958dc429a6e6f7e0d6704d43a55f18d02a253608351b6bf6723ffdaf24e/vs_Community.exe")
            os.system("vs_Community.exe --add Microsoft.VisualStudio.Component.VC.Tools.x86.x64 --add Microsoft.VisualStudio.Component.Windows10SDK.19041 -p")
            os.system("del vs_Community.exe")

            messagebox.showwarning("HaxeFunkin", "Some things may not have not been installed but dont worry if you get any errors just say in the issues section on the github page!")
            notext()
        elif option == 2:
            notext()
            print("Credits:")
            print("- Programmer: MooMan")
            print("- Help with code: ChatGPT")
            notext()
            input("Press Enter")
            os.system('cls')
            print(ascii_art)
            menu()
        elif option == 3:
            print("We do not have github yet!")
            notext()
            input("Press Enter")
            os.system('cls')
            print(ascii_art)
            menu()
        elif option == 4:
            notext()
            print("Version:", (version))
            print("Name:", (name))
            print("Creator:", (creator))
            notext()
            input("Press Enter")
            os.system('cls')
            print(ascii_art)
            menu()
        else:
            print("Invalid Option.")

except Exception as e:
    messagebox.showerror("HaxeFunkin Crash Handler", "An error occurred: {}" .format(str(e)))
    print(format(str(e)))