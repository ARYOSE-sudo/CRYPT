from subprocess import run
from colorama import Fore
import pyAesCrypt
import os
print("\033[1;34m##################################################")
print("##                                              ##")
print("##  88      a8P         db        88        88  ##")
print("##  88    .88'         d88b       88        88  ##")
print("##  88   88'          d8''8b      88        88  ##")
print("##  88 d88           d8'  '8b     88        88  ##")
print("##  8888'88.        d8YaaaaY8b    88        88  ##")
print("##  88     '88.   d8'        '8b  88        88  ##")
print("##  88       Y8b d8'          '8b 888888888 88  ##")
print("##                                              ##")
print("####  ############# ARYOSE #######################")
print("\n\033[1;33m[*]Encrypting files alongside the CRYPT tool")



while True:
    terminal = input("\n\033[1;31m (CRYPT@ROOT - [~]) " + Fore.RESET)
    
    if terminal.lower() == "exit":
        exit()
    
    try:
        run(terminal, shell=True)
        
        if terminal.lower() == "crypt":
            os.system("clear")
            print("\t\t\033[1;31m░█████╗░██████╗░██╗░░░██╗██████╗░████████╗")
            print("\t\t\033[1;31m██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝")
            print("\t\t\033[1;31m██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░")
            print("\t\t\033[1;31m██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░")
            print("\t\t\033[1;31m╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░")
            print("\t\t\033[1;31m░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░")
            
            x = input("\033[1;31m\nThis will encrypt your files [y/n]: ").lower()
            if x == "y":
                path_folder = "."
                for file_name in os.listdir(path_folder):
                    path_file = os.path.join(path_folder, file_name)
                    if os.path.isfile(path_file):
                        if path_file == "./terminal.py":
                            continue
                        else:
                            pyAesCrypt.encryptFile(path_file, f"{path_file}.aes", "root", 64 * 1024)
                            os.remove(path_file)
                            print(Fore.GREEN + "The operation was successfully completed")
    except FileNotFoundError:
        print(Fore.RED + "Command not found")