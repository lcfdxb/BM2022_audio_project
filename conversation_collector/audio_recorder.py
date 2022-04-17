import pyaudio
import wave
import os
import logging
import files_manager
from pydub import AudioSegment
from pydub.silence import detect_nonsilent


# https://makersportal.com/blog/2018/8/23/recording-audio-on-the-raspberry-pi-with-python-and-a-usb-microphone

form_1 = pyaudio.paInt16  # 16-bit resolution
chans = 1  # 1 channel
# TODO for some weird reason, my RPi can only play this rate.
#  Hence need to sample at same rate (IDK)? Some devices don't support 48000 though
samp_rate = 48000
chunk = 4096  # 2^12 samples for buffer


class AudioRecorder:
    _dev_index = 0
    _audio = None

    def __init__(self):
        logging.warning("AudioRecorder: Started Spawning PyAudio")
        self._audio = pyaudio.PyAudio()
        logging.warning("AudioRecorder: Finished Spawning PyAudio")

        # TODO: this needs to be changed when we have >1 sound devices. I.e. we add a speaker with same prefix
        for ii in range(self._audio.get_device_count()):
            device_name = str(self._audio.get_device_info_by_index(ii).get('name'))
            logging.info("AudioRecorder: Looking at " + device_name)
            # TODO: fix this when using an external speaker
            if 'USB PnP' in device_name:
                self._dev_index = ii
                return
        raise Exception("Recorder: no input device found!")

    def record_audio(self, duration_in_seconds=10):
        file_name = files_manager.get_new_file_name_no_ext()
        # tmp path also helps when it blows up during recording.
        # The audio player reads form final_path thus out of blast radius.
        tmp_save_path = files_manager.get_new_tmp_file_path(file_name)
        final_save_path = files_manager.get_new_processed_file_path(file_name)

        stream = self._audio.open(format=form_1, rate=samp_rate, channels=chans,
                                  input_device_index=self._dev_index, input=True,
                                  frames_per_buffer=chunk)

        logging.info("AudioRecorder: started to record for " + str(duration_in_seconds) + " seconds!")
        frames = []
        # loop through stream and append audio chunks to frame array
        for ii in range(0, int((samp_rate / chunk) * duration_in_seconds)):
            data = stream.read(chunk)
            frames.append(data)
        logging.info("AudioRecorder:  finished recording!")
        stream.stop_stream()
        stream.close()

        # save the audio frames as a tmp .wav file
        wavefile = wave.open(tmp_save_path, 'wb')
        wavefile.setnchannels(chans)
        wavefile.setsampwidth(self._audio.get_sample_size(form_1))
        wavefile.setframerate(samp_rate)
        wavefile.writeframes(b''.join(frames))
        wavefile.close()

        # normalize the recording to generate a final file
        raw_recording = AudioSegment.from_file(tmp_save_path)
        normalized_sound = raw_recording.apply_gain(-20.0 - raw_recording.dBFS)
        # TODO: this doesn't really work. Figure out a better way to handle silent recordings
        if len(detect_nonsilent(normalized_sound, silence_thresh=-40, seek_step=10)) == 0:
            return False
        normalized_sound.export(final_save_path, format="mp3")
        os.remove(tmp_save_path)
        return True

    # TODO not sure what would be the best way to call this
    def terminate(self):
        self._audio.terminate()
