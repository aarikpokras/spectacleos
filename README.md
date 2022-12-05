# spectacleOS 
<img src="https://i.ibb.co/3dPytT2/specs.png" alt="spectacleOS logo" width="200">

![Fuzz](https://img.shields.io/badge/spectacleos-The%20lightest%20operating%20system-5993ff?style=for-the-badge)

![GitHub](https://img.shields.io/github/license/aarikpokras/spectacleos) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/aarikpokras/spectacleos) ![Maintenance](https://img.shields.io/maintenance/yes/2022)
## Installation
You can get the latest release [here](https://github.com/aarikpokras/spectacleos/releases), or use `wget` to get the zip from GitHub.

Spectacle is available for all UNIX-like operating systems that can support Python.
**It is recommended to use `wget` to get the repo zip, because it will save to your home folder.**
### MacOS
To install Python, run `brew install python3`. I know brew is *really* slow, but unless you know a better way to get Python, it's the only way.

You can use wget or <a href = "https://github.com/aarikpokras/spectacleos/archive/refs/heads/main.zip">download</a> the repo.

`wget -O spectacleos.zip https://github.com/aarikpokras/spectacleos/archive/refs/heads/main.zip`
### Linux and Others
To install Python, you can use `apt` or your standard package manager.

`sudo apt install python3`, `sudo yay -S python3`, `sudo yum -S python3`, etc.

`wget -O spectacleos.zip https://github.com/aarikpokras/spectacleos/archive/refs/heads/main.zip`
## Running
To run on any system, you can use `python3`. It is recommended to clear the shell before you run it. Use `cd` to enter the spectacleOS directory.

Unzip the wgetted file. It is saved as 'spectacleos.zip'. `unzip path/to/zip.zip`

Make sure to run `fuzz.py` first.

`clear;python3 fuzz.py`
