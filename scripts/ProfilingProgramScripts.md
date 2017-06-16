# Helpful Scripts on running some of the profiling programs out there

## Kraken
### First build the database, this can be done by looking at the manual or looking at the website mentioned in me workflow document. Once this is done you can then run the following commands:
###  a. Classify
        ```for file in *fasta; do perl kraken --db Bacteria_perio $file >> ${file%}.kraken ; done
     b. There are many ways to report your sample information. I like the metaphlan style output because it looks alot like an OTU file.           and you can do multiple files at once
        ``` perl kraken-mpa-report --header-line --db Bacteria_perio file1 file2 file3 ect.. >> kraken_sample_info_output_files.txt```
