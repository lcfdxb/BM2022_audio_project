import pyaudio
import wave
import time
import random
import sculptor
from threading import Thread
from datetime import datetime


class AudioPlayer:

    CHUNK_SIZE = 1024
    NUM_TRACKS_TO_PLAY_TOGETHER = 3

    _files_manager = None
    _threads = []
    _audio = None
    _stop_threads = False  # flag which each thread checks on to see if it needs to stop

    def __init__(self, files_manager):
        self._files_manager = files_manager
        print("------- Spawning PyAudio -------")
        self._audio = pyaudio.PyAudio()
        print("------- Done Spawning PyAudio -------")
        self._stop_threads = False

    def start_playing(self):
        files_to_play = []
        for ii in range(self.NUM_TRACKS_TO_PLAY_TOGETHER):
            file_path = self._files_manager.get_random_file_path()
            if file_path is None:
                return
            files_to_play.append(file_path)

        self._stop_threads = False
        print("Playing files: " + str(files_to_play))

        for file_path in files_to_play:
            tid = random.random() * 100000000
            thread = Thread(target=self._play_wave_file, args=(tid, lambda: self._stop_threads, file_path,))
            self._threads.append(thread)
            thread.start()

    def stop_playing(self):
        self._stop_threads = True
        time.sleep(1)  # give them some time to terminate
        self._threads = []

    def is_playing(self):
        for thread in self._threads:
            if thread.is_alive():
                return True
        return False

    # TODO not sure what would be the best way to call this
    def terminate(self):
        self.stop_playing()
        for thread in self._threads:
            thread.join()
        self._audio.terminate()

    # private method
    def _play_wave_file(self, tid, should_stop, file):
        print("Player thread {}: started!".format(tid))
        wave_file = wave.open(file, 'rb')
        reshaped_wave_file = sculptor.reshape_audio(wave_file)
        stream = self._audio.open(
            format=self._audio.get_format_from_width(reshaped_wave_file.getsampwidth()),
            channels=reshaped_wave_file.getnchannels(),
            rate=reshaped_wave_file.getframerate(),
            output=True
        )
        data = reshaped_wave_file.readframes(self.CHUNK_SIZE)
        while len(data) > 0:
            if should_stop():
                print("Player thread {}: stopped by master!".format(tid))
                break
            # this produces a lot of logs
            # print("{} > Player thread {} writing data len({}) to stream.".format(datetime.now().strftime("%Y%m%d_%H%M%S"), tid, len(data)))
            stream.write(data)
            data = reshaped_wave_file.readframes(self.CHUNK_SIZE)
        stream.close()
        print("Player thread {}: exited peacefully!".format(tid))
