import json
import matplotlib.pyplot as plt
import numpy as np

#class to test and evaluate data 
class test_data:
    #initializer for the class. it also loads the data from words.json
    def __init__(self) -> None:
        file = open("words.json")
        self.data = json.load(file)
        self.api_return = [] #None TODO set to None when speech api is merged
        for key, value in self.data.items(): #TODO remove this forloop when self.api_return is set to None
            self.api_return.append(key)
    #this function uses a speechrecognizer class and sets the api return variable 
    def api(self, api = True):
        pass
        recog = None #SpeechToText TODO fix this when github is merged! 
        if api:
            self.api_return = recog.google_api(language = "Dutch")
        else:
            self.api_return = recog.api()
    #this function evaluates the api return variable with the words in the json. 
    def evaluate_api(self):
        if self.api_return is not None:
            self.word_counter = 0
            for key, value in self.data.items():
                if key == self.api_return[self.word_counter]:
                    value["rights"] +=1
                else:
                    value["wrongs"] += 1
                value["tests"] += 1
                self.word_counter += 1
    #TODO function needs to be implemented 
    #this function reshapes audio files by adding a filter. 
    def add_filter(self):
        pass
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
        plt.bar(X_axis-0.2, rights, 0.2, label = "Number of correctly recognized words", color="green")
        plt.bar(X_axis, wrongs, 0.2,  label = "Number of misrecognized words", color="red")
        plt.bar(X_axis + 0.2, tests, 0.2,  label = "Amount of tests", color="blue")
        plt.xticks(X_axis, keys)
        plt.xlabel("Words")
        plt.ylabel("Amount")
        plt.title("Test results")
        plt.legend()
        plt.show()

test = test_data()
test.evaluate_api()
test.reset_file()
test.save()
test.show_results()