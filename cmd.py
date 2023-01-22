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
        elif cmdLine == "dirn":
                print(os.getcwd())
        elif cmdLine == "dir":
                print(os.listdir())
        elif cmdLine == "chdir":
                chPath=input("Path> ")
                os.chdir(chPath)
        elif cmdLine == "fe":
                feName=input("What to name file? Or if file already exists, type name here. Current working directory is "+os.getcwd()+".> ")
                feOption=input("Append or overWrite? a/w> ");
                f = open(feName, feOption)
                fText=input("FuzzEdit:Enter text, press enter> ")
                f.write(fText)
                print("Reading file.")
                f = open(feName, "r")
                print(f.read())
                print("🔔 This file is located in "+os.getcwd()+".")
        elif cmdLine == "help":
                help=open("../../bin/help.txt", "r")
                print(help.read())
        elif cmdLine == "exit":
                exit()
        elif cmdLine == "echo":
                echoI=input("echo> ")
                print(echoI)
        elif cmdLine == "makef":
                makeFi=input("makef> ")
                os.mkdir(makeFi)
                print("🔔 This folder is located in "+os.getcwd()+"/exit"+makeFi+".")
        elif cmdLine == "fe -read":
                feRead=input("Input filename. 🔔 The current working directory is "+os.getcwd()+".> ")
                ferr = open(feRead, "r")
                print(ferr.read())
        elif cmdLine == "cls":
                def cls():
                        os.system('clear')
                cls()
        elif cmdLine == "rm":
                rmChoice=input("rm-file> ")
                os.remove(rmChoice) 
        elif cmdLine == "rm -fo":
                rmChoice=input("rm-directory> ")
                os.rmdir(rmChoice) 
        elif cmdLine == "math":
                print('Type "eva" to input a raw expression.')
                num1=input("Number 1> ")
                if num1 == "eva":
                        nnu=input("==> ")
                        print(eval(nnu))
                num2=input("Number 2> ")
                numop=input("Operation> ")
                print(eval(num1+numop+num2))
        elif cmdLine == "open":
                print("Input filepath.\n")
                opench=input("open> ")
                os.system('open ' + opench)
        elif cmdLine == "open --args":
                openchs=input("filepath> ")
                openarg=input("args> ")
                os.system('open ' + openchs + " " + "'" + openarg + "'")
        elif cmdLine == "webcon":
                webconp=input("webcon> ")
                os.system("curl " + webconp)
        elif cmdLine == "custcol":
                custcolc=input("Enter color: ")
                if custcolc == "default":
                        print("\033[0m")
                elif custcolc == "black":
                        print("\033[1;30m")
                elif custcolc == "red":
                        print("\033[1;31m")
                elif custcolc == "green":
                        print("\033[1;32m")
                elif custcolc == "yellow":
                        print("\033[1;33m")
                elif custcolc == "blue":
                        print("\033[1;34m")
                elif custcolc == "purple":
                        print("\033[1;35m")
                elif custcolc == "cyan":
                        print("\033[1;36m")
                elif custcolc == "white":
                        print("\033[1;37m")
                else:
                        print("Colors:\ndefault\nblack\nred\ngreen\nyellow\nblue\npurple\ncyan\nwhite")
        elif cmdLine == pass:
                print()
        elif cmdLine == "shutdown":
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
        else:
                print("specs: " + cmdLine + ": Command not found. Type `help` for help.")
        # IMPORTANT STUFF BELOW
        if os.path.basename(os.getcwd()) != start.signInUn:
                print("You've exited the home directory. Some commands like `help` will not work.")
