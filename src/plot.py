import numpy as np
import matplotlib.pyplot as plt
import codecs
import math
import sys

file_estimate='files/estimate.txt'
file_count='files/counts.txt'
file_stream='files/words_stream.txt'
max_id=1407593
estimate={}
count={}

t=0;
infile=codecs.open(file_stream , 'r' , encoding='utf-8' )
for line in infile :
    t+=1


infile=codecs.open(file_estimate , 'r' , encoding='utf-8' )
for line in infile :
    line=line.split('\t')
    estimate[int(line[0])]=int(line[1])
    
infile=codecs.open(file_count , 'r' , encoding='utf-8' )
for line in infile :
    line=line.split('\t')
    count[int(line[0])]=int(line[1])
    
y=[]
x=[]
for i in range(max_id):
    j=i+1
    es=estimate[j]
    cn=count[j]
    #y.append(math.log10((es-cn)/cn))
    #x.append(math.log10(cn/max_id))
    y.append((es-cn)/cn)
    x.append(cn/t)

fig, ax = plt.subplots()
plt.ylabel('relative error')
plt.xlabel('word frequency')
ax.plot(x,y,'ro')
ax.set_xscale('log')
ax.set_yscale('log')

plt.show()