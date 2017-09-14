#!/bin/bash
#$ -cwd

# Script allows you to split a fasta file into multiple (smaller) fasta files for quicker analysis on the cluster downstream.
FILE=$(head -n $SGE_TASK_ID fasta.txt  | tail -n 1)
perl ~/deconseq-standalone-0.4.3/splitFasta.pl -verbose -i $FILE -n 9
