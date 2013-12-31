# Input: paper title 
# Output: total number of downloads in the last 6 weeks, in the last 12 months and overall

import urllib2
import BeautifulSoup
import pickle

PICKLE_FILE = "downloads.pickle"
cache = pickle.load(open(PICKLE_FILE, "rb"))

def downloads(title):
    if title in cache:
        return cache[title]
    
    # put the title into proper form to use as a query 
    query = title.strip().replace(" ","-");

    # base site 
    base = "http://dl.acm.org/results.cfm?query=" + query
    
    # sketchy things
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent','Mozilla/5.0')]
    response = opener.open(base)
    
    # find the string that contains all of the download data
    soup = BeautifulSoup(response.read())
    data = soup.find_all("strong")
    for i in data:
        result = str(i).find("Bibliometrics")
        if result > 0:
            scramble =  i.parent
            break 
    
    # extract the three download numbers from the string 
    string_scramble = str(scramble).split('/strong>:')[1].replace('\n',' ').split(',')
    downloads = []
    for i in string_scramble[:3]:
        curr_item = i.split(':')[1]
        if curr_item.strip() == 'n/a':
            curr_item = '0'
        downloads.append(int(curr_item))

    cache[title] = downloads
    pickle.dump(cache, open(PICKLE_FILE,'wb'))
    return downloads 















