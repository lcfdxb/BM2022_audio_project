import numpy
import pydub
import random
import pyrubberband


# adjust the audio for playing (input is pydub AudioSegment, output byte array to write to the stream)
def reshape_audio(audio_segment):
    # let's do this for every segment because fading makes everything sound better
    audio_segment = audio_segment.fade_in(3000).fade_out(3000)

    # randomly mess with the audio
    if _lets_do_this(0.3):
        speed_adjust = float(random.randrange(85, 115)) / 100  # 0.85 - 1.15
        if speed_adjust == 1.0:
            speed_adjust = 0.99  # or this will be fun
        audio_segment = _change_tempo_and_preserve_pitch(audio_segment, tempo=1.0, new_tempo=speed_adjust)
    elif _lets_do_this(0.03):
        audio_segment = _speed_change_also_changes_pitch(audio_segment, speed=0.6)
    elif _lets_do_this(0.03):
        audio_segment = _speed_change_also_changes_pitch(audio_segment, speed=1.4)

    # https://github.com/jiaaro/pydub/blob/master/API.markdown#audiosegmentget_array_of_samples
    audio_segment = audio_segment.set_frame_rate(48000)
    audio_segment = audio_segment.split_to_mono()
    samples = [s.get_array_of_samples() for s in audio_segment]

    # we could do something artsy here, give it a try if you are good at math!
    fp_arr = numpy.array(samples).T.astype(numpy.float32)
    fp_arr /= numpy.iinfo(samples[0].typecode).max
    return fp_arr.astype(numpy.float32).tobytes()


# # # Below are utils for sculptor use only # # #

def _lets_do_this(probability=0.5):
    return random.random() <= probability


# from https://stackoverflow.com/a/51434954
def _speed_change_also_changes_pitch(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)


# from https://stackoverflow.com/a/59269959
def _change_tempo_and_preserve_pitch(audiosegment, tempo=1.0, new_tempo=1.0):
    y = numpy.array(audiosegment.get_array_of_samples())
    if audiosegment.channels == 2:
        y = y.reshape((-1, 2))
    sample_rate = audiosegment.frame_rate
    tempo_ratio = new_tempo / tempo
    y_fast = pyrubberband.time_stretch(y, sample_rate, tempo_ratio)
    channels = 2 if (y_fast.ndim == 2 and y_fast.shape[1] == 2) else 1
    y = numpy.int16(y_fast * 2 ** 15)
    new_seg = pydub.AudioSegment(y.tobytes(), frame_rate=sample_rate, sample_width=2, channels=channels)
    return new_seg

