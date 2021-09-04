# spark context -- this already done for ua
sc

rdd = sc.parallelize(range(1000))

rdd.collect()

rdd.take(5)

rdd.first()

rdd.getNumPartitions()

rdd.count()
rdd.sum()
rdd.max(), rdd.min(), rdd.mean(), rdd.stdev()

rdd.stats()

rdd.histogram(6)

rdd.sample(False, 0.01, 23).collect()

def square(x):
  return x*x

rdd.map(square).take(5)

rdd.map(lambda x: x**2).take(5)

def hundreds_filter(x):
  return x%100 == 0
rdd.filter(hundreds_filter).take(5)

rdd.filter(lambda x: x % 100 == 0).take(5)

rdd2 = rdd.filter(lambda x: x % 150 == 0).map(lambda x:(x**2)/5)

rdd2.take(5)

# RDD with keys:
import random
keyrdd = rdd.map(lambda x: (random.choice(['a','b','c']),x))
keyrdd.take(5)

keyrdd.countByKey()

keyrdd.countByValue()  # Treats full tupple as a key

keyrdd.map(lambda x: x[1]).countByValue() # To count by specific columns

keyrdd.collectAsMap()

keyrdd.groupByKey().mapValues(list).take(3)
keyrdd.groupByKey().mapValues(sum).take(3)

keyrdd.reduceByKey(lambda x, y: x + y).collect()
# Two inputs:
# x is equal to previouse line
# y is the current line

