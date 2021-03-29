'''
Name: data_processer.py
Author: Nathalie de Palm
Date: 04-03-2021
'''

import sys

#def process(data, idioms):
#    idiom_counter = 0
#    non_idiom_counter = 0
#    for tweet in data:
#        chkpnt = 0
#        for idiom in idioms:
#            if idiom in tweet:
#                idiom_counter += 1
#                chkpnt = 1
#        if chkpnt == 0:
#            non_idiom_counter += 1
#    return idiom_counter, non_idiom_counter


	
def main(argv):
    if len(argv) != 3:
        print('Please enter the idiom-, 2015 data-, or 2020 data files in the command line while running this program.', file=sys.stderr)
        exit(-1)
		
    idioms_file = open(argv[1], 'r')
    idioms = idioms_file.readlines()
    idioms_file.close()
    with open(argv[2], 'r') as data:
        idiom_counter = 0
        non_idiom_counter = 0
        for tweet in data:
            chkpnt = 0
            for idiom in idioms:
                idiom2 = idiom.lower().rstrip('\n')
                if tweet.lower().find(idiom2) != -1:
                    idiom_counter += 1
                    chkpnt = 1
            if chkpnt == 0:
                non_idiom_counter += 1
    print('Tweets with Dutch idioms:', idiom_counter)
    print('Tweets without Dutch idioms:', non_idiom_counter)
    print('Total tweets:', (idiom_counter + non_idiom_counter))


if __name__ == '__main__':
    main(sys.argv)	
