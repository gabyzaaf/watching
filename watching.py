import time;
import shutil;
import datetime;
import os;
import argparse, sys
import platform;

class File:
    def __init__(self,file_path,folder_path):
        if os.path.isfile(file_path)==False:
            raise Exception('The --file is not a file on your computer')
        if os.path.isdir(folder_path) == False:
            raise Exception('The --destFolder not exist on your computer')
        if "Windows" in platform.system():
            print("Is Windows")
            paths = file_path.split('\\')
            self.fileName = paths[len(paths)-1]
        if "Darwin" in platform.system() or "Linux" in platform.system():
            print(platform.system())
            paths = file_path.split('/')
            self.fileName = paths[len(paths) - 1]
        self.file_path = file_path
        self.folder_path = folder_path

    def read(self,path):
        with open(path) as file:
            content = file.readlines();
        return content

    def execute(self):
        exist = True
        old = ""
        while exist:
            time.sleep(3)
            exist = os.path.isfile(self.file_path)
            if exist:
                current = self.read(self.file_path)
            if current != old:
                shutil.copyfile(self.file_path, self.folder_path + str(datetime.datetime.now()) + "-"+self.fileName)
                old = current
        if exist == False:
            raise Exception('The file is deleted')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file',type=str,help='The file to watch')
    parser.add_argument('--destFolder', type=str,help='The folder where make the copy')
    args = parser.parse_args()
    f = File(args.file,args.destFolder)
    f.execute()