import json
import matplotlib.pyplot as plt
import numpy as np
from SpeechAPI import SpeechToText
#class to test and evaluate data 
class test_data:
    #initializer for the class. it also loads the data from words.json
    def __init__(self) -> None:
        file = open("words.json")
        self.data = json.load(file)
        self.api_return = None 
    #this function uses a speechrecognizer class and sets the api return variable 
    def api(self, api = True, audiofile = None): #param api: True is google False is sphinx
        pass
        recog = SpeechToText()
        if api:
            self.api_return = recog.google_api(audio_file=audiofile)
        else:
            self.api_return = recog.sphinx_api(audio_file=audiofile)
    #this function evaluates the api return variable with the words in the json. 
    def evaluate_api(self):
        if self.api_return is not None:
            self.word_counter = 0
            total_correct = 0
            for key, value in self.data.items():
                if self.word_counter >= len(self.api_return):
                    break
                if key == self.api_return[self.word_counter].lower():
                    value["rights"] +=1
                    total_correct +=1
                else:
                    value["wrongs"] += 1
                value["tests"] += 1
                self.word_counter += 1
            print(total_correct/self.word_counter *100)
    #TODO function needs to be implemented 
    #this function reshapes audio files by adding a filter. 
    def add_filter(self, filter_nmr, audiofile):
        return audiofile
    #this function saves the updated dictionary and saves them in words.json
    def save(self):
        file = open("words.json", "w")
        json.dump(self.data, file, indent=6)
    #this function resets the file, it resets the counters 
    def reset_file(self):
        for key, value in self.data.items():
            value["rights"] = 0
            value["wrongs"] = 0
            value["tests"] = 0

    #this function shows the results in a bar type 
    def show_results(self):
        keys, rights, wrongs, tests = [], [], [], []
        for key, value in self.data.items():
            rights.append(value["rights"])
            wrongs.append(value["wrongs"])
            tests.append(value["tests"])
            keys.append(key)
        
        X_axis = np.arange(len(keys))
        plt.rcParams["figure.figsize"] = [7.00, 3.50]
        plt.rcParams["figure.autolayout"] = True
        plt.bar(X_axis-0.2, rights, 0.2, label = "Number of correctly recognized words", color="green")
        plt.bar(X_axis, wrongs, 0.2,  label = "Number of misrecognized words", color="red")
        plt.bar(X_axis + 0.2, tests, 0.2,  label = "Amount of tests", color="blue")
        plt.xticks(X_axis, keys , fontsize=7)
        plt.xlabel("Words")
        plt.ylabel("Amount")
        plt.title("Test results")
        plt.legend()
        manager = plt.get_current_fig_manager()
        manager.window.state('zoomed')
        plt.show()

test = test_data()
test.reset_file()
test.api(1, "test_sample.wav")
test.evaluate_api()
test.save()
test.show_results()