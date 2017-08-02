#!/bin/bash
#$ -cwd
#in order for the SGE_TASK_ID to work, files must be submitted to the cluster qsub -t must be involved

#FileA is our fowards reads (R1) and FileB is our reverse reads (R2). Make sure files are sorted prior to use so first file on FileA should be the same as first file on FileB.

FILEA=$(head -n $SGE_TASK_ID RFfile.txt | tail -n 1)
FILEB=$(head -n $SGE_TASK_ID RRfile.txt | tail -n 1)
A=$(echo $FILEA | cut -c 15-27)

# prinseq command
perl ~/prinseq-lite-0.20.4/prinseq-lite.pl -verbose -derep 1245 -lc_method entropy \
-lc_threshold 50 -trim_qual_right 20 -trim_qual_left 20 -trim_qual_type mean \
-trim_qual_rule lt -trim_qual_window 2 -trim_qual_step 1 -trim_tail_left 5 \
-trim_tail_right 5 -min_len 60 -min_qual_mean 25 -ns_max_p 1 \
-fastq $FILEA -fastq2 $FILEB -log ${A%}_prinseq.log -out_bad ${A%}_prinseq_bad \
-out_good ${A%}_prinseq_good
