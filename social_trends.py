import time, random
import sys
from twython import Twython, TwythonError
import KEYS
import pickle

PICKLE_FILE = "social_trends.pickle"
social_cache = pickle.load(open(PICKLE_FILE, "rb"))

class SocialTrends:
    def __init__(self, authors, title, urls):
        self.authors = authors
        self.title = title
        self.urls = urls
        # hackathon hack!
        if not len(authors):
            self.authors = [""]
        if not len(urls):
            self.urls = ["NOT_APPLICABLE_90125738943705"]
        
        if (authors[0], title) in social_cache:
            self.twitter_results = social_cache[(authors[0], title, urls[0])]['twitter']
            return

        social_cache[(self.authors[0], self.title, self.urls[0])] = {}
        (APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) = KEYS.keys()
        self.tw = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        self.twitter_results = ""
        self.reddit_results = ""

    def paper_tweets(self):
        if self.twitter_results:
            return self.twitter_results

        #allnames = author.split() # possible author names
        #lastname = allnames[len(allnames)-1]
        tweets = []
        trend_score = 0

        # possible urls
        for url in self.urls:
            url = url.lstrip("http://").lstrip("https://").lstrip("www.")
            results = self.tw.search(q=url, count=50)
            if results['statuses']:
                (new_tweets, rt_counts) = zip(*[(status['id'], status['retweet_count']) for status in results['statuses']])
                tweets += new_tweets
                trend_score += sum(rt_counts)

                
        # search title + author
        #TODO count retweets and use in ranking
        for author in self.authors:
            results = self.tw.search(q="\"" + self.title + "\" " + author, count=50)
            if results['statuses']:
                (new_tweets, rt_counts) = zip(*[(status['id'], status['retweet_count']) for status in results['statuses']])
                tweets += new_tweets
                trend_score += sum(rt_counts)
        #TODO see if there are any new urls to check in results?
        #TODO search author + title fragments

        #TODO better scoring system please
        trend_score += len(tweets)
        #TODO ID top tweets
        top_tweets = [(t, self.tw.show_status(id=t)) for t in tweets[:30]]

        self.twitter_results = (trend_score, top_tweets)
        social_cache[(self.authors[0], self.title, self.urls[0])]['twitter'] = self.twitter_results
        pickle.dump(social_cache, open(PICKLE_FILE,'wb'))
        return self.twitter_results
