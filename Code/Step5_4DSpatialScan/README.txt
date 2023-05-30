# 4DSpatialScan
Find clusters (local excesses of events) in origin-destination movement datasets and more generally spatial interactions involving two locations

## Poisson model
A Poisson model deals with the number of spatial interactions occurring in a time interval and a pair of OD spatial regions.
### To run
4DScanPoi InputFile WindowInc WindowCount NumberofClusters NumberofMonteCarlo HighOrLowIndicator ElimIntersectOD
 1. InputFile: a CSV without header that has 6 column: xorigin, yorigin, xdestination, ydestination, numberOfCases and intensity for each location
 2. WindowInc: the increment of scan windows
 3. WindowCount: the number of scan windows put at each location, and thus the maximum scan window is (WindowInc * WindowCount)
 4. NumberofClusters: number of clusters to detect
 5. NumberofMonteCarlo: number of Monte Carlo simulation
 6. HighOrLowIndicator:
	* 1: high value clusters only
	* -1: low value clusters only
	* 0: both
 7. ElimIntersectOD: Whether clusters with intersecting origin and destination are allowed:
	* -1:  Allow intersect (no limit)
	* 1.0: Center of origin (destination) not in the area of destination (origin)
	* 2.0: No intersection allowed

## Reference
Kulldorff, M., 1997. A spatial scan statistic. Communications in Statistics-Theory and methods, 26(6), pp.1481-1496.
 
##Compile source code
Requires Open MPI (Open Source High Performance Computing) module and High Performance Computing environment
Use the Makefile in the "src" folder

##Example
poisson/Run_code_in_HPC_example_50km.sh
poisson/Run_code_in_HPC_example_25km.sh
