#!/usr/bin/env python3

job_name  = 'amivy'
queue = 'ocomp06'
out = 'amivy'
nnum = 1
pnum = 32
wall = 6

print('#SBATCH -J', job_name)
print('#SBATCH --partition', queue)
print('#SBATCH -o'+ out + '_%j.txt')
print('#SBATCH -e' + out + '_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=amivy@uark.edu')
print('#SBATCH --nodes=', nnum)
print('#SBATCH --ntasks-per-node=', pnum)
print('#SBATCH --time='+ str(wall) + ':00:00')

print('export OMP_NUM_THREADS=32')

print(
'''
# load required modules
module load samtools
module load jellyfish
module load bowtie2
module load salmon/0.8.2
module load java
 
# cd into the directory where you're submitting this script from
cd $SLURM_SUBMIT_DIR

# copy files from storage to scratch
rsync -av RNA-R*.fastq.gz /scratch/$SLURM_JOB_ID

# cd onto the scratch disk to run the job
cd /scratch/$SLURM_JOB_ID/

# run the Trinity assembly
/share/apps/bioinformatics/trinity/trinityrnaseq-v2.11.0/Trinity --seqType fq --left RNA-R1.fastq.gz --right RNA-R2.fastq.gz --CPU 48 --max_memory 250G --trimmomatic --no_normalize_reads --full_cleanup --output trinity_Run2
 
# copy output files back to storage
rsync -av trinity_Run2 $SLURM_SUBMIT_DIR
'''
)
