# Burning Man 2022 Project

### Start the collector program
`$> python conversation_collector`

## Priorities
### Art
- Sound sculpture - design & implement different play styles
  - By implementing sculptor.reshape_audio() logic
- Sound sculpture - switch to different styles per hour in day / number of files / etc.
  - By implementing sculptor.reshape_audio() logic
### Fix
- Audio player - 3 threads works pretty bad on RPi 4 HDMI.
  - Experiment with merging audio files (1 thread only) or try analogue output?
- Audio player - don't pick the same file in start_playing()
- Audio player - need to handle garbage recordings (no voice / button mis trigger)
- System - make all "print" statement also log to a file
- System - test the heck out of this POC and make it more robust

## Notes

### Package Dependency 
- tkinter (demo only)
- wave
- RPI.GPIO (pip install RPi.GPIO)
- pyaudio (explained below)
- ESPEAK-NG (explained below)

## Hardcoding / Setup

### Make sure
- the hard-coded path in files_manager.py is present (_folder_path)

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

### Installing pyAudio on RPi 4b
```
sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
pip install pyaudio
```

## Design
Outdated*
![design_diagram](./design/design.png)
