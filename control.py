from scholar import csv
from scholar import url_get
from scholar import txt
import social_trends
import time
import downloads
import json
import random

def main(query):

	json_output = []

	article_list = []
	
	csv_data = csv(query, author='',  count=3)#, header=True)

	for line in csv_data:
		line = line.split('|')

		title = line[0]
		authors = line[7].split(', ')
		venue = line[8].rstrip()
		venue = venue.lstrip()
		version_urls = [line[1]]

		if len(line) >3 and int(line[3]) > 0: 
			version_data = url_get(line[5], author='', count=20)
			time.sleep(random.uniform(2,5))
			for subline in version_data:
				subline = subline.split('|')
				version_urls.append(subline[1])

		article_list.append((authors, title, version_urls, venue))

	toSort = []

	for paper in article_list:

		tw = social_trends.SocialTrends(paper[0], paper[1], paper[2])
		(score, tweets) = tw.paper_tweets()
		recent_downloads = downloads.downloads(paper[1])	
	
		if score > 0 or recent_downloads[0] > 0:	
			json_paper = dict()
			json_paper['title'] = paper[1]
			json_paper['authors'] = paper[0]
			json_paper['urls'] = paper[2]
			json_paper['venue'] = paper[3]
			json_paper['tweets'] = []

			for (tid, tweet) in tweets:
				json_tweet = dict()
				json_tweet['author'] = tweet['user']['screen_name']
				json_tweet['content'] = tweet['text']
				json_tweet['url'] = "http://twitter.com/"+tweet['user']['screen_name']+"/status/"+tweet['id_str']
				json_paper['tweets'].append(json_tweet)

				
			toSort.append((score, recent_downloads[0], json_paper))							
		time.sleep(2)

	toJson= [y[2] for y in sorted(toSort, key=lambda x : x[0]*10000+x[1])]

	return json.dumps(toJson)
	

if __name__ == '__main__':
	main('Retweeting Fukushima')
