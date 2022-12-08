import requests
updver=requests.get(url = 'https://ninth-destiny-mare.glitch.me/specsver').text

if updver == "3.0.1":
    print("██ spectacleOS is up to date. ██")
else:
    print("██ Not up to date. Please update at https://github.com/aarikpokras/spectacleos. ██")
    
