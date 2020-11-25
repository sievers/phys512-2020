#we can generate timing from the command line via 
#  python3 -m cProfile -o simple_hist_timing.dat simple_hist_2d.py

import pstats
from pstats import SortKey
p=pstats.Stats('simple_hist_timing.dat')
#this prints out ALL the function calls that went on
#p.strip_dirs().sort_stats(-1).print_stats()  
p.sort_stats(SortKey.TIME).print_stats(10)
