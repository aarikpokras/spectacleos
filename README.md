<!--# spectacleOS Kilimanjaro-->

<img src="https://github.com/aarikpokras/dmgs/blob/main/specs-head-OF.png?raw=true" alt="spectacleOS Kilimanjaro">

Current version: Kilimanjaro v5.2.0

![Fuzz](https://img.shields.io/badge/spectacleos-The%20lightest%20operating%20system-5993ff?style=for-the-badge)

![GitHub](https://img.shields.io/github/license/aarikpokras/spectacleos) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/aarikpokras/spectacleos) ![Maintenance](https://img.shields.io/maintenance/yes/2023)
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

### ***Please make sure that you are in the spectacleos directory before running any executables.***

If you just downloaded it, run `chmod -R 755 spectacleos` in the folder that contains spectacleOS.

`cd` into the spectacleos directory.

Run `./first-time` and follow the instructions.

You can open menu.html for a graphical menu.

For information on the Migration Assistant, refer to the [wiki](https://github.com/aarikpokras/spectacleos/wiki/Migration-Assistant-(Migrator)).

To run on any system, you can use `python3`. It is recommended to clear the shell before you run it. Use `cd` to enter the spectacleOS directory.

Unzip the wgetted file. It is saved as 'spectacleos.zip'. `unzip path/to/zip.zip`

Make sure to run `fuzz.py` first.

`clear;python3 fuzz.py`

<br />
<br />

Made *by* a real person, *for* real people.
