import pyspark
from pyspark import SparkContext
from operator import add

sc = SparkContext('local[*]')

f=sc.textFile('task7_input.txt')

data = f.flatMap(lambda line : line.split(' ')).map(lambda x : (x.strip("(,),.,',*,#,),,,:,*, , ,;,?,/,&,!,%,-,_,+,\",+,$,&,1,2,3,4,5,6,7,8,9,0,{,},[,]").upper(),1)).reduceByKey(add)

m= data.map(lambda x : (x[0][:1],x)).sortBy(lambda x: (x[0],x[1][1]), ascending=False).groupByKey().mapValues(list)

n=m.map(lambda a : (a[0],a[1][0:30]) ).collect()

for (word,count) in n :
    print(word,count)


