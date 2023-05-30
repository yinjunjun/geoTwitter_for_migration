#!/bin/bash

#SBATCH -p RM
#SBATCH -t 5:00:00
#SBATCH -N 3
#####SBATCH --ntasks-per-node 14

#SBATCH --mail-type=ALL

# send mail to this address
#SBATCH --mail-user=yinjunjun@gmail.com

#echo commands to stdout
set -x

module load hadoop/2.7.2
start-hadoop.sh
cd /home/gchi0086/storage/projects/twitter_migration/step3/make_trajectories_county/
hdfs dfs -mkdir /user/gchi0086
hadoop fs -put /home/gchi0086/storage/projects/twitter_migration/data/raw/2014_usa_all.txt
hadoop jar dist/maketrajectories.jar classes/runhadoop/RunMovePattern.class /user/gchi0086/2014_usa_all.txt /user/gchi0086/us_raw_traj_14
hdfs dfs -getmerge /user/gchi0086/us_raw_traj_14 /home/gchi0086/storage/projects/twitter_migration/data/traj/us_raw_traj_14.txt
hdfs dfs -rm -r /user/gchi0086/*

#move to working directory
###cd $SCRATCH

