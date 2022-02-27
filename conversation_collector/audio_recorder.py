import toolings


class AudioRecorder:
    def __init__(self):
        self.truth = toolings.get_truth()

    def start_recording(self, duration=10):
        # TODO
        print("Recorder: started to record for " + str(duration) + " seconds!")
        return None

    def is_recording(self):
        # TODO
        print("Recorder: returning false for is_recording!")
        return False
