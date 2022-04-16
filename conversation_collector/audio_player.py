import pyaudio
import time
import random
import sculptor
from threading import Thread
from pydub import AudioSegment


class AudioPlayer:
    CHUNK_SIZE = 1024
    NUM_TRACKS_TO_PLAY_TOGETHER = 3

    _files_manager = None
    _thread = None
    _audio = None
    _stop_thread = False  # flag which the thread checks on to see if it needs to stop

    def __init__(self, files_manager):
        self._files_manager = files_manager
        print("------- Spawning PyAudio -------")
        self._audio = pyaudio.PyAudio()
        print("------- Done Spawning PyAudio -------")
        self._stop_thread = False

    def start_playing(self):
        if self._files_manager.get_number_of_processed_files() < self.NUM_TRACKS_TO_PLAY_TOGETHER:
            return
        # select X different recordings to play
        files_to_play = []
        while len(files_to_play) < self.NUM_TRACKS_TO_PLAY_TOGETHER:
            file_path = self._files_manager.get_random_processed_file_path()
            if file_path not in files_to_play:
                files_to_play.append(file_path)
        self._stop_thread = False
        print("Playing files: " + str(files_to_play))
        tid = random.random() * 100000000
        self._thread = Thread(target=self._play_wave_files, args=(tid, lambda: self._stop_thread, files_to_play,))
        self._thread.start()

    def stop_playing(self):
        self._stop_thread = True
        time.sleep(1)  # give them some time to terminate
        self._thread = None

    def is_playing(self):
        if self._thread and self._thread.is_alive():
            return True
        return False

    # private method
    def _play_wave_files(self, tid, should_stop, files):
        if len(files) < 1:
            raise Exception("Player: please play at least one file!")
        print("Player thread {}: started!".format(tid))

        combined_sound = AudioSegment.from_file(files[0])
        for i in range(1, len(files)):
            sound = AudioSegment.from_file(files[i])
            combined_sound = combined_sound.overlay(sound)
        combined_sound = combined_sound.fade_in(3000).fade_out(3000)
        # although you can use play(combined_sound) but then we lose the ability to stop the thread on demand
        combined_sample = sculptor.reshape_audio(combined_sound)
        stream = self._audio.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=48000,
            output=True
        )

        seg_start = 0
        while seg_start < len(combined_sample):
            if should_stop():
                print("Player thread {}: stopped by master!".format(tid))
                break
            seg_end = seg_start + self.CHUNK_SIZE
            stream.write(combined_sample[seg_start:seg_end])
            seg_start = seg_end
        stream.close()
        print("Player thread {}: exited peacefully!".format(tid))
