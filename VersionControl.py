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
            file_entry = self.files.__getitem__(filename)
            self.version = file_entry.__len__()
            file_entry.__setitem__(self.version, StringDiff(file_entry.__getitem__(self.version-1), file))
        else:
            # Ensure the value for the filename key is an OrderedMap
            self.files.__setitem__(filename, OrderedMap())
            self.version = 0
            self.files.__getitem__(filename).__setitem__(self.version,file)

        self.input("saved file: " + filename + ", version: " + str(self.version) + " \n", True)

    def restoreVersion(self, filename, version):#returns the restored version, recursive
        
        restoredFile = self.files.__getitem__(filename).__getitem__(0)
        for key in list(self.files.__getitem__(filename).tree.keys())[1:]:
            restoredFile = StringDiff.apply_diff(restoredFile, self.files.__getitem__(filename).__getitem__(key))
            if key == version:
                break
        
        return restoredFile
            
    
    def returnLog(self):

        self.input("returning log:\n",True)
        
        for key in self.files.tree.keys():
            copy = key
            self.input("- file: " + str(key) + "\n",True)
            for key2 in self.files.__getitem__(copy).tree.keys():
                self.input("   - version: " + str(key2),True)
                self.input("diff: " + str(self.files.__getitem__(copy).__getitem__(key2)) + "\n",True)
            
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
    command = vc.input("\nHello " + name + ", here are the commands:\n - save file \n - restore version \n - print log \n - exit \n What would you like to do? \n > ")
    commandList = {"save file":vc.saveCurrent,"restore version":vc.restoreVersion, "print log":vc.returnLog, "exit":exit}
    
    insultList = [
        "Who taught " + name + " how to type!",
        "Oh brother, get this " + name + " guy outa here! \n",
        "Erm, " + name + " what the \u03A3"
        ]
    
    while True:
        if command == "exit":
            vc.input("\nGoodbye " + name + "!\n", True)
            exit()
        while command not in commandList:
            command = vc.input(random.choice(insultList) + "\nHere are the commands:\n - save file \n - restore version \n - print log \n - exit \n What would you like to do? \n > ")
        if (command != "print log") and (command != "exit") and (command != "restore version"):
            filename = vc.input("What's the file name?\n > ")
            file = vc.input("What's the file?\n > ")
            commandList[command](filename,file)
        elif command == "restore version":
            filename = vc.input("What's the file name?\n > ")
            version = vc.input("What's the version?\n > ")
            vc.input("\nRestored version: " + version + " of file: " + filename + ":\n", True)
            vc.input("      "+ commandList[command](filename,version) + "/n", True)
        else:
            commandList[command]()
        command = vc.input("\nWhat would you like to do next?\n" + " here are the commands:\n - save file \n - restore version \n - print log \n - exit \n What would you like to do? \n > ")

if __name__ == "__main__":
    main()