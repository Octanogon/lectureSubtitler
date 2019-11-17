import speech_recognition as sr
import os
from pydub import AudioSegment
from os import listdir
from os import rename
from pydub import AudioSegment
from subtitler import Video
import numpy as np
import datetime

class Speech_To_Text:
    def __init__(self, video_source):
        INTERVAL_FOR_SINGLE_SUBTITLE = 10 # sets amount of time that a subtitle will show
        length = len(AudioSegment.from_file(video_source))*1000
        self.convert_video_to_audio(video_source, "audio_file")
        self.create_n_second_audio_file("audio_file.wav", INTERVAL_FOR_SINGLE_SUBTITLE)
        subtitles = self.text_output_from_directory_of_audio("audio_file_words")
        video_with_subtitles = Video(video_source)
        for i, sub in enumerate(subtitles):
            if sub != None:
                if (i+1)*INTERVAL_FOR_SINGLE_SUBTITLE < length:
                    video_with_subtitles.addSubtitle(sub, str(datetime.timedelta(seconds=i*INTERVAL_FOR_SINGLE_SUBTITLE))+".00", str(datetime.timedelta(seconds=(i+1)*INTERVAL_FOR_SINGLE_SUBTITLE))+".00")
                else:
                    video_with_subtitles.addSubtitle(sub, str(datetime.timedelta(seconds=i*INTERVAL_FOR_SINGLE_SUBTITLE))+".00", str(datetime.timedelta(seconds=length))+".00")
        video_with_subtitles.createVideo()

    def convert_video_to_audio(self, source, destination):
        AudioSegment.from_file(source).export(destination+".wav", format="wav")

    def create_n_second_audio_file(self, audio_source, n):
        new_directory = f"./{audio_source.split('.')[0]}_words"
        if f"{audio_source.split('.')[0]}_words" not in os.listdir():
            os.makedirs(new_directory) # creates new directory to hold all the word audio files
        audio = AudioSegment.from_file(audio_source)
        length = len(audio)/1000
        for i in range(int(np.ceil(length/n))):
            self.produce_audio_segment(audio_source, i*n,(i+1)*n, name=f".//{new_directory}//word{i}")

    def produce_audio_segment(self, source, start, end, name=None): # enter start and end in second
        audio_file = AudioSegment.from_file(source)
        if end > len(audio_file)*1000:
            end = len(audio_file)*1000
        if name == None:
            audio_file[start*1000:end*1000].export(f"{source.split('.')[0]}_{start}-{end}.wav", format="wav")
        else:
            audio_file[start*1000:end*1000].export(name+".wav", format="wav")

    def run_speech_recognition_on_a_single_file(self, source):
        r = sr.Recognizer()
        with sr.AudioFile(source) as source:
            audio = r.record(source) # reads the entire audio file

        # recognize speech using Google Speech Recognition
        try:
            recog = r.recognize_google(audio)
            return recog
        except sr.UnknownValueError:
            return "Could not understand"
        except sr.RequestError as e:
            return "Could not request results from Google Speech Recognition service; {0}".format(e)

    def text_output_from_directory_of_audio(self, directory):
        list_of_outputs = []
        for x in range(len(listdir(directory))):
            audio_source = f"word{x}.wav"
            print(audio_source)
            # set up speech recogniser
            r = sr.Recognizer()
            with sr.AudioFile(directory+"/"+audio_source) as source:
                audio = r.record(source) # reads the entire audio file

            # recognize speech using Google Speech Recognition
            try:
                recog = r.recognize_google(audio)
                list_of_outputs.append(recog)
            except sr.UnknownValueError:
                list_of_outputs.append(None)
            except sr.RequestError as e:
                list_of_outputs.append(None)
        return list_of_outputs


Speech_To_Text("JamesAcaster.mp4")
