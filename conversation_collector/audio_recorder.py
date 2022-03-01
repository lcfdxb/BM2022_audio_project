import pyaudio
import wave


# https://makersportal.com/blog/2018/8/23/recording-audio-on-the-raspberry-pi-with-python-and-a-usb-microphone

form_1 = pyaudio.paInt16  # 16-bit resolution
chans = 1  # 1 channel
samp_rate = 44100  # 44.1kHz sampling rate
chunk = 4096  # 2^12 samples for buffer


class AudioRecorder:
    _dev_index = 0
    _files_manager = None
    _audio = None

    def __init__(self, files_manager):
        self._files_manager = files_manager

        print("------- Spawning PyAudio -------")
        self._audio = pyaudio.PyAudio()
        print("------- Done Spawning PyAudio -------")

        # TODO: this needs to be changed when we have >1 sound devices. I.e. we add a speaker with same prefix
        for ii in range(self._audio.get_device_count()):
            if 'USB PnP Sound Device' in self._audio.get_device_info_by_index(ii).get('name'):
                self._dev_index = ii
                break
            raise Exception("Recorder: no input device found!")

    # This should be blocking, so no is_recording is needed
    def start_recording(self, duration_in_seconds=10):
        save_path = self._files_manager.get_new_file_path()

        # create pyaudio stream
        stream = self._audio.open(format=form_1, rate=samp_rate, channels=chans, \
                                  input_device_index=self._dev_index, input=True, \
                                  frames_per_buffer=chunk)

        print("Recorder: started to record for " + str(duration_in_seconds) + " seconds!")
        frames = []

        # loop through stream and append audio chunks to frame array
        for ii in range(0, int((samp_rate / chunk) * duration_in_seconds)):
            data = stream.read(chunk)
            frames.append(data)

        print("Recorder: finished recording!")

        # stop the stream, close it
        stream.stop_stream()
        stream.close()
        # audio.terminate() # terminate the pyaudio instantiation. If so, instantiate it in this method.

        # save the audio frames as .wav file
        wavefile = wave.open(save_path, 'wb')
        wavefile.setnchannels(chans)
        wavefile.setsampwidth(self._audio.get_sample_size(form_1))
        wavefile.setframerate(samp_rate)
        wavefile.writeframes(b''.join(frames))
        wavefile.close()
        return None
