#!/bin/bash
#$ -cwd

FILE=$(head -n $SGE_TASK_ID file.txt | tail -n 1)

#command
perl samsoft2fasta_nohit.pl $FILE > ${FILE%}_nohmn.fasta
