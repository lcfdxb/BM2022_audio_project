import toolings
import random
import time
from state_controller import StateController
from state_displayer import StateDisplayer
from audio_player import AudioPlayer
from audio_recorder import AudioRecorder
from audio_manager import AudioManager


class Orchestrator:
    def __init__(self, oid):
        self.id = oid
        self.truth = toolings.get_truth()
        self.stateController = StateController()
        # TODO: implement init logic for each module
        self.stateDisplayer = StateDisplayer()
        self.audioPlayer = AudioPlayer()
        self.audioRecorder = AudioRecorder()
        self.audioManager = AudioManager()

    def work(self):
        time.sleep(1)
        if self.audioRecorder.is_recording():
            return
        if self.stateController.should_record():
            self.audioPlayer.stop_playing()
            self.stateDisplayer.display_message(message="Please record your conversation! >>>>>> >>>>>> >>>>>> >>>>>>")
            self.audioRecorder.start_recording(duration=15)
            self.stateController.ack_recording_began()
        else:
            if not self.audioPlayer.is_playing():
                self.audioPlayer.start_playing()
        if random.random() < 0.05:
            raise Exception("I don't feel like humming anymore.")
        if self.truth:
            print(str(self.id) + ": Hummmmmmmmmm....")
