import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

years = [2010,2011,2012,2013,2014,2015,2016,2017,2018]
count = [11,  15,  21,  47,  76,  116, 140, 134, 67]
total = [11,  26,  47,  94,  170, 286, 426, 560, 627]

data = [count,total]

plt.bar(years,count,color="#FF8888")

ynew = np.linspace(2010,2018,300)
smooth = spline(years,total,ynew)
plt.plot(ynew,smooth)
#plt.plot(years,total)

plt.gca().yaxis.grid(True)

rows = ["Publications","Cumulative"]

table = plt.table(cellText=data,rowLabels=rows,colLabels=years,loc="bottom")

plt.tick_params(axis="x",which="both",bottom=False,top=False,labelbottom=False)
plt.ylabel("Peer-Reviewed Publications")
plt.legend()
plt.savefig("TCIAGraph.png",bbox_inches="tight")
