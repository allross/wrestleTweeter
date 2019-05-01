import re

from twitter_scraper import get_tweets

users = ['mikethemiz', 'hulkhogan', 'joeyryanonline', 'SussexCoChicken', 'FrightmareLucha', 'thekingnickgage', 'lastrealmanROH', 'KennyOmegamanX', 'RealDarioCueto',
         'JayWhiteNZ', 'MmmGorgeous', 'SamiZayn', 'the_ironsheik', 'BaronCorbinWWE', 'SamoaJoe', 'TherealRVD', 'MattJackson13', 'trentylocks', 'facdaniels', 'SexyChuckieT',
         'SiNNbODHi', 'JimmyJacobsX', 'ricflairnatrboy', 'niajaxxwwe', 'wwerollins']
tweets = []

#put tweets delineated by newline into a text file
def outtweets(tweets):
    with open('tweets.txt', 'w', encoding='utf-8') as f:
        for item in tweets:
            f.write("%s\n" % item)

def outpics(pics):
    with open('pics.txt', 'w', encoding='utf-8') as f:
        for item in pics:
            f.write("%s\n" % item)


def cleantweets(tweets):
    badLinks = ["https://twitter.com", ]
    newTweets = []
    for tweet in tweets:
        text = re.sub(r"(?:\@|https?\://)\S+", "", tweet)  # remove URLS from tweets
        text = text.replace("\xa0…", "")  # remomve this ugly thing idkw hat it is
        # add a space before pic.twitter so the picture will load in the tweet
        text = text.replace("pic.twitter", " pic.twitter")
        newTweets.append(text)
    return newTweets

def getPics(tweets):
    pictures = []
    for tweet in tweets:
        if "pic.twitter.com" in tweet:
            for word in tweet.split():
                if word.startswith("pic.twitter.com"):
                    pictures.append(word)  # add picture
    return pictures

def removePics(tweets):
    newTweets = []
    for tweet in tweets:
        if "pic.twitter.com" in tweet:
            for word in tweet.split():
                if word.startswith("pic.twitter.com"):
                    tweet = tweet.replace(word, "")
                    newTweets.append(tweet)
        newTweets.append(tweet)
    return newTweets

#todo: remove all pic.twitter from tweets and store in a separate list to randomly append to the end of a tweet its funnier that way
#todo: maybe sentiment analysis to only choose funny neg/pos tweets?



for user in users:
    try:
        for tweet in get_tweets(user, pages=3):
            tweets.append(tweet['text'])
    except:
        pass
# do nothing, just skip them

tweeeets = cleantweets(tweets)
pics = getPics(tweeeets)
#print(pics)
outpics(pics)
#tweeeets = removePics(tweeeets)
#print(tweeeets)
#outtweets(tweeeets)
