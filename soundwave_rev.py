#soundwave.py
#By Tashi
#soundwave is a representation of samples

import tonelib
import math
import wave
import struct
import subprocess
import random
import sys
import os
class SoundWave:
    def __init__(self, samples = []):
        """creates an empty soundwave list"""

        self._samples = list(samples)
        #list make own independent copy of the list
        self.wave = samples
        self.duration = 0
        self.maxamp = 0
        
    def __extend__(self, othersample):
        """add soundwave list to the empty list"""

        self.extend(othersample)
        self.duration += len(self.wave)
        new_max = max(self.wave)
        
        if new_max > self.maxamp:
            self.maxamp = new_max
        

    def duration(self):
        """play-length in seconds"""

        return self.duration
        
        
    def maxamp(self):
        """maximum amplitude"""

        return self.maxamp
        
    def clamp(self):
        """chops value to -1 to 1"""

        for i in range(self.duration):
            if self.wave[i] > 1:
                self.wave[i] = 1
            if self.wave[i] < -1:
                self.wave[i] = -1
    
    def normalize(self):
        """divide by maxamp"""

        for i in range(self.duration):
            self.wave[i] = self.wave[i]/self.maxamp
    
    def tofile(self, fname):
        """write wave file"""

        wavefile = open(fname, "w")
        wavefile.write(str(self.wave))
           
    def play(self, samples):
        write_wavefile(samples, "temp.wav")
        winsound.PlaySound("temp.wav",
                           winsound.SND_FILENAME & winsound.SND_ASYNC)
        os.remove("temp.wav")

    def __len__(self):
        """returns number of samples"""
        return len(self.wave)
    
    def __getitem__(self, i):
        """returns ith sample"""
        return self.wave[i]

    def __add__(self, other):
        """components-wise addition"""
        for item in self.wave:
            item += other

    def __mul__(self, factor):
        """multiply each sample by factor"""
        for item in self.wave:
            item *= factor

    def __rmul__(self, factor):
        """takes care of 0.25 * sound"""
        for item in self.wave:
            item = factor * item
        
    
    
