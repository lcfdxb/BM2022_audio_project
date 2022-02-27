import toolings


class AudioPlayer:
    def __init__(self):
        self.truth = toolings.get_truth()

    def start_playing(self):
        # TODO
        print("Player: started to play!")
        return None

    def stop_playing(self):
        # TODO
        print("Player: stopped playing!")
        return None

    def is_playing(self):
        # TODO
        print("Player: returned false to playing status!!")
        return False
