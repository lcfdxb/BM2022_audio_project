# Burning Man 2022 Project

### Start the collector program
`$> python conversation_collector`

## Priorities
### Art
- Sound sculpture - design & implement different play styles
  - By implementing sculptor.reshape_audio() logic
- Sound sculpture - switch to different styles per hour in day / number of files / etc.
  - By implementing sculptor.reshape_audio() logic
### System
- Audio player - need to handle garbage recordings (no voice / button mis trigger)
- Audio recorder - in case of disaster during write
  - investigate if we need to make it more robust
  - maybe write to staging folder then move completed file to the audio folder
- System - make all "print" statement also log to a file
- System - test the heck out of this POC and make it more robust
### UX
- Audio Recorder - talks more
  - e.g. better UI when sampling, and maybe randomly select from several prompts
### Hardware
- Power solution - solar? Swap batteries?
  - Solar Ref: https://hive.burningman.org/posts/14167796
- Make a robust and aestheticlly pleasing shell
  - Directly out of wood?
  - 3D printing with heat-resistent materials then put clay on top?
  - etc.
  - I'm thinking that we should use a 2-tier body where the lower one is reserved for mounting the button only
- Playa installation solution
  - what kind of pole to use
  - the whole thing needs to be resistent to STRONG wind and heat / cold / RAIN

## Notes

### Package Dependency 
- Stable OS: Raspberry Pi OS (32-bit), Release 2022-04-04; installed with Raspberry Pi Imager v1.7.2
- tkinter (demo only)
- wave (pip3 install wave)
- RPI.GPIO (pip3 install RPi.GPIO)
- numpy (pip3 install numpy)
- pydub (pip3 install pydub)
- pyaudio (pip3 install pyaudio)
- ESPEAK-NG (sudo apt-get install espeak && pip3 install speake3)

### Hard-wiring / Setup
- Make sure that the hard-coded path in files_manager.py is present (_folder_path)

## Design
*Mostly Outdated*
![design_diagram](./design/design.png)
