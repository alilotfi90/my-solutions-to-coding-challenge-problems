#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  temp2.py
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
#   Check if a number is a perfect square
#  
import math
def is_square(n):    
    if n>=0 and int(math.sqrt(n))**2==n:
        return True
    else:
        return False
def main(args):
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
