# Burning Man 2022 Project

### Start the collector program
`$> python conversation_collector`

### Package Dependency 
- wave
- pyaudio
- tkinter
- RPI.GPIO (pip install RPi.GPIO)
- ESPEAK-NG (explained below)

### TODO
- Audio player
- Audio recorder
- Audio storage (wrap up?)
- need to handle garbage recordings (no voice / button mis trigger)

### On ESPEAK-NG
- Can't get that pptxy thingy work on my RPi4b so I'm compiling its dependency (espeak) locally and running it with a system command
- LMK if you can apt get espeak to work on RPi : (
- How to install on your machine:
```
sudo apt-get install make autoconf automake libtool pkg-config
git clone https://github.com/espeak-ng/espeak-ng.git
cd espeak-ng
./autogen.sh
./configure --prefix=/usr
make
# get your own path replace below ESPEAK_DATA_PATH
ESPEAK_DATA_PATH='/home/pi/Desktop/espeak-ng' LD_LIBRARY_PATH=src:${LD_LIBRARY_PATH} src/espeak-ng "hello world" -p 50 --stdout | aplay
```

## Design
![design_diagram](./design/design.png)
