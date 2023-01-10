#Import dependencies
import pandas as pd
import numpy as np
import whisper
import pyttsx3
#import pyaudio
import wave
import io
import time
import streamlit as st

#Text to speech model initialization
engine = pyttsx3.init()


def spell_word():
    engine.say("Spell")
    engine.say(text)
    engine.runAndWait()

#Validate answers
def check_ans():
    answer = input("type the word here:  ")
    answer = answer.lower()
    print(text)
    if answer == text.lower():
        st.write("Yeay!!!!!!, That's correct! You did It")
    else:
        st.write("Try again!!!!")


w_max = st.slider('How many words would you like to spell?', 0, 10, 3)
st.write("You have spelected to spell ", w_max, 'words')

ft = ["award", "cartoon", "charm",'swarm', 'garden', 'harvest', 'warned', 'warmth', 'guard', 'reward', 'quarter', 'toward', 'carpet', 'alarm','starving']


N = len(text)
cnt = 0

#This loop will run forever
while True:
    
    print(f"The {cnt} words is {ft[cnt]}")
    #the time alloted to spell is a function of the length of the word plus 1 sec
    time = len(ft[cnt]) + 1
    text = ft[cnt]
    spell_word()
    check_ans()
    engine = pyttsx3.init()
    cnt += 1
    if cnt == w_max:
        break
