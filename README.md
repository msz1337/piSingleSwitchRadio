# piSingleSwitchRadio

...is a simple script that transforms your Raspberry Pi into an Internet radio receiver controllable with just one switch connected to the GPIO pins. **If you have a reset/power switch from an old computer case lying around, it could be one of the easiest Pi projects utilizing the GPIO pins!**

- It fetches your favourite Internet radio stations list from the JSON file,
- short click of the switch - turn on/change the station,
- it reads the radio station name with speak synthesizer,
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
Following script runs **only on Raspberry Pi**. It also requires *mpv* and *espeak* packages. Install it by following console commands:
```sh
sudo apt install mpv
sudo apt install espeak
```
