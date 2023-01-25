printf "\033[1;31mWait\! spectacleOS graphics'll only work on a GUI. Sorry about that.\033[0m\n"
printf "\033[1;37mThis program will install spectacleOS on your computer. If you don't want to do this, hit ^Z now.\033[0m\n"
sleep 2
if [ $(command -v python3) -z ]
then
printf "\033[1;31mPlease get Python 3.\033[0m\n" >&2
exit 2
else
  if [ $(command -v rlwrap) -z ]
  then
  printf "\033[1;31mPlease get rlwrap. You can run `\sudo apt-get install rlwrap`\, or \`brew install rlwrap\`.\n"
  else
    printf "\033[1;37mCongrats! \033[1;32mYou\'ve passed all the checks! Now, this program will use cURL to get the zip from the repository @ aarikpokras/spectacleos. If you don't want to do this, hit ^Z now.\033[0m\n"
    sleep 2
    curl -L -o spectacleos.zip https://github.com/aarikpokras/spectacleos/archive/refs/heads/master.zip
    printf "\033[1;37mNow, please unzip the file. I\'ll wait for you to do that.\033[0m\n"
    sleep 2
    printf "\033[1;37mHi there\! Me again. Now, please rename the folder you\'ve unzipped to \'spectacleos\'. I\'ll wait for you to do that.\033[0m\n"
    sleep 2
    printf "\033[1;37mDone\? Ok, good. Now wait as I run something real quick.\n"
    chmod -R 755 spectacleos
    printf "\033[1;32mDone with that\!\033[1;37m Ok, so now I want you to enter the spectacleos directory and run \`./first-time\`.\033[0m\n"
    sleep 2
    printf "\033[1;37mLooking good? Ok. So, now, run \`./specs start\`.\033[0m You\'re done\! Bye!\n"
  fi
fi
