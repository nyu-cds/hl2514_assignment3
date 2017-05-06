'''
Author: Hao Liu
Date: 5/6/2017
Spark script used for calculate the production of all elements in RDD.
'''

from pyspark import SparkContext
from operator import mul

if __name__ == '__main__':
	sc = SparkContext("local", "product")
	# Create an RDD of numbers from 1 to 1,000
	nums = sc.parallelize(range(1, 1001))
	# The neutral element of multiplication is 1.
	print(nums.fold(1, op=mul))
	sc.stop()
