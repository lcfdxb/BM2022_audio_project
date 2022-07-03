import speake3
import random


class StateDisplayer:

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
        self._engine = speake3.Speake()
        self._engine.set('voice', 'en-us')
        self._engine.set('speed', '120')
        self._engine.set('pitch', '45')
        self._engine.set('amplitude', '200')  # 0-200

    def display_message(self, message="Hello!"):
        print("I'm saying: " + message)
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
