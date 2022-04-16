# Burning Man 2022 Project

### Start the collector program
`$> python conversation_collector`

## Priorities
[Prio] until 5/31

### Art
- [MED] Sound sculpture - design & implement different play styles
  - By implementing sculptor.reshape_audio() logic
- [LOW] Sound sculpture - switch to different styles per hour in day / number of files / etc.
  - By implementing sculptor.reshape_audio() logic
### System
- [HIGH] Audio player - need to handle garbage recordings (no voice / button mis trigger)
- [HIGH] Audio recorder - in case of disaster during write
  - investigate if we need to make it more robust
  - maybe write to staging folder then move completed file to the audio folder
- [MED] System - make all "print" statement also log to a file
- [LOW] System - test the heck out of this POC and make it more robust
### UX
- [MED] Audio Recorder - talks more
  - e.g. better UI when sampling, and maybe randomly select from several prompts
### Hardware
- [HIGH] Design & implement power solution - solar / batteries
  - https://hive.burningman.org/posts/14167796
  - https://forums.raspberrypi.com/viewtopic.php?t=96544
  - https://howchoo.com/g/mmfkn2rhoth/raspberry-pi-solar-power
- [HIGH] Make a POC shell
  - so we can demo this around
- [MED] Playa installation solution: Pole
  - what kind of pole to use?
  - needs to be resistant to STRONG wind
- [LOW] Make a robust and aesthetically pleasing shell
  - Directly out of wood? or 3D printed w/ heat-resistant materials?
- [LOW] Playa installation solution: Harsh environment
  - the whole thing needs to be resistant to STRONG wind / heat / rain
  - https://forums.raspberrypi.com/viewtopic.php?t=54812
  - https://forums.raspberrypi.com/viewtopic.php?f=63&t=44684

## Notes

### Package Dependency 
- Stable OS: Raspberry Pi OS (32-bit) `Release 2022-04-04; installed with Raspberry Pi Imager v1.7.2`
- wave `pip3 install wave`
- RPI.GPIO `pip3 install RPi.GPIO`
- numpy `pip3 install numpy`
- pydub `pip3 install pydub`
- pyaudio `pip3 install pyaudio`
- ESPEAK-NG `sudo apt-get install espeak && pip3 install speake3`

### Hard-wiring / Setup
- Make sure to update the hard-coded path in files_manager.py `_folder_path`

## Design
*Mostly Outdated*
![design_diagram](./design/design.png)
