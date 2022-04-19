from datetime import datetime
import random
import os

# WARN: customize these for your Pi
#       make sure to manually create these folders under the directory:
#     > /tmp
#     > /processed
#     > /logs
ROOT_PATH = '/home/milton/Desktop/recordings/'
DEVICE_NAME = 'Jabra'


def get_new_file_name_no_ext():
    return datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + '.' + str(random.random() * 100000000)


def get_new_log_file_path(file_name_no_ext):
    return os.path.join(ROOT_PATH, 'logs/') + file_name_no_ext + ".log"


def get_new_tmp_file_path(file_name_no_ext):
    return os.path.join(ROOT_PATH, 'tmp/') + file_name_no_ext + ".wav"


def get_new_processed_file_path(file_name_no_ext):
    return os.path.join(ROOT_PATH, 'processed/') + file_name_no_ext + ".mp3"


def get_random_processed_file_path():
    processed_folder = os.path.join(ROOT_PATH, 'processed/')
    if len(os.listdir(processed_folder)) == 0:
        return None
    return os.path.join(processed_folder, random.choice(os.listdir(processed_folder)))


def get_number_of_processed_files():
    processed_folder = os.path.join(ROOT_PATH, 'processed/')
    return len(os.listdir(processed_folder))
