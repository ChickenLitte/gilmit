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
from colorama import Fore, Back, Style, init

class VersionControl:
    
    def __init__(self):#initialize empty file and version history tree

        self.files = OrderedMap()
        self.old_input = input#store the old input function
        init(autoreset=True)#for the colors

    def saveCurrent(self, filename, file):#save the current version of the file

        if self.files.__contains__(filename):#if the file already exists, add the new version

            file_entry = self.files.__getitem__(filename)
            self.version = file_entry.__len__()
            file_entry.__setitem__(self.version, StringDiff(file_entry.__getitem__(self.version-1), file))#add the new version

        else:#if the file version doesn't already exist, create it

            # Make sure that the value for the filename key is an OrderedMap
            self.files.__setitem__(filename, OrderedMap())
            self.version = 0
            self.files.__getitem__(filename).__setitem__(self.version,file)#add the new version

        self.input("saved file: " + filename + ", version: " + str(self.version) + " \n", True)#print a confirmation

    def restoreVersion(self, filename, version):#returns the restored version, iterative; could be recursive
        
        restoredFile = self.files.__getitem__(filename).__getitem__(0)
        for key in list(self.files.__getitem__(filename).tree.keys())[1:]:
            restoredFile = StringDiff.apply_diff(restoredFile, self.files.__getitem__(filename).__getitem__(key))
            if key == version:
                break
        
        return restoredFile
            
    
    def returnLog(self):

        self.input("returning log:\n",True)
        
        for key in self.files.tree.keys():#print the file names

            copy = key
            self.input("- file: " + str(key) + "\n",True)

            for key2 in self.files.__getitem__(copy).tree.keys():#print the version history of the file

                self.input("   - version: " + str(key2),True)
                self.input("diff: " + str(self.files.__getitem__(copy).__getitem__(key2)) + "\n",True)
            
    def input(self, str, inPUT = False):#acts as both a print and input function, with a dramatic slow type effect
            
            i = 0
            # print(len(str))

            while i < (len(str) - 1):#slowly print the string

                print(Fore.BLACK + Back.WHITE + Style.BRIGHT,str[i], sep='', end='', flush=True)#no endline,hopefully with colors
                sleep(0.025)
                i += 1
            
            if inPUT:#use the old input function for the last character
                print(Fore.BLACK + Back.WHITE + Style.BRIGHT, str[i], sep='', end='', flush=True)#just a normal printfunction
                return 
            
            return self.old_input(str[i])#return the input from the user

def main():

    vc = VersionControl()#initialize the vc system
    
    name = vc.input(str = "Who should I store these files after?\n > ")#get the user's name
    command = vc.input("\nHello " + name + ", here are the commands:\n - save file \n - restore version \n - print log \n - exit \n\n What would you like to do? \n > ")#ask for the initial command
    commandList = {"save file":vc.saveCurrent,"restore version":vc.restoreVersion, "print log":vc.returnLog, "exit":exit}# a dictionary linking user commands and actions for the program
    
    insultList = [#for laughs, random insults
        "Who taught " + name + " how to type!",
        "Oh brother, get this " + name + " guy outa here! \n",
        "Erm, " + name + " what the \u03A3",
        "You're not very good at this, are you " + name + "?\n",
        "Boy, " + name + ", someone needs to go back to typing school!\n",
        "Congrats, " + name +  " you're the worst typer I've ever seen!\n",
        name + " how would your mother feel about your typing skills?\n",
        name + " Are your fingers fat?\n",
        "You know " + name + ", they say, on the internet, no one knows you're a dog, but now I'm inclined disagree\n"
        ]
    
    while True:#run the UI until the user exits
        
        if command == "exit":#builtin quit function

            vc.input("\nGoodbye " + name + "!\n", True)
            exit()

        while command not in commandList:#if the user writes a type, insult them and give them a list of options

            command = vc.input(random.choice(insultList) + "\nHere are the commands:\n - save file \n - restore version \n - print log \n - exit \n What would you like to do? \n > ")

        if (command != "print log") and (command != "exit") and (command != "restore version"):#for the "normal" commands

            filename = vc.input("\nWhat's the file name?\n > ")
            file = vc.input("\nWhat's the file?\n > ")
            commandList[command](filename,file)

        elif command == "restore version":#needs a special case for the restore version command

            filename = vc.input("\nWhat's the file name?\n > ")
            version = vc.input("\nWhat's the version?\n > ")

            vc.input("\nRestored version: " + version + " of file: " + filename + ":\n", True)
            vc.input("      "+ commandList[command](filename,version) + "/n", True)

        else:

            commandList[command]()

        #repeat the process
        command = vc.input("\nWhat would you like to do next?\n" + " here are the commands:\n - save file \n - restore version \n - print log \n - exit \n What would you like to do? \n > ")

if __name__ == "__main__":
    main()