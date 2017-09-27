#!bin/bash
#$ -cwd

# This is an example of how a script would look like that allows me to downlod data from the HMP (this case supragingival_plaque), deconpress it
# remove the compressed file, go into each of the new directories, remove singletons, rename the 1.fastq file and in this case remove the 
#2.fastq file. 

FILE=$(head -n $SGE_TASK_ID supragingival_plaquept1.txt | tail -n 1)

wget ftp://public-ftp.hmpdacc.org/Illumina/supragingival_plaque/${FILE%}.tar.bz2 &&

tar -xjf ${FILE%}.tar.bz2 &&

rm ${FILE%}.tar.bz2 &&

cd ${FILE%}/ &&

rm *.singleton.fastq &&

mv  *.1.fastq ${FILE%}_supragingival_plaque.1.fastq &&
