import pyspark
import random
from pyspark import SparkContext
from operator import add

def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1

NUM_SAMPLES=10000
sc = SparkContext('local[*]')
count = sc.parallelize(range(0, NUM_SAMPLES)).filter(inside).count()
est_pi=4.0 * count / NUM_SAMPLES
print("Pi is roughly {}".format(est_pi))