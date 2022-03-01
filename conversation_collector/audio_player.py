

class AudioPlayer:
    _files_manager = None

    def __init__(self, files_manager):
        self._files_manager = files_manager

    def start_playing(self):
        # TODO
        # WARN: files manager could return None
        print("Player: pretending to play -> " + str(self._files_manager.get_random_file_path()))
        return None

    def stop_playing(self):
        # TODO
        print("Player: stopped playing!")
        return None

    def is_playing(self):
        # TODO
        print("Player: returned false to playing status!!")
        return False
