from bibliopixel.layout.strip import Strip


# https://github.com/tmckay1/best_friend_light/blob/main/led_controller/BiblioPixelLedController.py
# control the ambient leds around the personality
class BiblioPixelLedController(object):
    # bibliopixel animation for the leds
    _led = None

    def __init__(self, driver):
        super(object, self).__init__()
        self._led = Strip(driver)
        self._led.set_brightness(30)
        self._led.push_to_driver()

    def turn_off(self):
        self._led.all_off()
        self._led.push_to_driver()

    def turn_on_color(self, color):
        self._led.fill(color)
        self._led.push_to_driver()
