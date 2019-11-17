import speech_recognition as sr
import os
from os import path
from pydub import AudioSegment
from os import path
from os import listdir
from os import rename
from pydub import AudioSegment
from pydub.silence import split_on_silence
import numpy as np
from subtitler import Video
import datetime
class Utility:
    def convert_audio_file_to_wave(self, source, destination):
        AudioSegment.from_file(source).export(destination+".wav", format="wav")

    def split_audio_by_word(self, source, min_silence=500, silence_length=700, thresthold=-30):
        new_directory = f"./{source.split('.')[0]}_words"
        if f"{source.split('.')[0]}_words" not in os.listdir():
            os.makedirs(new_directory) # creates new directory to hold all the word audio files
        sound_file = AudioSegment.from_wav(source) # creates a AudioSegment object to handle manipulation of the audio
        audio_clips = split_on_silence(sound_file, min_silence_len=50, keep_silence=0, silence_thresh=-30) # creates an array of the audio clips for the words based off the parameters set

        #print(len(audio_chunks)) # outputs the number of audio files created
        # iterates through the array of all the clips and saves them all to a different wav file in the set directory
        for i, clip in enumerate(audio_clips):
            out_file = f".//{new_directory}//word{i}.wav"
            #print (f"Exporting {out_file}")
            clip.export(out_file, format="wav")

    def produce_audio_segment(self, source, start, end, name=None): # enter start and end in second
        audio_file = AudioSegment.from_file(source)
        if end > len(audio_file)*1000:
            end = len(audio_file)*1000
        if name == None:
            audio_file[start*1000:end*1000].export(f"{source.split('.')[0]}_{start}-{end}.wav", format="wav")
        else:
            audio_file[start*1000:end*1000].export(name+".wav", format="wav")

    def produce_video_segment(self, source, start, end, name=None): # enter start and end in second
        video_file = AudioSegment.from_file(source)
        if end > len(video_file)*1000:
            end = len(video_file)*1000
        if name == None:
            video_file[start*1000:end*1000].export(f"{source.split('.')[0]}_{start}-{end}.mp4", format="mp4")
        else:
            video_file[start*1000:end*1000].export(name+".mp4", format="mp4")

    def split_audio_into_n_pieces(self, audio_source, n):
        new_directory = f"./{audio_source.split('.')[0]}_words"
        if f"{audio_source.split('.')[0]}_words" not in os.listdir():
            os.makedirs(new_directory) # creates new directory to hold all the word audio files
        audio = AudioSegment.from_file(audio_source)
        length = len(audio)/1000
        for i in range(n):
            self.produce_audio_segment(audio_source, i*length/n,(i+1)*length/n, name=f".//{new_directory}//word{i}")

    def create_n_second_audio_file(self, audio_source, n):
        new_directory = f"./{audio_source.split('.')[0]}_words"
        if f"{audio_source.split('.')[0]}_words" not in os.listdir():
            os.makedirs(new_directory) # creates new directory to hold all the word audio files
        audio = AudioSegment.from_file(audio_source)
        length = len(audio)/1000
        for i in range(int(np.ceil(length/n))):
            self.produce_audio_segment(audio_source, i*n,(i+1)*n, name=f".//{new_directory}//word{i}")

    def stitch_audio_files_together(self, array_of_files, file_name="combined_file.wav"):
        total_file = AudioSegment.silent(duration=100)
        for source in array_of_files:
            total_file = total_file + AudioSegment.from_file(source)
        total_file.export(file_name, format="wav")

    def split_audio_by_sentence(self, audio_source, sentence):
        words = sentence.split(" ") # split sentence into words
        no_of_characters = len("".join(words)) # count characters
        audio_file = AudioSegment.from_file(audio_source)
        # calculate start and end times for the sections of audio for each word
        word_times = {}
        portions_of_total_time = [((len(word))/(no_of_characters))*(len(audio_file)/1000) for word in words ] # get proportion of total time in seconds for this word
        for i, word in enumerate(words):
            if len(word_times) == 0:
                word_times[word] = [0,portions_of_total_time[i]]
            else:
                word_times[word] = [word_times[words[i-1]][1],word_times[words[i-1]][1] + portions_of_total_time[i]]
        for word in word_times:
            self.produce_audio_segment(audio_source,word_times[word][0],word_times[word][1], name=word)
        return word_times

    def build_repeated_word(self, audio_file, number_of_repeats):
        silence = AudioSegment.silent(duration=500)
        audio = AudioSegment.from_file(audio_file)
        repeated_file = silence + (audio+silence)*number_of_repeats
        repeated_file.export(f"{'.'+audio_file.split('.')[-2]}_times_{number_of_repeats}.wav", format="wav")

    def convert_audio_file_to_wave(self, source, destination):
        AudioSegment.from_file(source).export(destination+".wav", format="wav")

#Speech_To_Text().split_audio_by_word("hank_green.wav")
#Speech_To_Text().convert_audio_file_to_wave("barackobama2004dncARXE.mp3", "barack")
#Speech_To_Text().split_audio_by_word("hank_green.wav" ,min_silence=100, thresthold=-20)
#print(Speech_To_Text().run_speech_recognition_on_a_single_file("./Maths_words/word12.wav"))
#Speech_To_Text().produce_video_segment("OxfordMathematics.mp4",600,720)
#print(Speech_To_Text().run_speech_recognition_on_a_single_file("vsaurce_words//word1.wav"))
#Speech_To_Text().stitch_audio_files_together([f".//hank_green_words//word{x}.wav" for x in range(30)])
#print(Speech_To_Text().split_audio_by_word("barack_15-20_words/word1.wav"))
#Speech_To_Text().relabel_words_based_on_speech_recognition("./vsaurce_words")
#Speech_To_Text().build_repeated_word("./alphabet_words/word0.wav",5)

#Speech_To_Text().stitch_audio_files_together([f".//barack_words//word{x}.wav" for x in range(19,22)])
#Speech_To_Text().convert_video_to_audio("Oxford Mathematics 1st Year Student Lecture - Introductory Calculus-I3GWzXRectE.mp4","Maths")
#Speech_To_Text().split_audio_by_word("vsaurce.wav",min_silence=1000, silence_length=500 ,thresthold=-20)
#Speech_To_Text().split_audio_into_n_pieces("vsaurce.wav", 100)
#Speech_To_Text().create_n_second_audio_file("Maths.wav", 10)
#Speech_To_Text().relabel_words_based_on_speech_recognition("./Maths_words")
