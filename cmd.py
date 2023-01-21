import os
import maskpass
import start
import signal
name=start.name


value=True # Repeats command line infinitely
while (value):
        cmdLine=input(name+" "+os.getcwd()+': '+start.signInUn+'$ ')
        if cmdLine == "fuzzver":
                vvCmd=open("version-gui.txt", "r")
                print(vvCmd.read())
        if cmdLine == "dirn":
                print(os.getcwd())
        if cmdLine == "dir":
                print(os.listdir())
        if cmdLine == "chdir":
                chPath=input("Path> ")
                os.chdir(chPath)
        if cmdLine == "fe":
                feName=input("What to name file? Or if file already exists, type name here. Current working directory is "+os.getcwd()+".> ")
                feOption=input("Append or overWrite? a/w> ");
                f = open(feName, feOption)
                fText=input("FuzzEdit:Enter text, press enter> ")
                f.write(fText)
                print("Reading file.")
                f = open(feName, "r")
                print(f.read())
                print("🔔 This file is located in "+os.getcwd()+".")
        if cmdLine == "help":
                help=open("../../bin/help.txt", "r")
                print(help.read())
        if cmdLine == "exit":
                exit()
        if cmdLine == "echo":
                echoI=input("echo> ")
                print(echoI)
        if cmdLine == "makef":
                makeFi=input("makef> ")
                os.mkdir(makeFi)
                print("🔔 This folder is located in "+os.getcwd()+"/exit"+makeFi+".")
        if cmdLine == "fe -read":
                feRead=input("Input filename. 🔔 The current working directory is "+os.getcwd()+".> ")
                ferr = open(feRead, "r")
                print(ferr.read())
        if cmdLine == "cls":
                def cls():
                        os.system('clear')
                cls()
        if cmdLine == "rm":
                rmChoice=input("rm-file> ")
                os.remove(rmChoice) 
        if cmdLine == "rm -fo":
                rmChoice=input("rm-directory> ")
                os.rmdir(rmChoice) 
        if cmdLine == "math":
                print('Type "eva" to input a raw expression.')
                num1=input("Number 1> ")
                if num1 == "eva":
                        nnu=input("==> ")
                        print(eval(nnu))
                num2=input("Number 2> ")
                numop=input("Operation> ")
                print(eval(num1+numop+num2))
        if cmdLine == "open":
                print("Input filepath.\n")
                opench=input("open> ")
                os.system('open ' + opench)
        if cmdLine == "open --args":
                openchs=input("filepath> ")
                openarg=input("args> ")
                os.system('open ' + openchs + " " + "'" + openarg + "'")
        if cmdLine == "webcon":
                webconp=input("webcon> ")
                os.system("curl " + webconp)
        if cmdLine == "shutdown":
                shutPw=maskpass.askpass(prompt='Enter Password: ', mask='*')
                if shutPw == start.signInPw:
                        yorn=input("Enter sboot? y/n> ")
                        if yorn == "y":
                                def cls():
                                        os.system('clear')
                                cls()
                                import sboot
                        if yorn == "n":
                                print("Aborted.")
                else:
                        print("Unauthorized.")
        # IMPORTANT STUFF BELOW
        if os.path.basename(os.getcwd()) != start.signInUn:
                print("You've exited the home directory. Some commands like `help` will not work.")
