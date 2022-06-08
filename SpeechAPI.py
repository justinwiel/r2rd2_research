import speech_recognition as sr

class SpeechToText:

    def google_api(self,*,audio_file):
        try:
            r = sr.Recognizer()
            with sr.AudioFile(audio_file) as source:
                    audio_data = r.record(source)
                    print("File loading google... ")
                    text = r.recognize_google(audio_data, language="en-US")
                    text.lower()
                    print(text.split())
                    return text.split()
        except sr.UnknownValueError:
            print(f"{audio_file}             --file doesn't work--")
    
    def sphinx_api(self,*,audio_file):
        try:
            r = sr.Recognizer()
            with sr.AudioFile(audio_file) as source:
                    audio_data = r.record(source)
                    print("File loading sphinx... ")
                    text = r.recognize_sphinx(audio_data)
                    text.lower()
                    print(text.split())
                    return text.split()
        except sr.UnknownValueError:

            print(f"{audio_file}             --file doesn't work--")

# sp = SpeechToText()

