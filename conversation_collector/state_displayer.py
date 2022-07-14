from espeakng import ESpeakNG
import random
from bibliopixel.drivers.PiWS281X import PiWS281X
from led_controller import BiblioPixelLedController

COLOR_FUCHSIA = (255, 0, 255)
COLOR_TEAL = (0, 255, 255)
COLOR_YELLOW = (255, 255, 0)


class StateDisplayer:
    # led_controller to light up the leds
    _led_controller = None

    LINES_PREPARE = [
        "Hello. I am the collector of stories. I would like to collect a story from you. I will start listening for one minute if you want to share. Please think about it for a few seconds.",
        "Hello. I am the collector of questions. I would like to collect a question from you. I will start listening for one minute if you have something to ask. Please think about it for a few seconds.",
        "Hello. I am the collector of songs. I would like to collect a song from you. I will start listening for one minute if you want to sing a song. Please prepare for a few seconds.",
        "Hello. I am the collector of voices. I would like to collect some sounds from you. I will start listening for one minute. Please prepare for a few seconds then make some sounds.",
    ]

    LINES_BEGIN = [
        "Ok, I am listening now!"
    ]

    LINES_COMPLETE_SUCCESS = [
        "Thank you. Your voice is heard. Press the button again to share more.",
    ]

    LINES_COMPLETE_FAIL = [
        "Thank you. But I have trouble hearing you. Press the button to try again.",
        "Thank you. But the recording is too silent. Press the button to try again.",
    ]

    def __init__(self):
        self._engine = ESpeakNG(voice='en-us')
        self._engine.pitch = 32
        self._engine.speed = 125
        self._led_controller = BiblioPixelLedController(driver=PiWS281X(1, gpio=13))  # numLeds == 1

    def display_message(self, message="Hello!"):
        print("I'm saying: " + message)
        self._engine.say(message, sync=True)

    def announce_recording_prepare(self):
        self.display_message(message=random.choice(self.LINES_PREPARE))

    def announce_recording_begin(self):
        self.display_message(message=random.choice(self.LINES_BEGIN))

    def announce_recording_complete(self, success=True):
        if success:
            self.display_message(message=random.choice(self.LINES_COMPLETE_SUCCESS))
        else:
            self.display_message(message=random.choice(self.LINES_COMPLETE_FAIL))

    def display_fuchsia(self):
        self._led_controller.turn_on_color(COLOR_FUCHSIA)

    def display_teal(self):
        self._led_controller.turn_on_color(COLOR_TEAL)

    def display_yellow(self):
        self._led_controller.turn_on_color(COLOR_YELLOW)
