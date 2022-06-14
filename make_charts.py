
from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

# len = 5

data_google = [90.40, 0.8, 18.1, 5.4, 0] #FFT
dev_google=[4.2, 1.4, 19.9, 7.9, 0]
data_sphinx = [38.1, 1.2, 0, 0, 0.4] #FFT
dev_sphinx = [14.2, 1.8, 0, 0, 0.7]

data_google = [88.1, 87.7, 88.1, 88.1, 88.5]#Mel
dev_google = [4.5, 4.2, 5.2, 5.2, 3.9]
data_sphinx = [42.3, 0,0,0,0]#Mel
dev_sphinx = [15.4, 0,0,0,0]

data_google = [13.8, 1.9, 7.4, 0,0.8]#pnr
dev_google = [12.0, 3.5, 10.3,0,1.2]
data_sphinx = [1.6, 1.5,0,0, 0.8]#pnr
dev_sphinx = [1.8, 2.1,0,0,1.4]

data_google = [93.9, 90.8]
dev_google = [2.8, 4.9]

data_sphinx = [44.6, 43]
dev_sphinx = [12, 5.5]

# data_google = [90.0, 40.8]
# dev_google = [4.6, 16.2]



ruis = ["No noise", "Café", "Distorted", "Radio", "Train"]
titel = ["Man", "Vrouw"]
titel = ["Zonder plopkap", "Met plopkap"]

X_axis = np.arange(2)

bar1 = plt.bar(X_axis-.1, data_google, .2,  yerr=dev_google, label="Google")
bar2 = plt.bar(X_axis+.1, data_sphinx, 0.2, yerr=dev_sphinx, label="Sphinx")
i = 0
for rect in bar1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()*.2, height, f'{data_google[i]}', ha='center', va='bottom')
    i+=1
i = 0
for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()*.2, height, f'{data_sphinx[i]}', ha='center', va='bottom')
    i+=1
plt.xticks(X_axis, titel , fontsize=7)
plt.title('plopkap met mannelijke stem')
plt.ylabel('Gemiddelde correctheid')
plt.xlabel('Plopkap')
plt.legend()
plt.show()
plt.show()