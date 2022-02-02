import toolings


class AudioManager:
    def __init__(self):
        self.truth = toolings.get_truth()

    def save(self, audio_file, file_name):
        # TODO
        return None

    def get(self, file_name):
        # TODO
        return "Decide what file format we use"

    def list(self):
        # TODO
        return ["1.wav", "2.mp3"]
