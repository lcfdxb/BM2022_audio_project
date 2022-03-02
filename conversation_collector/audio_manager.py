import wave
from datetime import datetime
import os

folder_path = "./wavefiles"

# wave file parameter (should be the same for all file under folder_path)
fs = 44100
sample_width = 2 # 2 bytes per sample
channel_num = 1 # single channel

class my_wavefile:
    """
    Wavefile strcture
     - path: string, file path
     - status: file status
      0: closed
      1: read
      2: write 
    """
    def __init__(self, path, status):
        self.path = path
        self.status = status
        self.name = os.path.basename(path)

wf_closed = 0
wf_read   = 1
wf_write  = 2

class AudioManager:
    """
    AudioManager manage all the audio files status:
     - offer index to all available files
     - track what file is open for read or write (can't be both)
     - offer wave file handle by index
     - create new wave file - name by timestamp

    Drawback of current implementation:
     - don't support delet (by the structure)
     - don't track who is having the handle (can add this feature in future)
    """

    def __init__(self):
        self.file_list = []
        self.wf_r_handle_dict = {}
        self.wf_w_handle_dict = {}
        
        # search local wav file, add to file_list (mapping filename <-> index)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        for root, ds, fs in os.walk(folder_path):
            for f in fs:
                self.file_list.append(my_wavefile(os.path.join(root,f), wf_closed))

    def new(self):
        """ create a new wavefile to write
        input : none
        return: index
        """
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
        
    def close(self, index):
        """ Close a opened wavefile (also for saving files)
        input : index
        return: 0:done -1:file is closed
        """
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

    def read(self, index):
        """ Open a wave file for reading
        input : index
        return: index:(success) -1(failed)
        """
        wf = wave.open(self.file_list[index].path)
        ## TODO: add execption handling code
        self.file_list[index].status = wf_read
        self.wf_r_handle_dict[index] = wf
        return index

    def len(self):
        """ Get number of wavefiles (also index range)
        """
        return len(self.file_list)

    def get_read_handle(self, index):
        """ get wavefile read handle
        input : index
        return: read handle(success) -1(failed)
        """
        if self.file_list[index].status == wf_read:
            return self.wf_r_handle_dict[index]
        else:
            return -1 

    def get_write_handle(self, index):
        """ get wavefile write handle
        input : index
        return: write handle(success) -1(failed)
        """
        if self.file_list[index].status == wf_write:
            return self.wf_w_handle_dict[index]
        else:
            return -1 

    def print_list(self):
        """ print wavefile lists
        """
        for my_file in self.file_list:
            print(my_file.name)
        return
