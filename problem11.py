import pyperclip
import time
import math
import re
import urllib2
import string

def get_matrix(url):
  Matrix = [[0 for x in xrange(20)] for x in xrange(20)]
  response = urllib2.urlopen(url)
  html = response.read()
  m = re.findall('^(.*?)<br\s/>',html,re.MULTILINE)
  list = []
  for i in m[:-2]:
    i = string.replace(i,'<span style="color:#ff0000;"><b>','')
    i = string.replace(i,'</b></span>','')
    list.append(i)
  for i in list:
    Matrix[list.index(i)] = i.split()
  return Matrix

def max_product(n):
  Matrix = get_matrix('http://projecteuler.net/problem=11')
  product_list=[]
  for i in range(20):
    for j in range(20-n):
      product1 = 1
      product2 = 1
      product3 = 1
      product4 = 1
      for k in range(n):
        product1 *= int(Matrix[j+k][i])
        product2 *= int(Matrix[i][j+k])
        product3 *= int(Matrix[j+k][j+k])
        product4 *= int(Matrix[k-j][k-j])
      product_list.extend((product1,product2,product3,product4))
      
  product_list.sort()
  print product_list
  return product_list[-1]
 
print max_product(4)
pyperclip.copy(max_product(4))


# start = time.time()
# answer = max_product(4)
# elapsed = (time.time()-start)

# print "found %s in %s seconds" % (answer,elapsed)
# pyperclip.copy(answer)