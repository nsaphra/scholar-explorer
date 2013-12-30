import time, random
import sys
#sys.path.append("GoogleScraper-master")
#import GoogleScraper as gs
from twython import Twython, TwythonError
import praw
import KEYS
import pickle

#TINYURL_SHORTEN = "http://tinyurl.com/api-create.php?url="
#OWLY_SHORTEN = "http://ow.ly/api/1.1/url/shorten?apiKey=$ACCESS&longUrl="
#bitly = bitly_api.Connection(access_token=$ACCESS)
    
#def get_short_urls(url):
#    shorts = []
#    shorts += [bitly.shorten(url)]
#    shorts += [urllib2.urlopen(TINYURL_SHORTEN+url).read()]
#    shorts += [Googl.shorten(url).short_url]
#    shorts += [urllib2.urlopen(OWLY_SHORTEN+url)]
#    return shorts

social_cache = {} #TODO pickle

class SocialTrends:
    def __init__(self, author, title, urls):
        if (author, title) in social_cache:
            self.twitter_results = social_cache[(author, title)]['twitter']
            self.reddit_results = social_cache[(author, title)]['reddit']
            return

        (APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) = KEYS.keys()
        self.tw = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        self.rd = praw.Reddit(user_agent="scholar-explorer")
        self.author = author
        self.title = title
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
        #results += gs.scrape("site:twitter.com \"" + title + "\" " + author, number_pages = 5)
        results = self.tw.search(q="site:twitter.com \"" + self.title + "\" " + self.author)
        tweets += [status['id'] for status in results['statuses']]
        #for tweet in results['statuses']:
        #    tweets.append


        #TODO see if there are any new urls to check in results?
        # search author + title fragments
        #title_toks = title.split()
        #for i in range(3, len(title_toks)):
        #    gs = GoogleSearch("\"" + " ".join(title_toks[:i]) + "\" " + author)
        #    gs.results_per_page = 20

        # possible urls
        for url in self.urls:
            #short_urls = get_short_urls(scholar_url)
            #for short_url in short_urls:
            #    results += gs.scrape("site:twitter.com " + short_url)
            #    time.sleep(random.uniform(2, 5))
            results = self.tw.search(q=url)
            tweets += [status['id'] for status in results['statuses']]
            #for tweet in results['statuses']:
            #    print(tweet)

        #TODO better scoring system please
        trend_score = len(tweets)
        #TODO ID top tweets
        top_tweets = [(t, self.tw.show_status(id=t)) for t in tweets[:30]]

        self.twitter_results = (trend_score, top_tweets)
        return self.twitter_results

    #TODO finish implementing
    def paper_reddits(self):
        if self.reddit_results:
            return self.reddit_results
            
        reddits = []
        for url in self.urls:
            results = self.rd.search(url)
            for result in results:
                new_reddit = {}
                #TODO

        self.reddit_results = (trend_score, top_reddits)
