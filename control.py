from scholar import csv
from scholar import url_get
from scholar import txt

def main(query):

	article_list = []
	
	csv_data = csv(query, author='',  count=20)#, header=True)

	for line in csv_data:
		line = line.split('|')

		title = line[0]
		authors = line[7].split(', ')
		venue = line[8].rstrip()
		venue = venue.lstrip()
		version_urls = [line[1]]

		if len(line) >3 and int(line[3]) > 0: 
			version_data = url_get(line[5], author='', count=20)
			for subline in version_data:
				subline = subline.split('|')
				version_urls.append(subline[1])

		article_list.append((title, authors, version_urls, venue))

	print article_list
				
		


if __name__ == '__main__':
	main('bloom filter')
