# piSingleSwitchRadio

...is a simple script that transforms your Raspberry Pi into an Internet radio receiver controllable with just one switch connected to the GPIO pins. **If you have a reset/power switch from an old computer case lying around, it could be one of the easiest Pi projects utilizing the GPIO pins!**

- It fetches your favourite Internet radio stations list from the JSON file,
- short click of the switch - turn on/change the station,
- it reads the radio station name with speech synthesizer,
- long press of the switch (more than 1 sec) - turn off.

Ingredients:
- **Raspberry Pi** (developed and tested on the Pi 1 B+ model, should work flawlessly on the newer models),
- **Hi-Fi set** or a boombox or whatever that could play music,
- **switch** (eg. from an old PC case),
- **cable** to connect RPi and Hi-Fi set,
- **piSingleSwithRadio.py** and **piSingleSwithRadio.json** files somewhere in your home directory (most cases /home/pi).

## Let's do some tinkering...

### 1. Connect switch to the Raspberry Pi 

asdasdasdasdasd

### 2. Connect RPi to your Hi-Fi set

asdasdasdasd

### 3. Tidy everything 

asdasdasdasdasd

## Configuring environment

### 1. Install required packages

Following script runs **only on Raspberry Pi**. It also requires *mpv* and *espeak* packages. Install it by following console commands:
```sh
$ sudo apt install mpv
$ sudo apt install espeak
```

### 2. Deploy piSingleSwitchRadio script

Put **piSingleSwithRadio.py** and **piSingleSwithRadio.json** files somewhere in your home directory (most cases /home/pi).
Then set executable bit on **piSingleSwithRadio.py** script by:
```sh
$ chmod +x ~/piSingleSwithRadio.py
```
Now you can launch piSingleSwithRadio manualy by:
```sh
$ ~/piSingleSwithRadio.py
```
Or add following commands to your startup scripts
```sh
pkill radio #POPRAWIĆ
~/piSingleSwithRadio.py
```
### 3. Configure radio stations
Configuration file looks like this:
```json
[
	{
		"name": "BBC Radio 1",
		"lang": "en",
		"url": "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p"
	},
	{
		"name": "BBC Radio 2",
		"lang": "en",
		"url": "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio2_mf_p"
	},
	{
		"name": "Yorkshire Coast Radio",
		"lang": "en",
		"url": "http://str1.sad.ukrd.com/yorkshirecoast.m3u"
	},
	{
		"name": "France Musique Classique plus",
		"lang": "fr",
		"url": "http://www.listenlive.eu/fr_francemusiqueplus.m3u"
	}	
]
```
It's basicly json array of objects. One object represents a radio station. 
- **name**: name of the radio station (speech synthesizer reads it)
- **lang**: language of the radio statnion name (for speech synthesizer)
- **url**: URL of the radio stream

**Where to find radio statnions?**

Personaly I use [www.listenlive.eu](http://www.listenlive.eu). Not every link is working, so I recommend to test radio URL before adding it to the config file.

## Using piSingleSwitchRadio

If everything is up and running:
- **short switch press** - speech synthesizer reads first radio station name, then radio starts playing (in Raspberry Pi 1 it could be slight delay for buffering),
- **next short switch press** - speech synthesizer reads next radio station name and next radio station starts playing,
- **long switch press** - radio turns off (long press - more than 1 second)
Thats all!
