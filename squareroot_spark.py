'''
Author: Hao Liu
Date: 5/6/2017
Spark script used for calculating the average square root.
'''

from pyspark import SparkContext
from operator import add
from math import sqrt

if __name__ == '__main__':
	sc = SparkContext("local", "product")
	# Create an RDD of numbers from 1 to 1,000
	nums = sc.parallelize(range(1, 1001))
	# Map the square root function to all elements in RDD
	nums_sqrt = nums.map(sqrt)
	# Calculate the average square root
	print('Average square root = {}'.format(nums_sqrt.fold(0, add)/float(nums.count())))
