# from pyzolib import pyximport
# pyximport.install()
# import c1
import pyximport
pyximport.install(setup_args={"script_args":["--compiler=mingw32"]}, reload_support=True)
import timeit  

lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826
num = 500000



t = timeit.Timer("c1.great_circle(%f,%f,%f,%f)" % (lon1,lat1,lon2,lat2), 
                     "import c1")
print "Cython function (still using python math)", t.timeit(num), "sec"