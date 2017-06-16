# Helpful Scripts on running some of the profiling programs out there. At this stage sequences has been trimmed, qualty checked, and removed of potential contamination (i.e. human). Look at Basic Workflow file

## Kraken
### First build the database, this can be done by looking at the manual or looking at the website mentioned in me workflow document. Once this is done you can then run the following commands:
####     a. Classify
         for file in *fasta; do perl kraken --db Bacteria_perio $file >> ${file%}.kraken ; done
        
####     b. There are many ways to report your sample information. I like the metaphlan style output because it looks alot like an OTU                 file and you can do multiple files at once
         perl kraken-mpa-report --header-line --db Bacteria_perio file1 file2 file3 ect.. >> kraken_sample_info_output_files.txt
         
## SMALT
### Smalt approach can be a bit complicated, but it is extremely fast and has the potential to do stuff that you can't with the other programs. 
####     a. Index the viral reference genome ( same as you would with the human). Additional infor found int the basic workflow file.
         smalt index -k -s 13 viral viral.genomic.fa
   
####     b. Map to reference genome:  ( y is the percent alignment i want use .9 for human but if doing viruses you will use 0.8)
         smalt map -n 10 -y 0.8 -f samsoft -o file.samsoft trimmed_file_quality_checked_no_contamination.fasta 
         
####     c. Then comes some tricky grep: the samsoft file is going to have alot of sequences that did not match but will still record on               the file so we need to seperate that using this code:
            grep -v '@SQ' trimmed_file_quality_checked_no_contamination.samsoft | grep -v '@HQ' | grep -v '@PG' | grep -v '@HD' | cut -f 3             | sort -n | uniq -c |sort -n -r | paste -- > viral_hits.txt
       
```Example output:
Abundance   gene_ref
955402 
    270 gi|155573622|ref|NC_006273.2|
    161 gi|9626243|ref|NC_001416.1|```
####     d. Now i will want to know what those gi belong to so i will do a complicated grep looking for those gi in my viral reference                 database:
            cat viral_hits.txt | cut -d'|' -f2 | xargs -I{} grep '{}' reference_viral_database.fasta > viral_names.txt
####     c. Then we can go to the next part which is pasting the viral names to viral hits:
            cut -d' ' -f1 --complement viral_names.txt | paste viral_hits.txt - >viral_hits_and_names.txt


