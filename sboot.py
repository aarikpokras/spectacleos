import platform
import os
import time
grubChoice=input('____________________________________________________\n | Boot Menu for spectacleOS     						  |\n | '+platform.platform()+'	       						 		 |\n | Run spectacleOS				r		       						  |\n | spectacleOS tutorial				t		       						  |\n | Exit						e		    	   					  |\n |							       						  |\n |___________________________________________________ |\n>>> ')
if grubChoice == "r":
    print("Booting spectacleOS...")
    if os.path.basename(os.getcwd()) != 'spectacleos':
        print('Not in proper directory. Please point the terminal to the "spectacleos" directory.')
        time.sleep(1)        
        exit()
    time.sleep(1)
    import fuzz
if grubChoice == "t":
    import tut
if grubChoice == "e":
    exit()
