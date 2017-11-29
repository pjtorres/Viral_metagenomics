__author__= 'Pedro J. Torres'
# get full taxonomic names for this dataset
import argparse
import os
from Bio import Entrez
from Bio import SeqIO
import urllib

"""If you have an OTU style file made from your blast output but your 'OTUs' are accesion numbers and you want taxonomic rank you can run this script. USED FOR JORGEN. For now you must chanfe the name of the fin2 file - which will be your taxonomic output- and change the output file name. Will fix later. Also, right now any Accesion number not found in Biopython gets printed, need to fix it so that those that aren;t in the accesion file just stay as accesion numbers and are not just removed."""
#--------Get information from accesion number-------
print ("Processing... Might take a while so take a walk, grab a beer or aimlessly wander the internet")
Entrez.email = '##############'
lineage_info={} #will keep info on accesion numbers and lineage for later use when makng new header

print ("Making new fasta file now......")
fin2=open('/Volumes/Transcend/Jorgen/blast_rob/conbined_blast.txt','r')
fout=open('taxName_blast_otry3.txt','w+')
header = fin2.readline()
fout.write(header)

for line in fin2:
    line=line.strip()
    line=line.split('\t')
    acc_num=line[0].strip()
    newline=line[1:]
    lines=line[1:]
    lines=map(int,lines)


    #newline=map(int,newline)
    #print (line)
    try:
        handle = Entrez.efetch(db='nucleotide', id=str(acc_num), rettype="gb", retmode="text")
        x = SeqIO.read(handle, 'genbank')# get information regarding your accesion number in here will be taxonomy
        tax=x.annotations['taxonomy']# only get taxonomy
        #org=x.annotations['organism']
        #new=tax.append(org)
        taxf=";".join(tax)#join taxonomy based on ';' character
        full_lineage=(taxf+';'+x.annotations['organism']) # but i also want the organism name so this will also add organism specific name
        #print (newline)
        for i in range(len(newline)):
            if full_lineage not in lineage_info:
                lineage_info[full_lineage]=[0]*len(newline)
            else:pass
          #  print(full_lineage)
            lineage_info[full_lineage][i] += int(newline[i])



    except urllib.error.HTTPError: # the exception  is here in case your accesion number is not found in entrez the script will not fail
        acc_num=acc_num.strip()
        lineage_info[acc_num]=acc_num
        print(acc_num)


        continue     
    #else:
     #   fout.write(line)
print("You have "+ str(len(lineage_info))+' accesion numbers')  
for i in lineage_info:
    print(i)
    fout.write(i+"\t"+"\t".join([str(xx) for xx in lineage_info[i]])+'\n')

fin2.close()
fout.close()

print ('Done')
