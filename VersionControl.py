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

    def saveCurrent(self, filename, file):

        if self.files.__contains__(filename):
            self.fileChange = StringDiff(self.files.getitem(filename).getitem(self.files.getitem(filename).len()),file)
            self.version = self.files.getitem(filename).len() + 1
            self.files.getitem(filename).setitem(self.version,self.fileChange)
        else:
            self.versions = OrderedMap()
            self.version = 0
            self.files.__setitem__(0,file)
        

        self.input("saved file: " + filename + ", version: " + str(self.version) + " \n", True)

    def restoreVersion(self, file, version):#returns the restored version, recursive

        print("restoring version", "file:" + file + "version:", version)
        print("restore version", "file:" + file + "version:", version)
    
    def returnLog(self):

        self.input("returning log:",True)
        
        for key in self.files.tree.keys():
            self.input("file: " + str(key) + "\n",True)
            for key2 in self.files.__getitem__(key).tree.__keys__():
                self.input("version: " + str(key2) + "\n",True)
                self.input(self.files.__getitem__(key).__getitem__(key2).apply_diff(self.files.__getitem__(key).__getitem__(key2).__len__()),True)
            self.input("\n",True)
            
    def input(self, str, inPUT = False):
            i = 0
            # print(len(str))
            while i < (len(str) - 1):
                print(str[i], sep='', end='', flush=True)
                sleep(0.01)
                i += 1
            
            if inPUT:
                print(str[i], sep='', end='', flush=True)
                return 
            return self.old_input(str[i])

def main():
    vc = VersionControl()
    
    name = vc.input(str = "Who should I store these files after?\n > ")
    command = vc.input("Hello " + name + ", here are the commands:\n - save file \n - restore version \n - print log \n - exit \n What would you like to do? \n > ")
    commandList = {"save file":vc.saveCurrent,"restore version":vc.restoreVersion, "print log":vc.returnLog}
    
    insultList = [
        "Who taught " + name + " how to type!",
        "Oh brother, get this " + name + " guy outa here! \n",
        "Erm, " + name + " what the \u03A3"
        ]
    
    while True:
        if command == "exit":
            vc.input("Goodbye " + name + "!\n", True)
            exit()
        while command not in commandList:
            command = vc.input(random.choice(insultList) + "\nHere are the commands:\n - save file \n - restore version \n - print log \n - exit \n What would you like to do? \n > ")
        if command != "print log":
            filename = vc.input("What's the file name?\n > ")
            file = vc.input("What's the file?\n > ")
            commandList[command](filename,file)
        else:
            commandList[command]()
        command = vc.input("What would you like to do next?\n" + " here are the commands:\n - save file \n - restore version \n - print log \n - exit \n What would you like to do? \n > ")

if __name__ == "__main__":
    main()