import speake3
import random


class StateDisplayer:

    LINES_PREPARE = [
        "Hello. I will be listening to your voice in a few seconds!",
        "Hello. I would like to hear your story! I will be listening in a few seconds!",
    ]

    LINES_BEGIN = [
        "Hello. I am now listening for one minute. Please tell me your story!",
        "Hello. I am now listening for one minute. The time is all yours!",
    ]

    LINES_COMPLETE_SUCCESS = [
        "Thank you. Your story has been written to my memory.",
        "Thank you. Your voice is heard.",
    ]

    LINES_COMPLETE_FAIL = [
        "Thank you. But I have trouble hearing you. Press the button to try again.",
        "Thank you. But the recording is too silent. Press the button to try again.",
    ]

    def __init__(self):
        self._engine = speake3.Speake()
        self._engine.set('voice', 'en-us')
        self._engine.set('speed', '150')
        self._engine.set('pitch', '50')

    def display_message(self, message="Hello!"):
        print("Saying: " + message)
        self._engine.say(message)
        self._engine.talkback()

    def announce_recording_prepare(self):
        self.display_message(message=random.choice(self.LINES_PREPARE))

    def announce_recording_begin(self):
        self.display_message(message=random.choice(self.LINES_BEGIN))

    def announce_recording_complete(self, success=True):
        if success:
            self.display_message(message=random.choice(self.LINES_COMPLETE_SUCCESS))
        else:
            self.display_message(message=random.choice(self.LINES_COMPLETE_FAIL))
