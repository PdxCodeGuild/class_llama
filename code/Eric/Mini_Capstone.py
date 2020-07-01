# Idea for Mini Capstone: ****U/Record**** a FREE Web App

# My mini capstone would be a start to help some struggling artists with a free, simple, and easy to use
# recording online web app! Record original music or voice over work. All the features needed to 
# record a decent .wav or .mp3 file are all included. Create an account on Soundcloud.com or a 
# YouTube Artist Channel and upload your recordings!

"""
Might lead into the final Capstone Project
Potential to add music theory (notation)
Metronome or Back Beat to play along with...
Use an Audio Converter program to convert mp3 to FLAC (Lossless) file for higher quality sound
pip installed pyaudio, wave, playsound, soundfile and ftransc 
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

# ftransc is a python library for converting audio files across various formats
import ftransc


"""
*****SETTINGS for RECORDING******
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

# How many seconds to record
record_seconds = 30

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

# to playback the output file
playsound("demotrack1.wav")







