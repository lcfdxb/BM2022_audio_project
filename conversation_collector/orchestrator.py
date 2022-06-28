import time
from poet import Poet
from state_controller import StateController
from state_displayer import StateDisplayer
from audio_player import AudioPlayer
from audio_recorder import AudioRecorder


class Orchestrator:
    def __init__(self, oid):
        self.id = oid
        self.stateController = StateController()
        self.stateDisplayer = StateDisplayer()
        self.audioRecorder = AudioRecorder()
        self.audioPlayer = AudioPlayer()
        self.poet = Poet()

    def work(self):
        # print("ORCH#" + str(self.id) + ": orchestrating....")
        time.sleep(1)
        should_record = self.stateController.should_record()
        # print("ORCH#" + str(self.id) + ": should_record?=" + str(should_record))
        if should_record:
            self.audioPlayer.stop_playing()
            time.sleep(1)
            self.stateDisplayer.announce_recording_prepare()
            time.sleep(5)
            self.stateDisplayer.announce_recording_begin()
            self.stateController.ack_recording_began()
            succeeded = self.audioRecorder.record_audio(duration_in_seconds=60)
            self.stateController.ack_recording_began()  # so if won't immediately record again
            self.stateDisplayer.announce_recording_complete(success=succeeded)
        else:
            is_playing = self.audioPlayer.is_playing()
            # print("ORCH#" + str(self.id) + ": is_playing?=" + str(is_playing))
            if not is_playing:
                self.stateDisplayer.display_message(self.poet.recite())
                time.sleep(3)  # this is needed to fix the Jabra traffic issue
                self.audioPlayer.start_playing()
