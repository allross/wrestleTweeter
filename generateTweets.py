import linecache
import random

import markovify

# Get raw text as string.
with open("tweets.txt", encoding='utf-8') as f:
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text)



# Print three randomly-generated sentences of no more than 140 characters
tweets = []
for i in range(10):
    tweets.append(text_model.make_short_sentence(280))

#randomly append picture to tweets
chosen = random.choice(tweets)
with open("pics.txt", encoding='utf-8') as f:
    num = random.randint(0, 100)
    line = linecache.getline('pics.txt', num)
chosen += ' '
chosen += line
print(chosen)

#todo: i dont like these pics. maybe scrape images from cagematch instead like ugly indie pics