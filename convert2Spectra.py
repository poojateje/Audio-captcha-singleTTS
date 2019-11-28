#import libraries
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile,join
import os
#for loading and visualizing audio files
import librosa
import librosa.display
import librosa
import librosa.display
import numpy as np
#to play audio
#import IPython.display as ipd
path="audio_captchas"
dest = "audio_spectra"
#get audio files from given folder
files = [f for f in listdir(path) if isfile(join(path,f))]
#gray= file.open(self.directory_name + "/" + random_image_file)
#audio_clips = os.listdir(audio_fpath)
for audio in files:
    #loading file using librosa
    x, sr = librosa.load(os.path.join(path, audio))
    #set dimentions of spectogram figure
    plt.figure(figsize=(1.28, .64), dpi=100)
    plt.axis('off')
    plt.axes([0., 0., 1., 1., ], frameon=False, xticks=[], yticks=[])
    #generate spectogram 
    S = librosa.feature.melspectrogram(y=x, sr=sr)
    #show spectogram
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    #save spectogram with same name as that of audio file
    plt.savefig(os.path.join(dest, os.path.splitext(audio)[0]+'.png'), bbox_inches=None, pad_inches=0)
    plt.close()