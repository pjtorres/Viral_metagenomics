# Basic Workflow
## 1. Always run some sort of quality check to make sure your sequence output looks good and is the correct length ect..
### Can use FastqC (http://www.bioinformatics.babraham.ac.uk/projects/fastqc/)
## 2. Remove sequence adaptors
### Can use Trimmomatic (http://www.usadellab.org/cms/?page=trimmomatic) or TagCleaner (http://tagcleaner.sourceforge.net/)
#### Trimmomatic
```java -jar trimmomatic-0.36.jar PE seqfile_R1_001.fastq.gz seqfile _R2_001.fastq.gz paired.output_seqfile _R1_001.fastq.gz unpaired.seqfile_R1_001.fastq.gz paired.output_seqfile R2_001.fastq.gz unpaired.output_seqfile_R2_001.fastq.gz -trimlog output.log ILLUMINACLIP:~/trimmomatic-0.36/adapters/TruSeq3-PE-2.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36```
## 3. Filter, reformat, or trim your genomic and metagenomic sequence data
### I usually use Prinseq (http://prinseq.sourceforge.net/)
```
#!/bin/bash
#$ -cwd
#$ -S /bin/sh
perl -e 'foreach my $f qw(1_1bx_ATCACG_L001_ 12_1by_GAGTGG_L001_ 12_2by_ATTCCT_TTCCT_L001_ 12_3by_CTTGTA_L001_) {print STDERR `perl ~/prinseq-lite-020.4/prinseq-lite.pl -verbose -derep 1245 -lc_method entropy -lc_threshold 50 -trim_qual_right 20 -trim_qual_left 20 -trim_qual_type mean -trim_qual_rule lt -trim_qual_window 2 -trim_qual_step 1 -trim_tail_left 5 -trim_tail_right 5 -min_len 60 -min_qual_mean 25 -ns_max_p 1 -fastq ~/Perio_NA_data/$f\R1_001.fastq -fastq2 ~/Perio_NA_data/$f\R2_001.fastq -log ~/Perio_NA_data/$f\_prinseq.log -out_bad ~/Perio_NA_data/$f\_prinseq_bad -out_good ~/Perio_NA_data/$f\_prinseq`}'
```

## 4. Remove contamination- this will depend on sample source and question being asked. 
### Can use DeconSeq (http://deconseq.sourceforge.net/) , SMALT (http://www.sanger.ac.uk/science/tools/smalt-0), Snap (http://snap.cs.berkeley.edu/)... there are many tools to align your reads to a potential contamination reference genome and then remove those which aligned and keep those that did not.
#### Most of my work lately has been with human metagenome and human contamination is an issue. I must therefore build a human database to align against. This is what I do:
#### a. Download Human Database: wget hgdownload.cse.ucsc.edu/goldenPath/hg19/bigZips/chromFa.tar.gz
#### b. Then : tar -zxvf chromFa.tar.gz
#### c. Concatenate all file: cat chr*.fa > hg19.fa
#### d. Align sequences to reference human genome (using SMALT here)
```for file in *fastq; do smalt map -n 10 -y 0.9 -f samsoft -o ${file%}_noha19.samsoft ../../smalt/hg19 $file ; done```
#### e. Create a fasta with reads that did ***NOT*** map to reference genome (from scripts folder)
``` perl sansoft2fasta_nohits.pl ${file%}_noha19.samsoft >${file%}_noha19.fasta```

## 5. Annotate Sequences
### So many choices I will mention a few:
#### blast (ftp://ftp.ncbi.nlm.nih.gov/blast/executables/LATEST/ncbi-blast-2.6.0+-x64-linux.tar.gz), MetaPhlan2 (https://bitbucket.org/biobakery/metaphlan2), FOCUS (http://edwards.sdsu.edu/focus/) , SUPERFOCUS (http://edwards.sdsu.edu/superfocus/), kraken (https://ccb.jhu.edu/software/kraken/), Human (https://huttenhower.sph.harvard.edu/humann)... ect Read up and see what will best help at answering your question
### but here I am doing viral metagenomics so:
#### Need to get viral reference file here (ftp://ftp.ncbi.nlm.nih.gov/refseq/release/viral/) download viral1.1.genomics.fna (true viruses) and viral.2.1genomic.fna (evidence of virus but not fully accepted by NCBI i.e. crassphage). Then I will concatenate both files.
### you will need to build your database based on program used:
#### Smalt: smalt index -k 20 -s 13 viral /path/to/concatenated_viral_fna
#### blast: makeblastdb -in /path/to/concatenated_viral_fna -dbtype nucl -out viral_blastdb

