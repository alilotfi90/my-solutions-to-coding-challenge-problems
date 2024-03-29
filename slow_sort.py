#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  slow_sort.py
#  
#  Copyright 2021 Ali Lotfi <ali@ali-Oryx-Pro>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.s
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import numpy as np
def slow(lis):
	for i in range(len(lis)):
		for j in range(i,len(lis)):
			if lis[i]<lis[j]:
				x=lis[j]
				lis[j]=lis[i]
				lis[i]=x
	return lis
def quick(lis1,left,right):
	piv=lis1[(left+right)//2]
	while lis1[left]<piv:
		left=left+1
	while lis1[right]>piv:
		right=right-1	
				
def main(args):
	lis=[1,5,4,3,6,1]
	#print(slow(lis))
	print(slow(lis))
	a={'name':'ali','grade':'A'}
	a.update({'name':'hi'})
	print(a)
	a.update({'grade':'B'})
	print(a)
	quick(lis,0,len(lis))
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
