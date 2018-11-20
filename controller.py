import pyaudio
import wave
import subprocess

running = True


def playaudio(filename): 
    chunk = 1024 # split the aufio file into 1MB chunks
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream=pa.open(
    format=pa.get_format_from_width(wf.getsampwidth()),
    channels=wf.getnchannels(),
    rate=wf.getframerate(),
    output=True
    )

    datastream = wf.readframes(chunk)

    while(datastream):
        stream.write(datastream)
        datastream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

playaudio('auido/alert1.wav')