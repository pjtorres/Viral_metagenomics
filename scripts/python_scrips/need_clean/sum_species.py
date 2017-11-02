__author__= 'Pedro J. Torres'
import argparse
import os

fin=open('/Volumes/Transcend/AJ_Virus/Blast_o_virus_9_2017/trytocombine/new.txt' , 'r')
total={}
header=fin.readline()# header here

for line in fin:
    lines=line.split('\t')
    taxName=lines[-1].strip()# this will remove the 'serotype' part of the taxa name
    taxName=taxName.rsplit(' ', 1)
    taxName = taxName[0]
    lines=lines[:-1]
    lines=map(int,lines) #makes strings in list into intergers
    for i in range(len(lines)):
        if taxName not in total:
            total[taxName]=[0]*len(lines) #setting up the inital list
        else:pass
        total[taxName][i] += lines[i]
            
print " There are a total of " + str(len(total)) + " taxa!"
             
#-------------Create new output file and write abindance in
o=open("out.txt","w+") # WE WILL CHANGE THE NAME OF THIS AS WE AUTOMATE IT
o.write(header)
for i in total:
    o.write("\t".join([str(xx) for xx in total[i]])+"\t"+ i+'\n')
o.close()
