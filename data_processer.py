'''
Name: data_processer.py
Author: Nathalie de Palm
Date: 04-03-2021
'''

import sys

def process(data, idioms):
	for tweet in data:
		for idiom in idioms:
			if idiom in tweet:
				idiom_counter += 1
			else:
				non_idiom_counter += 1
	return idiom_counter, non_idiom_counter


def results(idiom_2015, non_idiom_2015, idiom_2020, non_idiom_2020):
	print('Tweets with Dutch idioms in 2015:', idiom_2015)
	print('Tweets with Dutch idioms in 2020:', idiom_2020)
	print('Tweets without Dutch idioms in 2015:', non_idiom_2015)
	print('Tweets without Dutch idioms in 2020:', non_idiom_2020)
	print('Total tweets with Dutch idioms:', (idiom_2015 + idiom_2020))
	print('Total tweets without Dutch idioms:', (non_idiom_2015 + non_idiom_2020))
	print('Total tweets in 2015:', (idiom_2015 + non_idiom_2015))
	print('Total tweets in 2020:', (idiom_2020 + non_idiom_2020))
	
	
def main(argv):
	if len(argv) != 4:
		print('Please enter the idiom-, 2015 data-, and 2020 data files in the command line while running this program.', file=sys.stderr)
		exit(-1)
		
	idioms = open(argv[1], 'r').readlines()
	data_2015 = open(argv[2], 'r').readlines()
	data_2020 = open(argv[3], 'r').readlines()
	
	results(process(data_2015, idioms), process(data_2020, idioms))
	
	idioms.close()
	data_2015.close()
	data_2020.close()
	
if __name__ == '__main__':
	main(sys.argv)
	
	
	
	
	
