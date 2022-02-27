import toolings
import os


class StateDisplayer:
    def __init__(self):
        self.truth = toolings.get_truth()

    def display_message(self, message="Hello"):
        print("Displaying Message: " + message)
        # Note that this is unique to my environment only - feel free to refactor this to make it more sane
        command_pre = "ESPEAK_DATA_PATH='/home/pi/Desktop/espeak-ng' LD_LIBRARY_PATH=/home/pi/Desktop/espeak-ng/src:${LD_LIBRARY_PATH} /home/pi/Desktop/espeak-ng/src/espeak-ng '"
        command_post = "' -v en-gb -p 35 -s 160 --stdout | aplay"  # Feel free to play around with pitch speed etc.
        os.system(command_pre + message + command_post)
        return None
