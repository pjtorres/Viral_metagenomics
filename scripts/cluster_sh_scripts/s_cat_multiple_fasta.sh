#!/bin/bash
#$ -cwd

# After splitting all fasta files using 's_split_fasta.sh' and then removing contamination using 'deconseq_multithred.sh' you will
#have 9 diff fasta files per sample and then you will want to merge these 9 files per sample. Use this code. 
# Example file names in file.txt : file1_prinseq_good_1.fastq.fasta_c

FILE=$(head -n $SGE_TASK_ID file.txt | tail -n 1)
FOUT=$(echo $FILE | cut -c1-28) # this may be subject to cange depending on file name and character size

cat $FILE*.fasta_clean.fa >> ${FOUT%}_clean_all.fasta
