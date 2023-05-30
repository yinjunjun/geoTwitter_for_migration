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
hadoop fs -put /home/gchi0086/storage/projects/twitter_migration/data/traj_revert/filtered/twitter_data_usa_2015_filter_sorted.txt
hadoop jar dist/UserMainCounty.jar /user/gchi0086/twitter_data_usa_2015_filter_sorted.txt /user/gchi0086/us_flow_15_filtered
hdfs dfs -getmerge /user/gchi0086/us_flow_15_filtered /pylon5/se5fp6p/gchi0086/projects/twitter_migration/data/flow/filtered/us_flow_15_fitered.txt
hdfs dfs -rm -r /user/gchi0086/*


#move to working directory
###cd $SCRATCH

