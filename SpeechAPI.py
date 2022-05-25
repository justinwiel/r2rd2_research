import speech_recognition as sr

class SpeechToText:

    def google_api(self,*,audio_file):
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
                audio_data = r.record(source)
                print("File loading google... ")
                text = r.recognize_google(audio_data, language="en-US")
                text.lower()
                print(text.split())
                return text.split()
    
    def sphinx_api(self,*,audio_file):
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
                audio_data = r.record(source)
                print("File loading sphinx... ")
                text = r.recognize_sphinx(audio_data)
                text.lower()
                print(text.split())
                return text.split()

# sp = SpeechToText()

