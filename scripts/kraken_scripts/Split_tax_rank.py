#!/usr/bin/python
__author__ = 'Pedro J. Torres'
import os
import sys, getopt
import argparse

'''This script is used to split kraken-mpa formatted  output into files based on taxonomy rank'''
parser = argparse.ArgumentParser(description='This is a script to parse out a kraken-mpa formated file based on taxonomic rank.')
parser.add_argument('-i','--input', help='Input file name aka the output from running kraken-mpa',required=True)
parser.add_argument('-o','--output',help='Output directory name.', required=False)
args = parser.parse_args()
inputfile= str(args.input)

#--------Create new directory for file output-----
path=str(args.output) #'Split_kraken_o'
if not os.path.exists(path):
    os.makedirs(path)

'''write names of files that will appear in new directory'''
k = os.path.join(path, "L1_kingdom"+".txt")
p = os.path.join(path, "L2_phylum"+".txt")
c = os.path.join(path, "L3_class"+".txt")
o = os.path.join(path, "L4_order"+".txt")
f = os.path.join(path, "L5_family"+".txt")
g = os.path.join(path, "L6_genus"+".txt")
s = os.path.join(path, "L7_species"+".txt")

#-----read the file and open new text-------
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

#-------------------------------------------------------------------------------
'''Followign Split function will create a list seperated by '|' (this is how different
taxonomic levels are seperated in kraken.  This way the length of the list will be dictitated
by how many taxonomic levels the current line contains (i.e., len(kingdom)==1, len(phylum)==2,
len(class)==3 ..ect)'''
for line in fin:
    sep_line=line.split('\t')# seperate based on tab in txt file
    domain=sep_line[0].split('|')
    rank=domain[-1].split("__")
        
    if rank[0]=='k':#Kingdom
        fout_k.write(line)
    elif rank[0]=='p':#Phylum
        fout_p.write(line)
    elif rank[0]=='c':#Class
        fout_c.write(line)
    elif rank[0]=='o':#Order
        fout_o.write(line)
    elif rank[0]=='f':#Family
        fout_f.write(line)
    elif rank[0]=='g':#Genus
        fout_g.write(line)
    elif rank[0]=='s':#Species
        fout_s.write(line)
            
fout_k.close()
fout_p.close()
fout_c.close()
fout_o.close()
fout_f.close()
fout_g.close()
fout_s.close()     
fin.close()
