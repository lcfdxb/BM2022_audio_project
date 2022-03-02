import pyaudio
import wave
import time
import random
from threading import Thread


class AudioFile:

    CHUNK_SIZE = 1024

    _threads = []
    _audio = None
    _stop_threads = False

    def __init__(self):
        print("------- Spawning PyAudio -------")
        self._audio = pyaudio.PyAudio()
        print("------- Done Spawning PyAudio -------")
        self._stop_threads = False

    def play_wave_file(self, tid, should_stop, file):
        wave_file = wave.open(file, 'rb')
        stream = self._audio.open(
            format = self._audio.get_format_from_width(wave_file.getsampwidth()),
            channels = wave_file.getnchannels(),
            rate = wave_file.getframerate(),
            output = True
        )
        data = wave_file.readframes(self.CHUNK_SIZE)
        while data != '':
            if should_stop():
                print("Player thread {}: stopped!".format(tid))
                break
            stream.write(data)
            data = wave_file.readframes(self.CHUNK_SIZE)
        stream.close()

    def play(self, file):
        self._stop_threads = False
        tid = random.random()
        thread = Thread(target=self.play_wave_file, args=(tid, lambda: self._stop_threads, file,))
        self._threads.append(thread)
        thread.start()
        print("Player thread {}: started!".format(tid))

    def stop(self):
        self._stop_threads = True

    def terminate(self):
        self.stop()
        for thread in self._threads:
            thread.join()
        self._audio.terminate()


fp = '/Users/milton/Downloads/wake up 20220213.wav'
a = AudioFile()

a.play(fp)
for i in [1,2,3,4,5]:
    time.sleep(1)
    print(i)

a.play(fp)
for i in [1,2,3,4,5]:
    time.sleep(1)
    print(i)

a.play(fp)
for i in [1,2,3,4,5]:
    time.sleep(1)
    print(i)

print("trying to stop!")
a.stop()
for i in [1,2,3,4,5]:
    time.sleep(1)
    print(i)

print("trying to terminate!")
a.terminate()
