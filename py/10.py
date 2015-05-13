#!/usr/bin/env python
# -*- coding: utf-8 -*-
#       a0 a1  a2   a3       a4
# a = [1, 11, 21, 1211, 111221, 
#１個の１
#２個の１
#１個の２，１個の１
#１個の１，１個の２、２個の１
#３個の１，２個の１，１個の１

from itertools import groupby

# 参考
# http://stackoverflow.com/questions/6972764/python-look-and-say-sequence-improved
def lookandsay(n):
	return ''.join( str(len(list(g))) + k for k, g in groupby(n))

n='1'
print "len(",0,")=" ,len(n)
for i in range(1,31):
	n = lookandsay(n)
	print "len(", i, ")=" ,len(n)

