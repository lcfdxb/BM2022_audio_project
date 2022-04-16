import numpy

def reshape_audio(audio_segment):
    # TODO implement here how the audio will be adjusted (input is pydub AudioSegment, output byte array for playing)
    # TODO stretch: include logic that dynamically changes the playing style per external parameters

    # https://github.com/jiaaro/pydub/blob/master/API.markdown#audiosegmentget_array_of_samples
    audio_segment = audio_segment.set_frame_rate(48000)
    audio_segment = audio_segment.split_to_mono()
    samples = [s.get_array_of_samples() for s in audio_segment]
    fp_arr = numpy.array(samples).T.astype(numpy.float32)
    fp_arr /= numpy.iinfo(samples[0].typecode).max
    return fp_arr.astype(numpy.float32).tobytes()
