import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils

"""
Following tutorial from:
https://www.analyticsvidhya.com/blog/2018/03/text-generation-using-python-nlp/
"""

#open corpus
text = (open("/tweets.txt").read())
text = text.lower()

#map characters to numbers in dicts
chars = sorted(list(set(text)))
number_to_char = {n:char for n, char in enumerate(chars)}
char_to_number = {char:n for n, char in enumerate(chars)}

# Dats preprocessing
X = [] #train array
Y = [] #target array
length = len(text)
seq_length = 100 #Sequence length to consider b4 predicting a char??

for i in range(0, length-seq_length, 1):
    sequence = text[i:i + seq_length]
    label = text[i + seq_length]
    X.append([char_to_number[char] for char in sequence])
    Y.append(char_to_number[label])