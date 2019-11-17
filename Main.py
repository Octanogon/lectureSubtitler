from SpeechToText import Speech_To_Text
from subtitler import Video
from silenceTest import speedUpSilence
import sys

if len(sys.argv) != 2:
    print("Error not the correct number of args")

else:
    input = sys.argv[0]
    output = sys.argv[1]
    
    if output.split(".")[1] != "mp4" or input.split(".")[1] != "mp4":
        print("Input and output need to be mp4s")
    
    else:
        Speech_To_Text = Speech_To_Text(input)
        
        #This should create subtitled_input?
        
        # Then feed into silence remover
        
        speedUpSilence("subtitled_"+input)


