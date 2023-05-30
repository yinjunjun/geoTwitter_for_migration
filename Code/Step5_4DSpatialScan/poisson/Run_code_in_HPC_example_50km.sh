#!/bin/bash

#SBATCH -p RM
#SBATCH -t 2:00:00
#SBATCH -N 3
#SBATCH --ntasks-per-node 10

#SBATCH --mail-type=ALL

# send mail to this address
#SBATCH --mail-user=xx@gmail.com

#echo commands to stdout
set -x

module load mpi/gcc_openmpi 
/path/4DScanPoi /path/twitter_IRS_outflow_pairs_coords_proj_1314.csv 50.0 20 30 99 -1 2.0

