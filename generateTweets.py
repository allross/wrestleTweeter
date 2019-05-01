import linecache
import random

import markovify

# Get raw text from tweets.txt as string.
with open("tweets.txt", encoding='utf-8') as f:
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text)

# Print three randomly-generated sentences of no more than 140 characters
tweets = []
for i in range(10):
    tweets.append(text_model.make_short_sentence(280))

# randomly append picture to tweets
chosen = random.choice(tweets)
chosen += ' '


# Returns a single randomly generated tweet
def get_Single_Tweet():
    chosen = random.choice(tweets)
    return chosen

