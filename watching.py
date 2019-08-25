import time;
import shutil;
import datetime;
import os;
path = "/Users/zaafranigabriel/PycharmProjects/Watching/samples/sample.txt";
newPath = "/Users/zaafranigabriel/PycharmProjects/Watching/save/"

def read(path):
    with open(path) as file:
        content = file.readlines();
    return content

exist = True
old = ""
while exist :
    time.sleep(3)
    exist = os.path.isfile(path)
    if exist :
        current = read(path)
        if current != old:
            print("NOT EQUAL")
            shutil.copyfile(path,newPath+str(datetime.datetime.now())+"-sample.txt")
            old = current
        else:
            print("Equal")

