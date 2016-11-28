import numpy as np
import matplotlib.pyplot as plt
import codecs
import math
import sys


def hash(a,b,p,n_bucket,x):
    y = x % p
    hash_val= (a*y+b) % p
    return hash_val % n_bucket

p=123457
delta=pow(math.e, -5)
epsilon=math.e*pow(10, -4)
n_bucket=pow(10, 4)
max_id=1407593
file_word_stream='files/words_stream.txt'
file_para='files/hash_params.txt'
F_={}
a=[]
b=[]
C={}
#load parameters of hash functions
infile=codecs.open(file_para , 'r' , encoding='utf-8' )
for line in infile :
    line=line.split('\t')
    a.append(int(line[0]))
    b.append(int(line[1]))


infile=codecs.open(file_word_stream , 'r' , encoding='utf-8' )
for line in infile :
    x=int(line)
    for j in range(len(a)):
        hash_val=hash(a[j], b[j], p, n_bucket, x)
        s='_'
        seq=[]
        seq.append(str(j))
        seq.append(str(hash_val))
        key=s.join(seq)
        if key in C:
            C[key]+=1
        else:
            C[key]=1

outfile=codecs.open('files/estimate.txt' , 'w' , encoding='utf-8' )
for i in range(max_id):
    j=i+1
    min=sys.maxsize
    for k in range(len(a)):
        hash_val=hash(a[k], b[k], p, n_bucket, j)
        s='_'
        seq=[]
        seq.append(str(k))
        seq.append(str(hash_val))
        key=s.join(seq)        
        val=C[key]
        if val < min:
            min=val
    outfile.write(str(j)+'\t'+str(min)+'\r\n')
outfile.close()   
        