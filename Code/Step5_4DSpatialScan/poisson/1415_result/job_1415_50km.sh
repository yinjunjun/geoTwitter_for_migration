#!/bin/bash

#SBATCH -p RM
#SBATCH -t 2:00:00
#SBATCH -N 3
#SBATCH --ntasks-per-node 10

#SBATCH --mail-type=ALL

# send mail to this address
#SBATCH --mail-user=yinjunjun@gmail.com

#echo commands to stdout
set -x

module load mpi/gcc_openmpi 
/home/gchi0086/storage/projects/twitter_migration/step4/4DSpatialScan/poisson/4DScanPoi /home/gchi0086/storage/projects/twitter_migration/step4/4DSpatialScan/data/twitter_IRS_outflow_pairs_coords_proj_1415.csv 50.0 20 30 99 1 2.0


