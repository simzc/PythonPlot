# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""##
#  marker   '+' '.'  'o'  's'  '<' '>' '^' 'v'  
#  linestyle ':'  '-.'  '--' '-'
#  color     'black'  'red' 'blue' 'lime' 'cyan' 'orange'
###  
import matplotlib.pyplot as plt
import numpy as np
        
        
glob_markersize=10
da=np.loadtxt(r"experiment.dat")
inp=np.loadtxt(r"probe Rie 2.dat")  


inp[:,0]*=np.sqrt(9.8)
inp[:,1]=(inp[:,1]-400.)/1000./9.8/1.


fig,ax=plt.subplots(figsize=(6.5,5))

ax.plot(inp[:,0],inp[:,1],linestyle="-",marker=".",markersize=1.,color="b",label="TF-SPH")


# ax.plot(inp1[:,0],inp1[:,1],linestyle="-",marker=".",markersize=1,color="r",label="delta")
# ax.plot(inp2[:,0],inp2[:,1],linestyle="",marker=".",markersize=0.5,color="orange",label="mix")

ax.plot(da[:,0],da[:,1],linestyle="",marker="^",markersize=8,color="k",label="experiment")
# ax.plot(inp1[:,0],inp1[:,1],linewidth=2.0,color="red",\
#         markersize=glob_markersize,label=r"TF-SPH")
# ax.plot(inp1[:,0],inp1[:,2],linewidth=2.0,color="red",\
#             markersize=glob_markersize)
    
# ax.plot(inp2[:,0],inp2[:,1],linewidth=2.0,color="orange",\
#         markersize=glob_markersize,label=r"TF-SPH $k^*=\frac{k_i+k_j}{2}$")
# ax.plot(inp2[:,0],inp2[:,2],linewidth=2.0,color="orange",\
#         markersize=glob_markersize)


# ax.plot(inp1[:,0],inp1[:,1],"k.",label="TF-SPH111")

ax.set_xlabel("t*",fontfamily="Times New Roman",fontsize=18)
ax.set_ylabel("p*",fontfamily="Times New Roman",fontsize=18)

ax.tick_params(axis='both',length=4,width=2,direction="in")
plt.xticks(fontfamily="Times New Roman", fontsize=18)
plt.yticks(fontfamily="Times New Roman", fontsize=18)


# ax.set_xlim([0,2.1])
# ax.set_ylim([])

# ax.legend(prop={"family":"Times New Roman", "size":18},\
#           frameon=True,edgecolor='k',bbox_to_anchor=(0.42,0.6))
ax.legend(prop={"family":"Times New Roman", "size":18},\
          frameon=True,edgecolor='k')

bwidth=2
ax.spines[['top','bottom','left','right']].set_linewidth(bwidth)


fig.subplots_adjust(left=0.14,right=0.95,top=0.95,bottom=0.15) ##调节图尺寸位置
# plt.text(0.374,381,"P2",fontfamily="Times New Roman",fontsize=20)
# plt.text(0.786,394,"P1",fontfamily="Times New Roman",fontsize=20)
# plt.text(0.58,333,"P3",fontfamily="Times New Roman",fontsize=20)
# plt.savefig(./)


