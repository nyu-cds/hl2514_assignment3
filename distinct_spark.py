'''
Author: Hao Liu
Date: 5/6/2017
Spark script used for counting the total distinct words of input text file.
Total distinct words in pg2701.txt: 17355
'''


from pyspark import SparkContext
import re

# remove any non-words and split lines into separate words
# finally, convert all words to lowercase
def splitter(line):
    line = re.sub(r'^\W+|\W+$', '', line)
    line = line.encode('ascii','ignore')
    return map(str.lower, re.split(r'\W+', line))

if __name__ == '__main__':
	sc = SparkContext("local", "wordcount")
	
	text = sc.textFile('pg2701.txt')
	words = text.flatMap(splitter)
	words_mapped = words.map(lambda x: (x,1))
	sorted_map = words_mapped.sortByKey()
	counts = sorted_map.groupByKey()
	print('Total distinct words in this text: {}'.format(counts.count()))
	sc.stop()
