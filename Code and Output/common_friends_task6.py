import pyspark
from pyspark import SparkContext
from operator import add
#from operator import union

sc = SparkContext('local[*]')
f=sc.textFile('cf.txt')

data=f.map(lambda x : x.split('-'))

m=data.cartesian(data).filter(lambda x : x[0][0]!=x[1][0]).map(lambda x : ([x[0][0],x[1][0]],[set(x[1][1]) & set(x[0][1])])).collect()

for x in m:
    print(x)

