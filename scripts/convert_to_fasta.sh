#!/bin/bash
#$ -cwd

# script allows for multiple fastq files to be converted to fasta. Done on clsuter. Will need to add the names of all file you want to 
# convert into fasta into a new txt file here named 'fastq_files.txt'. Thenn submit in qsub -t 1-#:1 

FILE=$(head -n $SGE_TASK_ID fastq_files.txt | tail -n 1)


cat $FILE | perl -e '$i=0;while(<>){if(/^@/&&$i==0){s/^@/>/;print;}elsif($i==1){print;$i=-3}$i++;}' > ${FILE%}.fasta
