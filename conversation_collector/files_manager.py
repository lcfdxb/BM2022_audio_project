from datetime import datetime
import random
import os


class FilesManager:
    _folder_path = '/home/milton/Desktop/recordings/'

    def __init__(self):
        return

    def get_new_file_path(self):
        now_time_rand = datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + '.' + str(random.random() * 100000000)
        return os.path.join(self._folder_path, "%s.wav" % now_time_rand)

    def get_random_file_path(self):
        if len(os.listdir(self._folder_path)) == 0:
            return None
        return os.path.join(self._folder_path, random.choice(os.listdir(self._folder_path)))

    def get_number_of_files(self):
        return len(os.listdir(self._folder_path))
