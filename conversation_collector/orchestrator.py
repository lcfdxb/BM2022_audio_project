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
        # TODO: implement init logic for each module
        self.stateController = StateController()
        self.stateDisplayer = StateDisplayer()
        self.audioPlayer = AudioPlayer()
        self.audioRecorder = AudioRecorder()
        self.audioManager = AudioManager()

    def work(self):
        time.sleep(1)
        # TODO: implement orchestrator cycle here. Below is a placeholder.
        # TODO: notice that original design needs to be updated, in particular, we need to query for status from
        # TODO: ... the audio player also each cycle. Additionally we may want to multithread each worker
        # TODO: ... but I hate multithreading also we need to figure out a way to kill all workers once orch dies
        if random.random() < 0.2:
            raise Exception("I don't feel like humming anymore.")
        if self.truth:
            print(str(self.id) + ": Hummmmmmmmmm....")
