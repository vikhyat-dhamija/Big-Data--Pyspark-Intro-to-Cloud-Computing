import pyspark
from pyspark import SparkContext
from operator import add
sc = SparkContext('local[*]')
f=sc.textFile('file01_Hd_Sp_Freq.txt')
data = f.flatMap(lambda line : line.split()).map(lambda x : (x.strip("(,),.,',*,#,),,,:,*, , ,;,?,/,&,!,%,-,_,+,\",+"),1)).reduceByKey(add)
data.saveAsTextFile("wc_out.txt")