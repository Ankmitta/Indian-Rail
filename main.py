import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS 

def textToSpeech(text,filename):
    mytext=str(text)
    language='hi'
    myobj=gTTS(text=mytext, Lang=language, slow=True)
    myobj.save(filename)

def mergeAudios(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined=combined+AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    # 1 Generate kripya dhyan dijiye
    audio= AudioSegment.from_mp3("Train Announcement.mp3")
    start=500
    finish=3500
    audioProcessed=audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2 from city
    audio= AudioSegment.from_mp3("Train Announcement.mp3")
    start=22800
    finish=24600
    audioProcessed=audio[start:finish]
    audioProcessed.export("2_hindi.mp3", format="mp3")

    # 3 se chalkar
    audio= AudioSegment.from_mp3("Train Announcement.mp3")
    start=8900
    finish=9600
    audioProcessed=audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    #4 via city
    audio= AudioSegment.from_mp3("Train Announcement.mp3")
    start=24800
    finish=27000
    audioProcessed=audio[start:finish]
    audioProcessed.export("4_hindi.mp3", format="mp3")
    
    #5 generate train no
    audio= AudioSegment.from_mp3("Train Announcement.mp3")
    start=3500
    finish=5900
    audioProcessed=audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    #6 train no and name
    audio= AudioSegment.from_mp3("Train Announcement.mp3")
    start=6000
    finish=6300
    audioProcessed=audio[start:finish]
    audioProcessed.export("6_hindi.mp3", format="mp3")

    #7 par aa rhi h
    audio= AudioSegment.from_mp3("Train Announcement.mp3")
    start=13000
    finish=15700
    audioProcessed=audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")



    pass 

def generateAnnouncement(filename):
    df=pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        textToSpeech(item['From'],'2_hindi.mp3')
 
        textToSpeech(item['Via'], '4_hindi.mp3')

        textToSpeech(item['Train no'], '5_hindi.mp3')

        audios=[f"{i}_hindi.mp3" for i in range(1,7)]
        announcement=mergeAudios(audios)
        announcement.export(f"announcement_{index+1}.mp3", format="mp3")

if __name__ == "__main__":
    print("Generating skeleton...")
    generateSkeleton()
    print("Now Generating announcement..")
    generateAnnouncement('Book1.xlsx')