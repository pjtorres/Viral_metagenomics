package DeconSeqConfig;


use strict;

use constant DEBUG => 0;
use constant PRINT_STUFF => 1;
use constant VERSION => '0.4.3';
use constant VERSION_INFO => 'DeconSeq version '.VERSION;

use constant ALPHABET => 'ACGTN';

use constant DB_DIR => '/home3/torres/deconseq-standalone-0.4.3/db/';
use constant TMP_DIR => 'tmp/';
use constant OUTPUT_DIR => 'output/';

use constant PROG_NAME => 'bwa64';  # should be either bwa64 or bwaMAC (based on your system architecture)
use constant PROG_DIR => '/home3/torres/deconseq-standalone-0.4.3/bwasw_modified_source/';      # should be the location of the PROG_NAME file (use './' if in the same location at the perl script)

use constant DBS => {hs_ref_GRCh37_p7 => {name => 'Human_Reference_GRCh37',  #database name used for display and used as input for -dbs and -dbs_retain
                               db => 'hs_ref_GRCh37_p7'},            #database name as defined with -p for "bwa index -p ..." (specify multiple database chunks separated with commas without space; e.g. hs_ref_s1,hs_ref_s2,hs_ref_s3)
                     bacteria_virus => {name => 'Bacterial_genomes',
                              db => 'bacteria_1,bacteria_2,virus'},
                     virus => {name => 'Viral_genomes',
                             db => 'virus'}};
use constant DB_DEFAULT => 'hsref';

#######################################################################

use base qw(Exporter);

use vars qw(@EXPORT);

@EXPORT = qw(
             DEBUG
             PRINT_STUFF
             VERSION
             VERSION_INFO
             ALPHABET
             PROG_NAME
             PROG_DIR
             DB_DIR
             TMP_DIR
             OUTPUT_DIR
             DBS
             DB_DEFAULT
             );

1;
