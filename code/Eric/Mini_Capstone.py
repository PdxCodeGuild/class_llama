"""

Web App Name:    u/R3c0rD  

FREE Online Recording Web App for Artistic Endeavors (USB Microphone is recommended)

pip install metronomiconic (play along with a beat/tempo while writing a song)

pip installed pyaudio, wave, playsound, and soundfile

"""

# pyaudio.PyAudio.open() (To record or play audio)
# pyaudio.Stream.write() (Play audio by writing audio data to the stream)
# pyaudio.Stream.read() (Read audio data from the stream)
# pyaudio.Stream.stop_stream() (Pause/play recording)
# pyaudio.Stream.close() (To terminate the stream)
# pyaudio.Pyaudio.terminate() (End the session)


# record audio in .wav or .mp3
import pyaudio

# .wav format
import wave

# plays the .mp3 or .wav file after recording
from playsound import playsound

# converting .wav files to FLAC or Lossless (much larger file but higher quality)
import soundfile as sf

# # Extract audio data and sampling rate from file 
# data, fs = sf.read('myfile.wav') 
# # Save as FLAC file at correct sampling rate
# sf.write('myfile.flac', data, fs)  

"""
*****RECORDING PARAMETERS******
"""

# the file name and output either .wav or .mp3
filename = "demotrack1.wav"

# set the chunk size of 1024 samples
chunk = 1024

# sample format
FORMAT = pyaudio.paInt16

# mono, change to 2 if you want stereo
channels = 1

# 44100 samples per second
sample_rate = 44100

# How many seconds to record (180 sec = 3 minutes)
record_seconds = 45

# initialize PyAudio object
p = pyaudio.PyAudio()

# open stream object as input & output
stream = p.open(format=FORMAT,
                channels=channels,
                rate=sample_rate,
                input=True,
                output=True,
                frames_per_buffer=chunk)

frames = []

print("Recording...")

for i in range(int(44100 / chunk * record_seconds)):
    data = stream.read(chunk)
    # if you want to hear your voice while recording
    # stream.write(data)
    frames.append(data)

print("Finished Recording")

# stop and close stream
stream.stop_stream()
stream.close()

# terminate pyaudio object
p.terminate()

# save audio file
# open the file in 'write bytes' mode
wf = wave.open(filename, "wb")

# set the channels
wf.setnchannels(channels)

# set the sample format
wf.setsampwidth(p.get_sample_size(FORMAT))

# set the sample rate
wf.setframerate(sample_rate)

# write the frames as bytes
wf.writeframes(b"".join(frames))

# close the file
wf.close()

# to playback the output file after you are finished recording
playsound("demotrack1.wav")







