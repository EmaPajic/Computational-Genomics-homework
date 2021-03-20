"""
@author: EmaPajic
"""

import pysam

def main():
    path_to_file = 'merged-tumor.bam'
    num_unmapped = 0
    num_reads = 0
    num_mapping_quality_0 = 0
    sum_mapping_quality = 0
    
    for read in pysam.AlignmentFile(path_to_file):
        num_reads += 1
        sum_mapping_quality += read.mapping_quality
        
        if read.flag & 4:
            num_unmapped += 1
        if read.mapping_quality == 0:
            num_mapping_quality_0 += 1
            
    avg_mapping_quality = sum_mapping_quality / num_reads
    avg_mapping_quality_without_0s = sum_mapping_quality /(num_reads - num_mapping_quality_0)
    
    print("Number of unmapped reads: ", num_unmapped)
    print("Total number of reads: ", num_reads)
    print("Number of reads with mapping quality 0: ", num_mapping_quality_0)
    print("Average mapping quality: ",avg_mapping_quality)
    print("Average mapping quality if reads with mapping quality 0 are filtered out: ", 
          avg_mapping_quality_without_0s)

if __name__ == '__main__':
    main()