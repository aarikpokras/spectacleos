import os
import maskpass
from version import ver
# vers=version.ver
print("Welcome to spectacleOS! This is version "+ver+" command line.")
name=input('Enter desired hostname. ==> ')
user=input('Sign in as existing user, create new user, or bypass? s/c/b> ')
if user == "c":
    newUserNameUn=input("Enter new user's username. This will be the name on the home folder: ")
    newUserName=input("Enter "+newUserNameUn+"'s full name: ")
    newUserPw=input("Enter "+newUserName+"'s password.")
    os.chdir('home')
    os.mkdir(newUserNameUn)
    os.chdir(newUserNameUn)
    pwF = open("pw", "w")
    pwText=newUserPw
    pwF.write(pwText)
    print("Returning Password.")
    pwF = open("pw", "r")
    pwRead=pwF.read()
    print(pwRead)
    print("Account successfully created. Please sign in. Exiting.")
    exit()
if user == "s":
    signInUn=input("Username> ")
    os.system('sudo chmod +rw home/'+signInUn+'/pw')
    #os.chdir('home/'+signInUn)
    pwReadS = open("home/"+signInUn+"/pw", "r")
    signInPw=maskpass.askpass(prompt='Enter Password: ', mask='*')
    if pwReadS.read() == signInPw:
        os.chdir("home/"+signInUn)
        print("Sign-in ok. Welcome to spectacleOS, "+signInUn+"! Remember, you are responsible for doing `chmod -rw` on your password file!")
        import cmd
    if pwReadS.read() != signInPw:
        print("Sign-in failed.")
        exit()


# Make continous imports of py files to make full command line file - import variables with import <filename>, then to import variables, <new-var-name>=<filename>.<old-var-name>
