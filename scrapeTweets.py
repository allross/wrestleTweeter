import re
import unicodedata

from twitter_scraper import get_tweets

# List of wrestling twitter accounts to scrape from.
users = ['hulkhogan', 'joeyryanonline', 'SussexCoChicken', 'FrightmareLucha', 'thekingnickgage',
         'lastrealmanROH', 'KennyOmegamanX', 'RealDarioCueto',
         'JayWhiteNZ', 'MmmGorgeous', 'SamiZayn', 'the_ironsheik', 'BaronCorbinWWE', 'SamoaJoe', 'TherealRVD',
         'MattJackson13', 'trentylocks', 'facdaniels', 'SexyChuckieT',
         'SiNNbODHi', 'JimmyJacobsX', 'ricflairnatrboy', 'niajaxxwwe', 'wwerollins', 'markostunt', 'wressocietyx',
         'njpwglobal', 'reyfenixmx', 'pentagonjunior', 'go2sleepyhollow', 'dragoaaa', 'cheeseburgerroh',
         'mmmgorgeous', 'samizayn', 'ivar_wwe', 'gentlemanjervis', 'mrgmsi_bcage', 'petedunneyxb',
         'scottdawsonwwe', 'realjeffcobb', 'codyrhodes', 'tlee910', 'thebobbyfish', 'officialpwg',
         'janelababy', 'thedaltoncastle', 'korcombat', 'futuremeltzer', 'brethart', 'lukeharperwwe', 'therealec3',
         'wwedramaking', 'mdoggmattcross', 'scottsteiner','randyorton', 'lufisto', 'jimmyhavoc', 'adamcolepro',
         'jigsawwrestling', 'erickrowan', 'gentlemanjackg', 'gogoach', 'speedballbailey', 'kikutarosan', 'superkingofbros',
         'realbulljames', 'nickjacksonyb', 'kaijubigbattel', 'maffewgregg', 'matthardybrand', 'willie_mack', 'eviluno',
         'combatzone', 'ultramantis']


# TODO: ignore tweets containing these words
blackListedWords = []
tweets = []


# Scrape tweets from the wrestlers list above
def scrape_Tweets():
    for user in users:
        try:
            for tweet in get_tweets(user, pages=3):
                tweets.append(tweet['text'])
        except:
            pass
    return tweets


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
        text = unicodedata.normalize("NFKD", text)  # Remove ugly Unicode characters, not sure if works yet
        text = re.sub(r"(?:\@|s?\://)\S+", "", text)  # remove URLS from tweets
        text = ' '.join(word for word in text.split(' ') if not word.startswith('pic.twitter'))  # Remove pic.twitter URLS
        text = ' '.join(word for word in text.split(' ') if not ("pic.twitter" in word))  # Remove pic.twitter URLS
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

tweetList = scrape_Tweets()
tweetList = clean_Tweets(tweetList)
output_Tweets(tweetList)
