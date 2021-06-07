#soundwave.py
#By Tashi
#soundwave is a representation of samples
class SoundWave:
    def __init__(self, samples = []):
        """creates an empty soundwave list"""

        self._samples = list(samples)
        self._maxamp = self.maxamp()
    
    def __len__(self):
        return len(self._samples)
    
    def __getitem__(self, i):
        return self._samples[i]

    def extend(self, samples):
        for i in samples:
            self._samples.append(i)
        return self._samples

    def duration(self):
        return 1/44100 * len(self._samples)

    def maxamp(self):
        high = 0
        for i in self._samples:
            if abs(i) > high:
                high = abs(i)
        return high
        

    def clamp(self):
        i = 0
        for sample in self._samples:
            if sample > 1:
                self._samples[i] = 1
            elif sample < -1:
                self._samples[i] = -1
            else:
                self._samples[i] = sample
            i += 1
        return self._samples
            
    def normalize(self):

        for i in range( len(self._samples)):
            self._samples[i] /= self._maxamp
        return self._samples

    def __add__(self, other):
        for i in range(len(self._samples)):
            if i > len(other)-1:
                break
            self._samples[i] += other[i]
        return self._samples

    def __mul__(self, factor):
        for i in range(len(self._samples)):
            self._samples[i] *= factor
        return self._samples
        
    def __rmul__(self, factor):
        for i in range(len(self._samples)):
            self._samples[i] = factor * self._samples[i]
        return self._samples

    def play(self):
       return play_sound(generate_tone(freq=freq))
        
        

    

    
            
            
        
