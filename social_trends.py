import time, random
import sys
sys.path.append("GoogleScraper-master")
#import GoogleScraper as gs
from twython import Twython, TwythonError
import KEYS

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

(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) = KEYS.keys()
tw = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def paper_tweets(author, title, urls):
    #allnames = author.split() # possible author names
    #lastname = allnames[len(allnames)-1]
    tweets = []

    # search title + author
    #results += gs.scrape("site:twitter.com \"" + title + "\" " + author, number_pages = 5)
    results = tw.search(q="site:twitter.com \"" + title + "\" " + author)
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
    for url in urls:
        #short_urls = get_short_urls(scholar_url)
        #for short_url in short_urls:
        #    results += gs.scrape("site:twitter.com " + short_url)
        #    time.sleep(random.uniform(2, 5))
        results = tw.search(q=url)
        tweets += [status['id'] for status in results['statuses']]
        #for tweet in results['statuses']:
        #    print(tweet)
        

    #TODO ID top tweets
    top_tweets = tweets[:30]
    #TODO better scoring system please
    trend_score = len(results)
    
    return (trend_score, top_tweets)
