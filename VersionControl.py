# save versions of file
# store version history of multiple files
# restore prev. versions
# see a log of changes

# OderedMap
# StringDiff, only init and apply_diff
# AVLTree, AVLCodec
# HuffmanFile

from friendsbalt.acs import AVLTree, StringDiff, OrderedMap#, HuffmanFile
from time import sleep
import random

class VersionControl:
    
    def __init__(self):#initialize empty file and version history tree
        self.files = OrderedMap()
        self.old_input = input

    def saveCurrent(self, file, version):#do
        print("saving current", "file:" + file + "version:", version)
        # if self.files.contains(key):
        #     pass
        # else:
        #     self.version = OrderedMap()
        #     self.files.setitem(key,value)
        print("saved", "file:" + file + "version:", version)

    def restoreVersion(self, file, version):#returns the restored version, recursive
        print("restoring version", "file:" + file + "version:", version)
        print("restore version", "file:" + file + "version:", version)
    
    def returnLog(self):#
        print("returning log")

    def input(self, str):
            i = 0
            # print(len(str))
            while i < (len(str) - 1):
                print(str[i], sep='', end='', flush=True)
                sleep(0.05)
                i += 1
            return self.old_input(str[i])

def main():
    vc = VersionControl()
    
    name = vc.input(str = "Who should I store these files after?\n > ")
    command = vc.input("Hello " + name + " here are the commands:\n - save file \n - restore version \n - print log \n What would you like to do? \n > ")
    commandList = {"save file":vc.saveCurrent,"restore version":vc.restoreVersion, "print log":vc.returnLog}
    
    insultList = [
        "Who taught " + name + " how to type!",
        "Oh brother, get this \n" + name + " guy outa here! \n",
        "Erm, " + name + " what the \u03A3"
        ]
    
    while command not in commandList:
        command = vc.input(random.choice(insultList) + "\nHere are the commands:\n - save file \n - restore version \n - print log \n What would you like to do? \n > ")
    if command != "print log":
        file = vc.input("What's the file name?\n > ")
        version = vc.input("What's the file version?\n > ")
    else:
        file, version = None,None
    commandList[command](file,version)

if __name__ == "__main__":
    main()