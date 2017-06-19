#!/usr/bin/python
__author__ = 'Pedro J. Torres'
import os
import sys, getopt
import argparse

'''This script is used to split kraken-mpa formatted  output into files based on taxonomic rank'''

#------------Use the command line to take in arguments--------------------------
parser = argparse.ArgumentParser(description='This is a script to parse out a  kraken-mpa-report formated file based on taxonomic rank.')
parser.add_argument('-i','--input', help='Input file name aka the output file from running kraken-mpa on multiple datasets',required=True)
parser.add_argument('-o','--output',help='Output directory name.', required=False)
args = parser.parse_args()
inputfile= str(args.input) 

#--------Create new directory for file output-----------------------------------
path=str(args.output) 
if not os.path.exists(path):
    os.makedirs(path)


#------- The path and names of files that will appear in new output directory--
k = os.path.join(path, "L1_kingdom"+".txt")
p = os.path.join(path, "L2_phylum"+".txt")
c = os.path.join(path, "L3_class"+".txt")
o = os.path.join(path, "L4_order"+".txt")
f = os.path.join(path, "L5_family"+".txt")
g = os.path.join(path, "L6_genus"+".txt")
s = os.path.join(path, "L7_species"+".txt")

#------- open inputfile and new output files-----------------------------------
fin=open(inputfile,'r')
header=fin.readline()# this will write out the first line of the file aka header.
'''will open a file for each taxonomic level and write the header'''
fout_k=open(k,"w")
fout_k.write(header)
fout_p=open(p,"w")
fout_p.write(header)
fout_c=open(c,"w")
fout_c.write(header)
fout_o=open(o,"w")
fout_o.write(header)
fout_f=open(f,"w")
fout_f.write(header)
fout_g=open(g,"w")
fout_g.write(header)
fout_s=open(s,"w")
fout_s.write(header)

#-----------Split file based on taxonomic rank-----------------------------------
'''Following Split function will create a list seperated by '|' (this is how different
taxonomic levels are seperated in kraken.  This way the length of the list will be dictated
by how many taxonomic levels the current line contains (i.e., len(kingdom)==1, len(phylum)==2,
len(class)==3 ..ect)'''
for line in fin:
    split=line.split('|')
    ln_split=len(split)      
    if ln_split==1:#Kingdom
        fout_k.write(line)
    elif ln_split==2:#Phylum
        fout_p.write(line)
    elif ln_split==3:#Class
        fout_c.write(line)
    elif ln_split==4:#Order
        fout_o.write(line)
    elif ln_split==5:#Family
        fout_f.write(line)
    elif ln_split==6:#Genus
        fout_g.write(line)
    elif ln_split==7:#Species
        fout_s.write(line)
            
fout_k.close()
fout_p.close()
fout_c.close()
fout_o.close()
fout_f.close()
fout_g.close()
fout_s.close()     
fin.close()
