# Viral Metagenomics
Flow and scripts to analyze Viral metagenomics

# Basic Workflow
## 1. Always run some sort of quality check to make sure your sequence output looks good and is the correct length ect..
### Can use FastqC (http://www.bioinformatics.babraham.ac.uk/projects/fastqc/)
## 2. Remove sequence adaptors
### Can use Trimmomatic (http://www.usadellab.org/cms/?page=trimmomatic) or TagCleaner (http://tagcleaner.sourceforge.net/)
## 3. Filter, reformat, or trim your genomic and metagenomic sequence data
### I usually use Prinseq (http://prinseq.sourceforge.net/)
## 4. Remove contamination- this will depend on sample source and question being asked. 
### Can use DeconSeq (http://deconseq.sourceforge.net/) , SMALT (http://www.sanger.ac.uk/science/tools/smalt-0), Snap (http://snap.cs.berkeley.edu/)... there are many tools to align your reads to a potential contamination reference genome and then remove those which aligned and keep those that did not.
#### Most of my work lately has been with human metagenome and human contamination is an issue. I must therefore build a human database to align against. This is what I do:
#### a. Download Human Database: wget hgdownload.cse.ucsc.edu/goldenPath/hg19/bigZips/chromFa.tar.gz
#### b. Then : tar -zxvf chromFa.tar.gz
#### c. Concatenate all file: cat chr*.fa > hg19.fa
## 5. Annotate Sequences
### So many choices I will mention a few:
#### blast (ftp://ftp.ncbi.nlm.nih.gov/blast/executables/LATEST/ncbi-blast-2.6.0+-x64-linux.tar.gz), MetaPhlan2 (https://bitbucket.org/biobakery/metaphlan2), FOCUS (http://edwards.sdsu.edu/focus/) , SUPERFOCUS (http://edwards.sdsu.edu/superfocus/), kraken (https://ccb.jhu.edu/software/kraken/), Human (https://huttenhower.sph.harvard.edu/humann)... ect Read up and see what will best help at answering your question
### but here I am doing viral metagenomics so:
#### Need to get viral reference file here (ftp://ftp.ncbi.nlm.nih.gov/refseq/release/viral/) download viral1.1.genomics.fna (true viruses) and viral.2.1genomic.fna (evidence of virus but not fully accepted by NCBI i.e. crassphage). Then I will concatenate both files.
#### you will need to build your database based on program used:
#### Smalt: smalt index -k 20 -s 13 viral /path/to/concatenated_viral_fna
#### blast: makeblastdb -in /path/to/concatenated_viral_fna -dbtype nucl -out viral_blastdb

