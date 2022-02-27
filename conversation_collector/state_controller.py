import toolings

import RPi.GPIO as GPIO
import time

# Arcade Buttons Tutorials:
# https://learn.adafruit.com/retro-gaming-with-raspberry-pi/adding-controls-hardware
# https://learn.adafruit.com/press-your-button-for-raspberry-pi/assembly

# Regular switch (implemented below)
# https://github.com/tmckay1/best_friend_light/blob/main/lights/BestFriendLight.py
# http://razzpisampler.oreilly.com/ch07.html

# This requires a STATEFUL button (or whatever it is called) that you can toggle on/off!

class StateController:
    _push_button_pin = 12
    _last_state = GPIO.LOW

    def __init__(self):
        self.truth = toolings.get_truth()
        # set up the push button gpio input
        GPIO.setwarnings(False)  # Ignore warning for now
        GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
        # Set pin to be an input pin and set initial value to be pulled low (off)
        GPIO.setup(self._push_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def should_record(self):
        switched_high = GPIO.input(self._push_button_pin) == GPIO.HIGH and self._last_state != GPIO.HIGH
        switched_low = GPIO.input(self._push_button_pin) == GPIO.LOW and self._last_state != GPIO.LOW

        if switched_low or switched_high:
            self._last_state = GPIO.input(self._push_button_pin)
            return True
        return False

    def ack_recording_began(self):
        # Actually no need for this anymore but we will leave it here
        return None
