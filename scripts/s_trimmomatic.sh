#!/bin/bash
#$ -cwd
#in order for the SGE_TASK_ID to work, files must be submitted to the cluster qsub -t 1-#:steps must be used. # is the number of files in  your RAfile.txt

#FILEF are our foward reads (R1) and FILER are our reverse reads (R2). Sake sure you sort your list before hand to amke sure files are in the same order in both files or else you will have issues.
FILEF=$(head -n $SGE_TASK_ID RAfile.txt | tail -n 1)
FILER=$(head -n $SGE_TASK_ID RBfile.txt | tail -n 1)

#had to copy a Truseq3-PE-2.fa file into this directory because it isn't working otherwise


#Trimmomatic Command
java -jar ~/Trimmomatic-0.36/trimmomatic-0.36.jar PE $FILEF $FILER paired_output_${FILEF%} \
unpaired_output_${FILEF%} paired_output_${FILER%} unpaired_output_${FILER%} -trimlog output.log \
ILLUMINACLIP:TruSeq3-PE-2.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36


