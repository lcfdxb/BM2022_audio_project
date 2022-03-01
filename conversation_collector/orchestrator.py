import toolings
import random
import time
from state_controller import StateController
from state_displayer import StateDisplayer
from audio_player import AudioPlayer
from audio_recorder import AudioRecorder
from audio_manager import AudioManager
from files_manager import FilesManager


class Orchestrator:
    def __init__(self, oid):
        self.id = oid
        self.truth = toolings.get_truth()
        self.stateController = StateController()
        self.stateDisplayer = StateDisplayer()
        self.filesManager = FilesManager()
        self.audioRecorder = AudioRecorder(files_manager=self.filesManager)
        self.audioPlayer = AudioPlayer(files_manager=self.filesManager)
        self.audioManager = AudioManager()

    def work(self):
        time.sleep(2)
        if self.stateController.should_record():
            self.audioPlayer.stop_playing()
            self.stateDisplayer.display_message(message="Please tell me a story!")
            # TODO: not sure if the speaking is blocking or not,
            #  I assume it is not so we want to start recording once the message is spoken?
            time.sleep(2)
            self.stateController.ack_recording_began()
            self.audioRecorder.start_recording(duration_in_seconds=15)
        else:
            if not self.audioPlayer.is_playing():
                self.audioPlayer.start_playing()

        # TODO: Test for robustness. Get rid of these below in prod
        if random.random() < 0.02:
            raise Exception("I don't feel like humming anymore.")
        if self.truth:
            print(str(self.id) + ": Hummmmmmmmmm....")
