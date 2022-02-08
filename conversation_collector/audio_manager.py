import toolings
import wave
from datetime import datetime
import os

folder_path = "./wavefiles"

# wave file parameter (should be the same for all file under folder_path)
fs = 44100
sample_width = 2 # 2 bytes per sample
channel_num = 1 # single channel

# Wavefile strcture
#  - path: string, file path
#  - status: file status
#       0: closed
#       1: read
#       2: write 
class my_wavefile:
    def __init__(self, path, status):
        self.path = path
        self.status = status
        self.name = os.path.basename(path)

wf_closed = 0
wf_read   = 1
wf_write  = 2

# AudioManager manage all the audio files status:
#  - offer index to all available files
#  - track what file is open for read or write (can't be both)
#  - offer wave file handle by index
#  - create new wave file，name by timestamp
class AudioManager:

    def __init__(self):
        self.truth = toolings.get_truth()
        self.file_list = []
        self.wf_r_handle_dict = {}
        self.wf_w_handle_dict = {}
        
        # search local wav file, add to file_list (mapping filename <-> index)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        for root, ds, fs in os.walk(folder_path):
            for f in fs:
                self.file_list.append(my_wavefile(os.path.join(root,f), wf_closed))

    """ create a new wavefile to write
        input : none
        return: index
    """
    def new(self):
        now_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        file_path = os.path.join(folder_path, "%s.wav"%now_time)
        wf = wave.open(file_path,'w')
        wf.setnchannels(channel_num)
        wf.setframerate(fs)
        wf.setsampwidth(sample_width)
        # add file to file_list
        index = len(self.file_list)
        self.file_list.append(my_wavefile(file_path, wf_write))
        # add index and handle to wf_w_handles_dict
        self.wf_w_handle_dict[index] = wf
        return index
        
    """ Close a opened wavefile (also for saving files)
        input : index
        return: 0:done -1:file is closed
    """
    def close(self, index):
        # check if in write dict
        if self.file_list[index].status==wf_write:
            wf = self.wf_w_handle_dict.pop(index)
            self.file_list[index].status = wf_closed
            wf.close()
        elif self.file_list[index].status==wf_read:
            wf = self.wf_r_handle_dict.pop(index)
            self.file_list[index].status = wf_closed
            wf.close()
        else:
            return -1
        return 0

    """ Open a wave file for reading
        input : index
        return: index:success -1:failed
    """
    def read(self, index):
        # TODO
        return "Decide what file format we use"

    """ Get wavefile number (also index range)
    """
    def len(self):
        return len(self.file_list)

    """ Print all wavefile lists
    """
    def list(self):
        # TODO
        return ["1.wav", "2.mp3"]
