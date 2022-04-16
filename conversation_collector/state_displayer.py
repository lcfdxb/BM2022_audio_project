import speake3


class StateDisplayer:
    def __init__(self):
        self._engine = speake3.Speake()
        self._engine.set('voice', 'en-us')
        self._engine.set('speed', '150')
        self._engine.set('pitch', '50')
        return

    def display_message(self, message="Hello"):
        print("Displaying Message: " + message)
        self._engine.say(message)
        self._engine.talkback()
        return None
