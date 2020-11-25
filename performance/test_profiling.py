import cProfile
import re

#python3 -m cProfile -o restats.prof simple_hist_2d.py from command line will work

#cProfile.run('python3 simple_hist_2d.py')
cProfile.run('re.compile("simple_hist_2d.py")','simple_hist_timing.dat')
