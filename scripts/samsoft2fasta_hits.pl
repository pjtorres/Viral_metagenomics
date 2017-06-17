#samsoft to fasta of the reads that did map on the reference index
#
#

open (SAMSOFT, $ARGV[0]);
my @line;

while (<SAMSOFT>){
        $line=$_;
        if ($line =~ m/^@/){}
                else {
                @columns=split(/\t/, $line);
                        if ($columns[1]!=4){
                                print STDOUT ">$columns[0]\n$columns[9]\n";
                                }
                        else {}
                        }
                }

#credit goes to Ana Cobian (git name: yinacobian) for this script
