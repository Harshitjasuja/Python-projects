import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100 #sample rate
seconds = int(input('enter the time duration (in Seconds): '))
print('Recording...')

#Record Audio
record_voice =sd.rec(int(seconds*fs), samplerate= fs, channels= 1, dtype='int16')
sd.wait() # Wait until recording is finished

#save the recording
write("out.wav", fs, record_voice)

print("voice has been recorded")
print("checkout out.wav file")