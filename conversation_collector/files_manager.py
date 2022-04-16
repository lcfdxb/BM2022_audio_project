from datetime import datetime
import random
import os


class FilesManager:
    # WARN: customize this for your Pi
    #       make sure to manually create these 2 folders under the directory:
    #     > /tmp
    #     > /processed
    _folder_path = '/home/milton/Desktop/recordings/'

    def __init__(self):
        return

    def get_new_file_name_no_ext(self):
        return datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + '.' + str(random.random() * 100000000)

    def get_new_tmp_file_path(self, file_name_no_ext):
        return os.path.join(self._folder_path, 'tmp/') + file_name_no_ext + ".wav"

    def get_new_processed_file_path(self, file_name_no_ext):
        return os.path.join(self._folder_path, 'processed/') + file_name_no_ext + ".mp3"

    def get_random_processed_file_path(self):
        processed_folder = os.path.join(self._folder_path, 'processed/')
        if len(os.listdir(processed_folder)) == 0:
            return None
        return os.path.join(processed_folder, random.choice(os.listdir(processed_folder)))

    def get_number_of_processed_files(self):
        processed_folder = os.path.join(self._folder_path, 'processed/')
        return len(os.listdir(processed_folder))
