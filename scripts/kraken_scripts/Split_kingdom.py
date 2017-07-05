#!/usr/bin/python
__author__= 'Pedro J. Torres'
import os
import sys,getopt
import argparse

"This script will split kraken-mpa output based on kingdom in the merged kraken files aka split original file based on wether the abundance
line belings to Bacteria, Virus, Archea, or Eukaryota (Protist and fungi)"
parser=argparse.ArgumentParser(description="Script will split kraken-mpa output based on Bacteria, Virus, Fungi, and Protist")
parser.add_argument('-i','--input', help=' Input file name aka the output from running kraken-mpa',required=True)
parser.add_argument('-o','--output',help='Output directory name.', required=False)
args = parser.parse_args()

inputfile=str(args.input)
                               
#--------Create new directory for file output-----
path=str(args.output) #'Split_kraken_domain'
if not os.path.exists(path):
    os.makedirs(path)

"write names of files that will appear in new directory"
Bacteria=os.path.join(path,"Bacteria"+".txt")
Viruses=os.path.join(path,"Viruses"+".txt")
Archaea=os.path.join(path,"Archaea"+".txt")
Eukaryota=os.path.join(path,"Eukaryota"+".txt")
#-------------open file output from kraken                                                           
fin=open(inputfile, "r+")
header=fin.readline() # header containing sample ids
                               
#----Open all new files which will contain counts for specific domain
fout_b=open(Bacteria,"w")
fout_b.write(header)
fout_v=open(Viruses,"w")
fout_v.write(header)
fout_a=open(Archaea,"w")
fout_a.write(header)
fout_e=open(Eukaryota,"w")
fout_e.write(header)  
#--------read through the file and sperate og file into 4 new files-------                              
for line in fin:
    sep_line=line.split('\t')# seperate based on tab in txt file
    domain=sep_line[0].split('|')# only look at the domain

    if domain[0]=="d__Bacteria":
        fout_b.write(line)
    elif domain[0]=="d__Viruses":
        fout_v.write(line)
    elif domain[0]=="d__Archaea":
        fout_a.write(line)
    elif domain[0]=="d__Eukaryota":
        fout_e.write(line)
                    
fout_b.close()
fout_v.close()
fout_a.close()
fout_e.close()
fin.close()
