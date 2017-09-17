__author__= 'Pedro J. Torres'
import argparse
import os
from Bio import Entrez
from Bio import SeqIO

"""Script allows changing the headers of fa files downloaded and concatinated from NCBI ref seq. After this script
headers should include nucleotide Accesion number followed by full taxonomic lineage as well as species specificity"""

#-----------Command Line Arguments-----------------
parser=argparse.ArgumentParser(description="This script uses python3 and Biopython. Make sure both are installed. Script will change fasta header from NCBI refseq.fa files to include both accesion numbers and taxonomic lineage. You will also need a text file with accesion numbers in it. This is how you can make one using the ref seq files downloaded from NCBI: sed 's/\s.*$//' viral_all.fna | grep > | sed 's/>//' > Viral_accesion_numbers.txt")
parser.add_argument('-a','--acc', help=' Input file containing accesion numbers -aka Viral_accesion_numbers.txt . Look at desciption to see how',required=True)
parser.add_argument('-i','--input', help=' Input fasta file you want to change',required=True)
parser.add_argument('-o','--output',help='New output file name. Example: Viral_new_header.fa', required=False)
args = parser.parse_args()
accfile=str(args.acc) #name of accesion file
fastafile=str(args.input) #name of fasta file want to change
outputfile=str(args.output) # name of output file with new header

#--------Get information from accesion number-------
print ("Processing... Might take a while so take a walk, grab a beer or aimlessly wander the internet")
Entrez.email = '##############'
# open my file and parse it
#accfile="short_list_accesion.txt"
fin1=open(accfile,'r')
lineage_info={} # will keep info on accesion numbers and lineage for later use when makng new header

for line in fin1:
    handle = Entrez.efetch(db="nucleotide", id=str(line), rettype="gb", retmode="text")
    x = SeqIO.read(handle, 'genbank')# get information regarding your accesion number in here will be taxonomy
    tax=x.annotations['taxonomy']# only get taxonomy
    taxf=";".join(tax)#join taxonomy based on ';' character
    full_lineage=(taxf+';'+x.annotations['organism']) # but i also want the organism name so this will also add organism specific name
    #print (line + '\t'+full_lineage)
    line=line.strip()
    lineage_info[line]=full_lineage
    #print (lineage_info)
print("You have "+ str(len(lineage_info))+' accesion numbers')   

"""now open the fasta file containing the headers you want to change. This is going to be done on my viral db which 
was downloaded from ftp://ftp.ncbi.nlm.nih.gov/refseq/release/viral/ . This downloaded dataset contains fasta files and 
header is AccesionNumber and Organism name. I want to change it to AccesionNumber and Taxonomic lineage. You can remove
the accesion number and add to a new file using the following commands:

sed 's/\s.*$//' viral_all.fna | grep ">" | sed 's/>//' > Viral_accesion_numbers.txt

"""
#-------Take in fasta file you want to change output new fasta file in which header includes full taxonomic lineage.
print ("Making new fasta file now......")
fin2=open(fastafile,'r')
fout=open(outputfile,'w+')
for line in fin2:
    if line.startswith('>'):
        acc_num=line[1:12]
        new_header=('>'+'ref|'+acc_num+'|'+' '+lineage_info[acc_num]+'\n') #changed the header more to work with my combined_blast_o.py script
        #print (new_header)
        fout.write(new_header)      
    else:
        #print (line)
        fout.write(line)
        
fin2.close()
fin1.close()
fout.close()
#return 

print ('Done :)')
