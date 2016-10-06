# Trim Adapters
far --source rawdata.fastq --target trimed.fastq --format fastq --min-overlap 6 --adapters 3ad.fasta --min-readlength 10 --cut-off 2 --trim-end right -th 4
python cGetReads.py trimed.fastq | sort | uniq -c | sort -k1,1nr > trimed.reads
python cGetReadsCount.py trimed.reads > trimed.readscount

#Mapping to Genome
bowtie-0.12.7/bowtie -v 0 -a --best --strata -p 6 ~/Genome/hg19/hg19 trimed.readscount -f trimed.map 

#Get BED files of mapping Reads
python cGetReadsBED1726.py trimed.map > trimed_1726.bed

#Get BED files of mature miRNAs in Human and Mouse
python cGetmiRNAFromdat.py miRBaseRelease18/miRNA.dat > miRBaseRelease18/hsa/miRNAFromdat.txt
python cGetmiRNAmatureBED.py miRBaseRelease18/hsa/hsa.bed miRBaseRelease18/hsa/miRNAFromdat.txt > miRBaseRelease18/hsa/human_maturemiRNA.bed

#Compare the reads BED and mature miRNA BED
BEDTools-Version-2.9.0/bin/intersectBed -wo -s -a miRBaseRelease18/hsa/human_maturemiRNA.bed -b trimed_1726.bed > miRBaseRelease18/hsa/trimed_1726_hsamiRNA.txt

#Count reads number of each miRNA and its isomiR
python cGetmiRNAisoTotalReads.py miRBaseRelease18/hsa/human_maturemiRNA.bed miRBaseRelease18/hsa/trimed_1726_hsamiRNA.txt | cut -f 1-6,8 | sort -k7,7nr > miRBaseRelease18/hsa/trimed_1726_hsamiRNA_total.txt

#Combined the reads count of each miRNA and its isomiR from each sample into one file.
cut -f 7-26 miRBaseRelease18/hsa/SNB19_nc_trimed_1726_hsamiRNA_total.txt > miRBaseRelease18/hsa/t1
cut -f 7-26 miRBaseRelease18/hsa/SNB19_siTDP_trimed_1726_hsamiRNA_total.txt > miRBaseRelease18/hsa/t2
cut -f 7-26 miRBaseRelease18/hsa/SY5Y_nc_trimed_1726_hsamiRNA_total.txt > miRBaseRelease18/hsa/t3
cut -f 7-26 miRBaseRelease18/hsa/SY5Y_siTDP_trimed_1726_hsamiRNA_total.txt > miRBaseRelease18/hsa/t4
paste trimed_1726_hsamiRNA_total.txt t1 t2 t3 t4 > miRBaseRelease18/hsa/hsamiRNA_combined.txt

cut -f 7-26 miRBaseRelease18/mmu/HT22_nc_trimed_1726_mmumiRNA_total.txt > miRBaseRelease18/mmu/t6
cut -f 7-26 miRBaseRelease18/mmu/HT22_siTDP_trimed_1726_mmumiRNA_total.txt > miRBaseRelease18/mmu/t7
paste trimed_1726_mmumiRNA_total.txt t6 t7 > miRBaseRelease18/mmu/mmumiRNA_combined.txt

#Get total reads number if miRNA locate in many loci
python cGetmiRNATotalReadsOfUniqmiRNA.py human_maturemiRNA.list hsamiRNA_combined.txt > hsamiRNA_Expression.txt

python cGetmiRNATotalReadsOfUniqmiRNA.py mouse_maturemiRNA.list mmumiRNA_combined.txt > mmumiRNA_Expression.txt

#Get miRNA and isomiR total profile. Count reads for every type of isomiR
python cGetmiRNAisoTotalProfile.py miRBaseRelease18/hsa/human_maturemiRNA.list miRBaseRelease18/hsa/trimed_1726_hsamiRNA.txt > miRBaseRelease18/hsa/trimed_1726_hsamiRNA_TotalProfile.txt

# get Reads with mismatches
python cGetSubSeqFastaByList.py trimed_v0.list(the list of reads mapping to genome without mismatch) trimed.readscount > trimed_withmismatch.fasta

# mapping rawdata to genome with 3 mismatches to find isomiR with 3' modification
bowtie-0.12.7/bowtie  -v 3 -a --best --strata -p 6 ~/Genome/hg19/hg19 trimed_withmismatch.fasta -f trimed_v3.map 

# get reads BED with mismatches 
python cGetReadsBED.py trimed_v3.map > trimed_v3.bed

#get reads with mismatches mapping to mature miRNAs
BEDTools-Version-2.9.0/bin/intersectBed -wo -s -a miRBaseRelease18/hsa/human_maturemiRNA.bed -b trimed_v3.bed > isomiR/trimed_hsaisomiR.txt
#get isomiR With one mismatch
python cGetisomiR3aWithMisOnematch.py miRBaseRelease18/hsa/human_maturemiRNA.list somiR/trimed_hsaisomiR.txt > miRBaseRelease18/hsa/isomiRWithmismatch/a3/trimed_hsaisomiR_a3.txt
