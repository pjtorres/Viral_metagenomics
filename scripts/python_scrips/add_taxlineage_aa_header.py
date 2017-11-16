__author__= 'Pedro J. Torres'
import argparse
import os
from Bio import Entrez
from Bio import SeqIO
import urllib

"""Script allows changing the headers of fa files downloaded and concatinated from NCBI ref seq. After this script
headers should include PROTEIN Accesion number followed by full taxonomic lineage as well as species specificity. Output will be in a new fasta file. Example fasta header for this script to work:
>CY153704
ATGAATATAAATCCTTATTTTCTCTTCATAGATGTGCCCGTACAGGCAGCAATTTCAACAACATTCCCATACACTGGTGTTCCCCCTTATTCTCATGGAACAGGAACAGGCTACACAATAGACACCGTGATCAGAA
"""

#-----------Command Line Arguments-----------------
parser=argparse.ArgumentParser(description="This script uses python3 and Biopython. Make sure both are installed. Script will change fasta header from NCBI refseq.fa files to include both accesion numbers and taxonomic lineage.)
parser.add_argument('-i','--input', help=' Input fasta file you want to change',required=True)
parser.add_argument('-db','--database', help='Input the type of database your fasta file requires e.g., nucleotide or protein',required=True)
parser.add_argument('-o','--output',help='New output file name. Example: Viral_new_header.fa', required=True)
args = parser.parse_args()
fastafile=str(args.input) #name of fasta file want to change
outputfile=str(args.output) # name of output file with new header
database_type=str(args.database) #name of fasta file want to change


#--------Get information from accesion number-------
print ("Processing... Might take a while so take a walk, grab a beer or aimlessly wander the internet")
Entrez.email = '##############'
lineage_info={} #will keep info on accesion numbers and lineage for later use when makng new header

print ("Making new fasta file now......")
fin2=open(fastafile,'r')
fout=open(outputfile,'w+')
for line in fin2:
    if line.startswith('>'):
        acc_num=line[1:]
        try:
            handle = Entrez.efetch(db=database_type, id=str(acc_num), rettype="gb", retmode="text")
            x = SeqIO.read(handle, 'genbank')# get information regarding your accesion number in here will be taxonomy
            tax=x.annotations['taxonomy']# only get taxonomy
            taxf=";".join(tax)#join taxonomy based on ';' character
            full_lineage=(taxf+';'+x.annotations['organism']) # but i also want the organism name so this will also add organism specific name
            acc_num=acc_num.strip()
            lineage_info[acc_num]=full_lineage
            new_header=('>'+'ref|'+acc_num+'|'+' '+lineage_info[acc_num]+'\n') #changed the header more to work with my combined_blast_o.py script
            fout.write(new_header)
        except urllib.error.HTTPError: # the exception  is here in case your accesion number is not found in entrez the script will not fail
            acc_num=acc_num.strip()
            lineage_info[acc_num]=acc_num
            new_header=('>'+'ref|'+acc_num+'|'+' '+lineage_info[acc_num]+'\n') #changed the header more to work with my combined_blast_o.py script
            fout.write(new_header)
            continue     
    else:
        fout.write(line)
#print("You have "+ str(len(lineage_info))+' accesion numbers')           
fin2.close()
fout.close()

print ('Done :)')
