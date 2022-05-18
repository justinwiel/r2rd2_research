from statistics import mode
from numpy import empty
import speech_recognition as sr
import json
from sqlalchemy import false, true

"""
    Name of the class: SpeechToText

    What it does:
    Activates the speechAPI and sets the language.  
"""
class SpeechToText:
    """
        This function sets the language. 
        @param language: is just a string like "Dutch" or "English"
    """
    def languageConverter(self,*,language):
        '''This function converts the languages to the right format for the function: speechRecoginzer'''
        switch_language = {
            "Dutch": "nl-NL",
            "English": "en-US",
        }
        return switch_language[language] 
    """
    Function for the speechRecognizer 
    """
    def google_api(self,*,language):
        '''This function recognizes speech and prints out the text'''
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("You can talk :) ")
                audio_data = r.record(source, duration=5)
                print("Recognizing...")
                text = r.recognize_google(audio_data, language=self.languageConverter(language=language))
                print(text.split())
    
    def api(self,*,language):
        '''This function recognizes speech and prints out the text'''
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("You can talk :) ")
                audio_data = r.record(source, duration=5)
                print("Recognizing...")
                text = r.recognize_google(audio_data, language=self.languageConverter(language=language))
                print(text.split())
    

        
sp = SpeechToText()
# sp.google_api(language="Dutch")
sp.api()