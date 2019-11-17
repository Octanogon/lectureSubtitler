import subprocess


SUBTITLE_LINE = "Dialogue: 0,{0},{1},Default,,0,0,0,,{\fad(500,500)}{2}"

class Video():
    
    def __init__(self, videoPath):
    
        self.path = videoPath
        self.subtitles = []
    
    def addSubtitle(self, text, start, end):
        '''
            Adds a subtitle to the list of subtitles
        '''
        
        # Format of time should be h:mm:ss.ss
        subtitleLine = SUBTITLE_LINE.format(start, end, text)
        
        self.subtitles.append(subtitleLine)
        
    
    
    def makeSubtitleFile(self):
        '''
            Creates the fade.ass file creating all of the subtitles
        '''
        
        # First read in the template file
        with open("fadeTemplate.ass", 'r') as f:
            template = f.readlines()
            
        # Add our subtitles
        for subtitle in self.subtitles:
            template.append(subtitle)
            
            
        with open("fade.ass", 'w') as f:
            f.writelines(template)
            
            
    def createVideo(self):
        
        self.makeSubtitleFile()
        
        subprocess.call("ffmpeg -i {0} -vf subtitles=fade.ass -c:a copy subtitled_{0}".format(self.videoPath), stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)