#! /usr/bin/env python3

#! /usr/bin/env python3

#This  script generates a PBS file for the AHPCC Razor Cluster

# Define variables
job_name = 'aivy'
queue = 'med16core'
job_out =  'aivy' # prefix for output file, hsould match the job name
nnum =  1 #node number
pnum = 1 #processor number
wall = 3 #this is in hours

#This section prints the header/required info for the PBS script
print("#PBS -N ", job_name) #job name
print('#PBS -q', queue) #which queue to use
print ('#PBS -j oe') #join the STDOUT and STDERR into a single file
print ('#PBS -o', job_out, '.$PBS_JOBID') # set the name of the job out file
print ('#PBS -l nodes=',str(nnum),':ppn=',str(pnum)) # how many resource to ask for (nodes = num nodes, ppn = num processors)
print ('#PBS -l walltime=' + str(wall) + ':00:00') # set the walltime w/in parameters of the queue (default = 1hr)
print()

# cd into working directory 
print('cd $PBS_O_WORKDIR')
print()

# load the necessary modules
print ("# load modules")
print ('module purge')
print ("module load gcc/7.2.1")
print()

# commands for this job
print('# insert commands here')
