# spectacleOS Kilimanjaro
<img src="https://i.ibb.co/3dPytT2/specs.png" alt="spectacleOS logo" width="200">

Current version: Kilimanjaro v5.0.0

![Fuzz](https://img.shields.io/badge/spectacleos-The%20lightest%20operating%20system-5993ff?style=for-the-badge)

![GitHub](https://img.shields.io/github/license/aarikpokras/spectacleos) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/aarikpokras/spectacleos) ![Maintenance](https://img.shields.io/maintenance/yes/2022)
## Installation
You can get the latest release [here](https://github.com/aarikpokras/spectacleos/releases), or use `curl` to get the zip from GitHub.

Spectacle is available for all UNIX-like operating systems that can support Python.
**It is recommended to grab the latest release from the releases page (Rather than `curl`ing), because those will be the most up-to-date. [Learn More](nocurl.md)**

***Please* do not download the zip from the "code" tab. Please.**
### MacOS
To install Python, run `brew install python3`. I know brew is *really* slow (if you haven't updated it in a while), but unless you know a better way to get Python, it's the only way.

You can use git to download the repo.

```console
git clone git@github.com:aarikpokras/spectacleos.git
```
### Linux and Others
To install Python, you can use `apt` or your standard package manager.

`sudo apt install python3`, `sudo yay -S python3`, `sudo yum -S python3`, etc.

```console
git clone git@github.com:aarikpokras/spectacleos.git
```
## Running
To run on any system, you can use `python3`. It is recommended to clear the shell before you run it. Use `cd` to enter the spectacleOS directory.

Unzip the wgetted file. It is saved as 'spectacleos.zip'. `unzip path/to/zip.zip`

Make sure to run `fuzz.py` first.

`clear;python3 fuzz.py`

<br />
<br />

Made *by* a real person, *for* real people.
