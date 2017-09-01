#!/bin/bash
#$ -cwd

#Run deconseq on multiple files at once. This will be after split_fasta.sh
FILE=$(head -n $SGE_TASK_ID deconfiles.txt | tail -n 1)

perl ~/deconseq-standalone-0.4.3/bwasw_modified_source/deconseq.pl -f $FILE -dbs hs_ref_GRCh37_p7 \
-dbs_retain bacteria_virus -out_dir deconseq/ -id $FILE -i 90 -c 90 -group 1

# '-dbs_retain bacteria_virus' can be changed to '-dbs_retain virus' if you only want to keep viral reads
