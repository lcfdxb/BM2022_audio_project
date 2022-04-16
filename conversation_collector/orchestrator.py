import random
import time
from state_controller import StateController
from state_displayer import StateDisplayer
from audio_player import AudioPlayer
from audio_recorder import AudioRecorder
from files_manager import FilesManager


class Orchestrator:
    def __init__(self, oid):
        self.id = oid
        self.stateController = StateController()
        self.stateDisplayer = StateDisplayer()
        self.filesManager = FilesManager()
        self.audioRecorder = AudioRecorder(files_manager=self.filesManager)
        self.audioPlayer = AudioPlayer(files_manager=self.filesManager)

    def work(self):
        print("ORCH#" + str(self.id) + ": orchestrating....")
        time.sleep(2)
        should_record = self.stateController.should_record()
        print("ORCH#" + str(self.id) + ": should_record?=" + str(should_record))
        if should_record:
            self.audioPlayer.stop_playing()
            time.sleep(2)
            # TODO: Task: Audio Recorder - talks more
            self.stateDisplayer.display_message(message="Hello. I will be listening for 15 seconds soon. Please tell me your story!")
            time.sleep(5)
            self.stateDisplayer.display_message(message="Hello. I am NOW listening. Please tell me your story!")
            self.stateController.ack_recording_began()
            self.audioRecorder.start_recording(duration_in_seconds=15)
            self.stateDisplayer.display_message(message="Thank you. Your recording has joined the stream of voices.")
        else:
            is_playing = self.audioPlayer.is_playing()
            print("ORCH#" + str(self.id) + ": is_playing?=" + str(is_playing))
            if not is_playing:
                self.audioPlayer.start_playing()

        # TODO: Test for robustness. Get rid of these below in prod
        if random.random() < 0.01:
            raise Exception("I don't feel like humming anymore.")
