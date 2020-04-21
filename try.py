from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("word count").setMaster("local[3]")
sc = SparkContext(conf=conf)							# this is the main entry point to the spark functionality
# 														# "word count" - the app name
# 														# "local[3]" - run locally using 3 cores of our cpu
# 														# local[2] - 2 cores; local[*] - all available cores; local - 1 core;
# # lines = sc.textFile("ML\\data\\my_data.csv")				# the file loaded as a RDD (resilient dristibuted dataset)
# rdd = sc.parallelize(range(1, 7))						# Create a RDD
# result = lines.collect()								# Return a list that contains all of the elements in this RDD.
# result = lines.first()									# Return the first element in this RDD.
# result = lines.take(num)								# Take the first num elements of the RDD.
# result = lines.count()									# Return the number of elements in this RDD.
# result = lines.distinct().collect()						# Return a new RDD containing the distinct elements in this RDD.
# result = lines.filter(lambda x: x % 2 == 0).collect()	# Return a new RDD containing only the elements that satisfy a predicate.
# result = lines.flatMap(lambda x: range(1, x)).collect()# Return a new RDD by first applying a function to all elements of this RDD, and then flattening the results.