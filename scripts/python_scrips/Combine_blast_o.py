#!/usr/bin/python
__author__= 'Pedro J. Torres'
import argparse
import os

"Script will sum up your blast output into an otu style format"

#---------- Split to count the number of hits given by a blast output and make an OTU style format------
parser=argparse.ArgumentParser(description="Script will sum up your blast text output into an otu style format. For this script to work output you must output your blastn data like this '-outfmt 6 stitle'. Also make sure all your blast outputs you want to summarize are in their own directory")
parser.add_argument('-d','--dir', help='All blast.txt files should be in one directory. Add directory here or leave blank for current working firectory', required=False)
parser.add_argument('-o','--out', help='Name of summary ouput text file', required=True)#require later
args=parser.parse_args()
directory_i=str(args.dir)
o_file=str(args.out)

# check to see if you input you input the directory where files are kept
if args.dir is None:
    directory=str(os.getcwd())
    directory=directory+"/"
else:
    cwd=str(os.getcwd())
    cwd=cwd+"/"
    directory=cwd+directory_i

#-----------------Make dictionary and call each txt file in directory-------------------------------
"""make dictionary to keep count of blast outputs. Keys are going to be taxa name and a list will keep track of the abundance for each file"""
taxa={}
# All txt files (should be blast output txt files) in current directory are added to a list 'F'
F=[i for i in os.listdir(directory) if i.split(".")[-1]=="txt"]
print ("You are combining " +str(len(F))+" text Files")

#------------Call and open each txt file in directory and start reading each line which should be taxonomy/gene name---------
for txt in F:
    f=open(txt,"r")
    for line in f:
        line=line.strip()
        line=line.split("|")# split based on this character and add them individually to a list
        taxName=line[-1]# get name of Taxa this can be changed if you want GI numbers or something else isntead

        """Add taxa/gene as key in dictionary and its value is a list in which each element represents taxa/gene count for each file.Checks to see if Taxa is already in the dictionary, if not, it will add it and and start to makes a list with a zero to keep count each time it sees that taxa it will add 1."""
        if taxName not in taxa:
            taxa[taxName]=[0]*len(F)# Make a list for to keep the Taxa abundace for each file in directory or length of F.
        else:pass
        taxa[taxName][F.index(txt)]+=1
print "There are a total of " +str(len(taxa)) +" taxa"

"""Above it does two things. First it will be calling the values to the Key 'taxName'. But because there are a list of counters (one for each file) we need to tell it which one. By indexing all the files in 'txt' you keep everything in order, call the right list index and add 1 each time you see that taxaName in that particular file."""

#-----------------Create new output file and write in abundance
o=open(o_file,"w+")
o.write("Taxa\t"+"\t".join(F)+"\n")
for i in taxa:
    o.write(i+"\t"+"\t".join([str(xx) for xx in taxa[i]])+"\n")
o.close()

print "Done :)"
