from scholar import csv
from scholar import url_get
from scholar import txt

def main(query):

	
	csv_data = csv(query, author='',  count=1)#, header=True)
	print csv_data
	for line in csv_data:
#		print line
		line = line.split('|')
		title = line[0]
		authors = line[7].split(', ')
		venue = line[8].rstrip()
		venue = venue.lstrip()
		print venue
		version_urls = [line[1]]
		if False and len(line) >3 and int(line[3]) > 0: 
			version_data = url_get(line[5], author='', count=20)
			for subline in version_data:
				subline = subline.split('|')
				version_urls.append(subline[1])
				
#		print version_urls
		afds


if __name__ == '__main__':
	main('bloom filter')
