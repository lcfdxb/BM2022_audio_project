import RPi.GPIO as GPIO

# Arcade Buttons Tutorials:
# https://learn.adafruit.com/retro-gaming-with-raspberry-pi/adding-controls-hardware
# https://learn.adafruit.com/press-your-button-for-raspberry-pi/assembly
# https://github.com/tmckay1/best_friend_light/blob/main/lights/BestFriendLight.py
# http://razzpisampler.oreilly.com/ch07.html

class StateController:
    _push_button_pin = 17
    _should_record = False

    def __init__(self):
        GPIO.cleanup()
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._push_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self._push_button_pin, GPIO.FALLING, callback=self._pressed, bouncetime=200)

    def should_record(self):
        return self._should_record

    def ack_recording_began(self):
        self._should_record = False

    # private method
    def _pressed(self, _):
        self._should_record = True
