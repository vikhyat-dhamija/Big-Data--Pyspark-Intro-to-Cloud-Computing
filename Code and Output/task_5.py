import pyspark
from pyspark import SparkContext
from operator import add


sc = SparkContext('local[*]')
f=sc.textFile('practice.txt')

lines_i=f.filter(lambda x : (x[0]=='I' ))
lines_2=lines_i.collect()

count1=lines_i.map(lambda x: x.split('\t')).map(lambda x: x[0]).filter(lambda x : "Spark" in x).count()

count2=lines_i.flatMap(lambda x: x.split('\t')).filter(lambda x : "Spark" in x).count()

count3=lines_i.flatMap(lambda x: x.split(' ')).filter(lambda x : "Spark" in x).count()

print("The number of lines starting with 'I' and containing the word 'Spark' is: ",count1)
print("The number of lines starting with 'I' and containing the word 'Spark' using FlatMap is: ",count2)
print("The count of 'Spark' in the lines starting with 'I': ",count3)

