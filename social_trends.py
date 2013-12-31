import time, random
import sys
from twython import Twython, TwythonError
import KEYS
import pickle

PICKLE_FILE = "social_trends.pickle"
social_cache = pickle.load(open(PICKLE_FILE, "rb"))

class SocialTrends:
    def __init__(self, author, title, urls):
        self.author = author
        self.title = title
        
        if (author, title) in social_cache:
            self.twitter_results = social_cache[(author, title)]['twitter']
            return

        social_cache[(self.author, self.title)] = {}
        (APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) = KEYS.keys()
        self.tw = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        self.urls = urls
        self.twitter_results = ""
        self.reddit_results = ""

    def paper_tweets(self):
        if self.twitter_results:
            return self.twitter_results

        #allnames = author.split() # possible author names
        #lastname = allnames[len(allnames)-1]
        tweets = []

        # search title + author
        #TODO count retweets and use in ranking
        results = self.tw.search(q="site:twitter.com \"" + self.title + "\" " + self.author, count=100)
        tweets += [status['id'] for status in results['statuses']]
        #TODO see if there are any new urls to check in results?
        #TODO search author + title fragments

        # possible urls
        for url in self.urls:
            url = url.lstrip("http://").lstrip("https://").lstrip("www.")
            results = self.tw.search(q=url, count=100)
            tweets += [status['id'] for status in results['statuses']]

        #TODO better scoring system please
        trend_score = len(tweets)
        #TODO ID top tweets
        top_tweets = [(t, self.tw.show_status(id=t)) for t in tweets[:30]]

        self.twitter_results = (trend_score, top_tweets)
        social_cache[(self.author, self.title)]['twitter'] = self.twitter_results
        pickle.dump(social_cache, open(PICKLE_FILE,'wb'))
        return self.twitter_results
