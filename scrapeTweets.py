import re
import unicodedata

from twitter_scraper import get_tweets

# List of wrestling twitter accounts to scrape from.
users = ['mikethemiz', 'hulkhogan', 'joeyryanonline', 'SussexCoChicken', 'FrightmareLucha', 'thekingnickgage',
         'lastrealmanROH', 'KennyOmegamanX', 'RealDarioCueto',
         'JayWhiteNZ', 'MmmGorgeous', 'SamiZayn', 'the_ironsheik', 'BaronCorbinWWE', 'SamoaJoe', 'TherealRVD',
         'MattJackson13', 'trentylocks', 'facdaniels', 'SexyChuckieT',
         'SiNNbODHi', 'JimmyJacobsX', 'ricflairnatrboy', 'niajaxxwwe', 'wwerollins']

badLinks = ["https://twitter.com", ]
tweets = []


# Put tweets delineated by newline into a text file tweets.txt
def output_Tweets(tweets):
    with open('tweets.txt', 'w', encoding='utf-8') as f:
        for item in tweets:
            f.write("%s\n" % item)


def outpics(pics):
    with open('pics.txt', 'w', encoding='utf-8') as f:
        for item in pics:
            f.write("%s\n" % item)


# Clean up the scraped tweets
def clean_Tweets(tweets):
    newTweets = []
    for tweet in tweets:
        text = re.sub(r"(?:\@|https?\://)\S+", "", tweet)  # remove URLS from tweets
        text = text.replace("\xa0…", "")
        text = unicodedata.normalize("NFKD", tweet)  # Remove ugly Unicode characters, not sure if works yet
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


# todo: remove all pic.twitter from tweets and store in a separate list to randomly append to the end of a tweet its funnier that way
# todo: maybe sentiment analysis to only choose funny neg/pos tweets?

# Scrape tweets from the wrestlers list above
def scrape_Tweets():
    for user in users:
        try:
            for tweet in get_tweets(user, pages=1):
                tweets.append(tweet['text'])
        except:
            pass
    return tweets


# do nothing, just skip them


tweetList = scrape_Tweets()
tweetList = clean_Tweets(tweetList)
# pics = getPics(tweeeets)
# print(pics)
# outpics(pics)
# tweeeets = removePics(tweeeets)
# print(tweeeets)
output_Tweets(tweetList)
