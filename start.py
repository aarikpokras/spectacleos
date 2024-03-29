import os
import maskpass
import bcrypt
from version import ver
# def checkpw(pw: str) -> str:
#     with open(f"home/{signInUn}/pw", "r") as f:
#         return bcrypt.checkpw(pw.encode(), f.read().encode())
# vers=version.ver
print("Welcome to spectacleOS! This is version "+ver+" command line.")
name=input('Enter desired hostname. ==> ')
user=input('Sign in as existing user or create a new one? s/c> ')
if user == "c":
    newUserNameUn=input("Enter new user's username. This will be the name on the home folder: ")
    newUserName=input("Enter "+newUserNameUn+"'s full name: ")
    newUserPw=input("Enter "+newUserName+"'s password> ")
    os.chdir('home')
    os.mkdir(newUserNameUn)
    os.chdir(newUserNameUn)
# KEEP IF NO AUTOMATIC PR MERGE
#
    pwF = open("pw", "wb")
    pwText=newUserPw
    bytes=newUserPw.encode('utf-8')
    salt=bcrypt.gensalt()
    hash=bcrypt.hashpw(bytes, salt)
    pwF.write(hash)
#
# KEEP IF NO AUTOMATIC PR MERGE
    print("Account successfully created. Please sign in. Exiting.")
    exit()
if user == "s":
    signInUn=input("Username> ")
    os.system('sudo chmod +rw home/'+signInUn+'/pw')
    #os.chdir('home/'+signInUn)
#    pwReadS = open("home/"+signInUn+"/pw", "r")
#    signInPw=maskpass.askpass(prompt='Enter Password: ', mask='*')
#    if pwReadS.read() == signInPw:
#        os.chdir("home/"+signInUn)
#        print("Sign-in ok. Welcome to spectacleOS, "+signInUn+"! Remember, you are responsible for doing `chmod -rw` on your password file!")
#        import cmd
#    if pwReadS.read() != signInPw:
#        print("Sign-in failed.")
#        exit()

# KEEP IF NO AUTOMATIC PR MERGE
#
    pwReadS = open("home/"+signInUn+"/pw", "rb")
    pwFullRead=pwReadS.read()
    signInPw=maskpass.askpass(prompt='Enter Password: ', mask='*')
    salt=bcrypt.gensalt()
    bytes=signInPw.encode('utf-8')
#    hashnew=bcrypt.hashpw(bytes, salt)
    bcrypt.checkpw(bytes, pwFullRead)
    if bcrypt.checkpw(bytes, pwFullRead):
        os.chdir("home/"+signInUn)
        print("Sign-in ok. Welcome to spectacleOS, "+signInUn+"!")
    if bcrypt.checkpw(bytes, pwFullRead) == False:
        print("Username or password incorrect. Exiting.")
        exit()
#    if pwReadS.read() != hashnew:
#        print('no.')
#    elif pwReadS.read() == hashnew:
#        os.chdir("home/"+signInUn)
#        print ("Sign-in ok. Welcome to spectacleOS, "+signInUn+"!")
#    if checkpw == signInPw:
#        os.chdir("home/"+signInUn)
#        print("Sign-in ok. Welcome to spectacleOS, "+signInUn+"! Remember, you are responsible for doing `chmod -rw` on your password file!")
        import cmd
#    if pwReadS.read() != signInPw:
#        print("Sign-in failed.")
#        exit()
# KEEP IF NO AUTOMATIC PR MERGE

# Make continous imports of py files to make full command line file - import variables with import <filename>, then to import variables, <new-var-name>=<filename>.<old-var-name>
