from scholar import csv
from scholar import url_get
from scholar import txt

def main(query):
	
	csv_data = csv(query, author='',  count=20)#, header=True)
	for line in csv_data:
		print line
		line = line.split('|')
		if int(line[3]) > 0: 
			version_data = url_get(line[5], author='', count=20)
			print 'list start'
			for subline in version_data:
				subline = subline.split('|')
				print subline[1]
			print 'list end'
				


if __name__ == '__main__':
	main('bloom filter')
