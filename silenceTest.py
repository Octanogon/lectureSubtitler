import subprocess

def speedUpSilence(inp):

    INPUT = inp
    # Outputs all the silences to log.txt
    subprocess.call("ffmpeg -i {0} -af silencedetect=n=-25dB:d=2,ametadata=print:file=log.txt -f null -".format(INPUT).split(" "), stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)


    # Read in the silences and split and speed up the clips

    with open("log.txt", 'r') as f:
     
        
        
        print("Worked out silences")
        endOfLast = 0
        x = 0
        # Each silence is four entries
        line = f.readline()
        while line != "":
            
            while "start" not in line and line != "":
                line = f.readline()

            if line == "":
                break
                
            start = line.split("=")[1].rstrip()
            
            while "end" not in line and line != "":
                line = f.readline()
                
            if line == "":
                break
            
            end = line.split("=")[1].rstrip()
                
            print("-----------")
            print(endOfLast)
            print(start)
            print(end)
            
            # Split the files
            
            
            # This will be regular talking
            subprocess.call("ffmpeg -y -i {0} -ss {1} -to {2} {3}.mp4".format(INPUT, str(float(endOfLast)), str(float(start)), x).split(" "))
            x += 1
            # This will be silence
            subprocess.call(("ffmpeg -y -i {0} -ss {1} -to {2} slow.mp4").format(INPUT, str(float(start)), str(float(end))).split(" "))
            subprocess.call(("ffmpeg", "-y", "-i", "slow.mp4", "-r", "50","-vf", "setpts=0.5*PTS", "-af", "atempo=2.0", "{0}.mp4".format(x)), shell=True)
            x += 1
            
            endOfLast = end
            
            line = f.readline()


    # Time to string them together

    with open("cat.txt", 'w') as f:
        for i in range(1,x):
            f.write("file {0}.mp4\n".format(i))
            
    subprocess.call("ffmpeg -y -f concat -safe 0 -i cat.txt output.mp4".split(" "))

