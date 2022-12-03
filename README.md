# bumfuzzleOS
![GitHub](https://img.shields.io/github/license/aarikpokras/bumfuzzleOS) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/aarikpokras/bumfuzzleOS) ![Maintenance](https://img.shields.io/maintenance/yes/2022)
## Installation
Did you know that to bumfuzzle means to confuse?
Bumfuzzle (aka fuzz) is available for all UNIX-like operating systems that can support Python.
### MacOS
To install Python, run `brew install python3`. I know brew is *really* slow, but unless you know a better way to get Python, it's the only way.
You can use wget or <a href = "https://github.com/aarikpokras/bumfuzzleos/archive/refs/heads/main.zip">download</a> the repo.
`wget https://github.com/aarikpokras/bumfuzzleos/archive/refs/heads/main.zip`
### Linux and Others
To install Python, you can use `apt` or your standard package manager.

`sudo apt install python3`, `sudo yay -S python3`, `sudo yum -S python3`, etc.
## Running
To run on any system, you can use `python3`. It is recommended to clear the shell before you run it. Use `cd` to enter the bumfuzzleOS directory.

`clear;python3 fuzz.py`
