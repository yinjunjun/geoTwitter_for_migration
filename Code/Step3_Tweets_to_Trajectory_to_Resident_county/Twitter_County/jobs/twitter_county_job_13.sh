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
cd /home/gchi0086/storage/projects/twitter_migration/step3/TweeterMainCounty/
hdfs dfs -mkdir /user/gchi0086
hadoop fs -put /home/gchi0086/storage/projects/twitter_migration/data/traj_revert/twitter_data_usa_2013_sorted.txt
hadoop jar dist/UserMainCounty.jar /user/gchi0086/twitter_data_usa_2013_sorted.txt /user/gchi0086/us_flow_13
hdfs dfs -getmerge /user/gchi0086/us_flow_13 /pylon5/se5fp6p/gchi0086/projects/twitter_migration/data/flow/us_flow_13.txt
hdfs dfs -rm -r /user/gchi0086/*


#move to working directory
###cd $SCRATCH

