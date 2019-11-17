from SpeechToText import Speech_To_Text
from subtitler import Video
from silenceTest import speedUpSilence
import sys

print(sys.argv)
if len(sys.argv) != 2:
    print("Error not the correct number of args")

else:
    inp = sys.argv[1]
    
    if inp.split(".")[1] != "mp4":
        print("Input needs to be mp4")
    
    else:
        Speech_To_Text(inp)
        
        #This should create subtitled_input?
        print("Subtitles created")
        # Then feed into silence remover
        
        speedUpSilence("subtitled_"+inp)


