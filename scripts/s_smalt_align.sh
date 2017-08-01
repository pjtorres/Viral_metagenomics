#!/bin/bash
#$ -cwd
#in order for the SGE_TASK_ID to work, files must be submitted to the cluster qsub -t must be invoked

FILE=$(head -n $SGE_TASK_ID file.txt | tail -n 1)
AS=$(echo $FILE |sed -e s/_L002__prinseq_1.fastq/.samsoft/)

#command 
/usr/local/smalt/bin/smalt map -n 10 -y 0.8 -f samsoft -o $AS /home3/torres/smalt/hg19 $FILE
