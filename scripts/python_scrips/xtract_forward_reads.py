__author__= 'Pedro J. Torres'
import argparse

'''Script allows you to extract the forward reads that did not merge in the bbmerge. AKA from you unmerged file'''

#----------------Command Line Arguments-------------
parser=argparse.ArgumentParser(description="Script allows you to extract the fowards reads that did not merge in the bbmerge. AKA from you runmerged file. Exmple use: python xtract_foward_reads.py -i SampleA_unmerged.fa -o SampleA")
parser.add_argument('-i','--input', help='Input unmerged fasta file in which you want to extract the foward reads that did not match in you rmatching program aka bbmerge, pandas,pear',required=True)
parser.add_argument('-o','--output',help='New output file namecontaining only foward reads', required=True)
args = parser.parse_args()
fastafile=str(args.input) #name of the unmerged fasta file
outputfile=str(args.output) # name of output file with new header

# ----------------- Command will convert your fasta file into a dictionary with fasta header as key and fasta sequence as value------
print 'Starting Process...'
infile=fastafile
fin=open(infile,'r')
fasta={}
for line in fin:
    line=line.strip()
    if line.startswith('>'):
        header = line.strip()
       # print header
        fasta[header]=""
        fastaseq=''# as long as the > character is not seen you will continue to build on this string
    else:
        fastaseq+=line.strip('\n').strip('\t').strip()# continue to add strings to your variable fastaseq until it sees the > character and is restarted with an empty string from above loop
        fasta[header]=fastaseq
        
#------------ Make new file containing only R1 or foward reads from your unmerged file---------------
out=outputfile
fout=open(outputfile+'_unmerged_R1_reads.fa','w+')       
for i in fasta.keys():
    if '1:N' in i:# search for this particular pattern as this '1:N' tells you that you are dealing with a forward read '2:N' would be reverse reads, but i on't care about these right now
        fout.write(i+'\n'+"".join(x for x in fasta[i])+'\n')
fout.close()

print 'Done :)'
