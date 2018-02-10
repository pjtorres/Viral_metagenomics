#!/usr/bin/python
__author__= 'Pedro J. Torres'
import argparse
import os
import pandas
import pandas as pd
"Script will sum up your Diamond output into an otu style format"

#---------- Split to count the number of hits given by a blast output and make an OTU style format------
parser=argparse.ArgumentParser(description="Script will sum up your blast text output into an otu style format. For this script to work output you must output your blastn data like this '-outfmt 6 stitle'. Also make sure all your blast outputs you want to summarize are in their own directory")
parser.add_argument('-d','--dir', help='All blast.txt files should be in one directory. Add directory here or leave blank for current working firectory', required=False)
parser.add_argument('-o','--out', help='Name of summary ouput text file', required=True)#require later
parser.add_argument('-o_ra','--outra', help='Name of summary ouput text file with relative gene abundance', required=True)#require later

args=parser.parse_args()
directory_i=str(args.dir)
o_file=str(args.out)
relative_abun=str(args.outra)

# check to see if you input you input the directory where files are kept
if args.dir is None:
    cwd=str(os.getcwd())
    directory=cwd+"/"
else:
    cwd=str(os.getcwd())
    cwd=cwd+"/"
    directory=cwd+directory_i

#-----------------Make dictionary and call each txt file in directory-------------------------------
"""make dictionary to keep count of DIAMOND outputs. Keys are going to be taxa name and a list will keep track of the abundance for each file"""
taxa={}
# All txt files (should be blast output txt files) in current directory are added to a list 'F'
F=[directory+i for i in os.listdir(directory) if i.split(".")[-1]=="txt"]
header=[i for i in os.listdir(directory) if i.split(".")[-1]=="txt"]
print ("You are combining " +str(len(F))+" text Files")
#------------Call and open each txt file in directory and start reading each line which should be taxonomy/gene name---------
for txt in  F:
    f=open(txt,"r")
    for line in f:
        line=line.strip()
        line=line.split('   ')# split based on this character and add them individually to a list
        line=line[1:]
        line=" ".join(line)
        line=line.split()
        taxName=" ".join(line[0:])# get name of Taxa this can be changed if you want GI numbers or something else isntead
        """Add taxa/gene as key in dictionary and its value is a list in which each element represents taxa/gene count for each file.Checks to see if Taxa is already in the dictionary, if not, it will add it and and start to makes a list with a zero to keep count each time it sees that taxa it will add 1."""
        if taxName not in taxa:
            taxa[taxName]=[0]*len(F)# Make a list for to keep the Taxa abundace for each file in directory or length of F.
        else:pass
        taxa[taxName][F.index(txt)]+=1
print ("There are a total of " +str(len(taxa)) +"  genes")

#-----------------Create new output file and write in abundance
o=open(o_file+'.txt',"w+")
o.write("Gene\t"+"Bacteria\t"+"\t".join(header)+"\n")
for i in taxa:
    Gene,bacteria=i.split('[')
    o.write(Gene + '\t'+ '['+bacteria+"\t"+"\t".join([str(xx) for xx in taxa[i]])+"\n")
o.close()
df=pandas.read_table(o_file+'.txt')
os.remove(o_file+'.txt')
df.to_csv(o_file+'.csv',index=False)
#--------This part will also make a file to use in Pandas and get relative abundance
### Make a temporary file for use in PANDAS
tmp=open('tmp.txt',"w+")
tmp.write("Gene "+"Bacteria\t"+"\t".join(header)+"\n")
for i in taxa:
    tmp.write(i+"\t"+"\t".join([str(xx) for xx in taxa[i]])+"\n")
tmp.close()

#---Start working with pandas to make relative abundance-------
print ("Retrieving relative abundance")
df=pandas.read_table('tmp.txt')
cols = [c for c in df.columns ] # get column names
df=df[cols]# convert columns to dataframe

#--------------- Convert raw counts to percentages -------
dft=(df.set_index('Gene Bacteria').T)
cols= df['Gene Bacteria'].tolist()
dft[cols] = dft[cols].div(dft[cols].sum(axis=1), axis=0)# you would *100 here if you want percent abdundance
dft=dft.transpose()
dft.to_csv('tmp2'+'.csv')#new tmp file
os.remove("tmp.txt")# remove old temp file from before

#----------------Work with new file, this was the only way i was able to manupulate my dataframe
df = pandas.DataFrame.from_csv('tmp2.csv', index_col=None)
dft=df['Gene Bacteria'].str.split('[',1, expand=True).rename(columns={0:'Gene', 1:'Bacteria'})# split my single column of Gene Bacteria back into two different files
df= df.drop(['Gene Bacteria'], axis=1)
final =pd.concat([dft,df], axis=1)
os.remove("tmp2.csv")
final.to_csv(relative_abun+'.csv',index=False)

print ('DONE :)')
