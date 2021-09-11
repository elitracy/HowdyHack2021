from pydub import AudioSegment
from pydub.playback import play

# song = AudioSegment.from_wav("sample.wav")

#clip is an Audio Segment, start is how much to trip
def trimAudio(clip, clipBegin, clipEnd):
    return clip[clipBegin:clipEnd]

#returns (firstClip, secondClip)
def clipAudio(clip,splitTime):
    return clip[:splitTime], clip[splitTime:]

def playAudio(clip):
    play(clip)
    pass

