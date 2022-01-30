from ast import Global
import pyaudio, struct
import tkinter as Tk   	
import time
import wave

WIDTH       = 2         # Number of bytes per sample
CHANNELS    = 1         # mono
RATE        = 16000     # Sampling rate (frames/second)
DURATION    = 5        # duration of processing (seconds)
FPB         = 512       # frames per buffer
block_len   = 256

# N : Number of samples to process
N = (DURATION * RATE)

read_pointer = 0
write_pointer = 0

recording_flag = 1

root = Tk.Tk()

buffer = N * [0]

p = pyaudio.PyAudio()
stream = p.open(format      = p.get_format_from_width(WIDTH),
                channels    = CHANNELS,
                rate        = RATE,
                input       = True,
                output      = True,
                frames_per_buffer = FPB)

def my_recording():
    global recording_flag
    print("recording...")
    recording_flag = 1
    pass

def my_playing():
    global recording_flag
    print("Playing...")
    recording_flag = 0
    pass

def key_input(event):
    if event.char == 'r':
        my_recording()
    elif event.char == 'p':
        my_playing()

root.bind("<Key>", key_input)

while 1:
    if recording_flag==1:
        input_bytes = stream.read(block_len, exception_on_overflow = False)
        input_tuple = struct.unpack('h' * block_len, input_bytes)
        for i in range(0, block_len):
            buffer[write_pointer] = int(input_tuple[i])
            write_pointer += 1
            if write_pointer >= N:
                write_pointer = 0

    else: #recording_flag==0
        output_bytes = struct.pack('h'*block_len, *buffer[read_pointer:read_pointer+block_len])
        stream.write(output_bytes)

        read_pointer += block_len
        if read_pointer >= N - block_len:
            read_pointer = 0
        
    # check keyboard input
    root.update()

stream.stop_stream()
stream.close()
p.terminate()