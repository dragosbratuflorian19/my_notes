from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("word count").setMaster("local")
sc = SparkContext(conf=conf)
rdd = sc.parallelize(range(1, 7))