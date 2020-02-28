import pyspark
from pyspark import SparkContext
from operator import add


sc = SparkContext('local[*]')
f=sc.textFile('file01_Hd_Sp_Freq.txt')

data = f.flatMap(lambda line : line.split()).map(lambda x : (x.strip("(,),.,',*,#,),,,:,*, , ,;,?,/,&,!,%,-,_,+,\",+"),1)).reduceByKey(add).sortBy(lambda x : x[1],ascending=False).take(3)

for (word, count) in data:
    print("{}: {}".format(word, count))