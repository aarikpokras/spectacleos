import platform
import os
import time
print("Please cd to the spectacleOS directory.")
grubChoice=input('____________________________________________________\n | Boot Menu for spectacleOS     						  |\n | '+platform.platform()+'	       						 		 |\n | Run spectacleOS				r		       						  |\n | spectacleOS tutorial				t		       						  |\n | Exit						e		    	   					  |\n |							       						  |\n |___________________________________________________ |\n>>> ')
if grubChoice == "r":
    print("Booting spectacleOS...")
    if os.path.basename(os.getcwd()) != 'spectacleos':
        print('Not in proper directory. Exiting.')
        exit()
    time.sleep(1)
    import fuzz
