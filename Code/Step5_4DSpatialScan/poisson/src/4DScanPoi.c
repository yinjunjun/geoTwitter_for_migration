/**
 * 4DScanPoi.c
 * Authors: Yizhao Gao <yizhaotsccsj@gmail.com>,Junjun Yin <yinjunjun@gmail.com>
 * Date: {08/01/2020}
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "io.h"
#include "scan.h"
#include "mc.h"

int main(int argc, char ** argv) {
	
	if(argc != 8)
	{
		printf("Incorrect number of parameters: 4DScanPoi [inputFile] [windowInc] [windowCount] [#ofClusters] [#ofMonteCarlo] [HighOrLowIndicator] [elimIntersectOD]\n");
		printf("[HighOrLowIndicator]\n\t1: High Only\n\t-1: Low Only\n\t0: Both\n");
		printf("[double elimIntersectOD]\n\t-1: Allow intersect\n\t1.0: Center not in area\n\t2.0: No intersecting\n");
		exit(1);
	}

	double wSize = atof(argv[2]);
        int wCount = atoi(argv[3]);
        int nClusters = atoi(argv[4]);
        int nSim = atoi(argv[5]);
	int highLow = atoi(argv[6]);
	double elimIntersectOD = atof(argv[7]);

	double * x1;
	double * y1;
	double * x2;
	double * y2;
	int * nPop;
	int * nEvent;

	int popCount;
	int eventCount;
	int locCount;

	FILE * file;
	if(NULL == (file = fopen(argv[1], "r"))) {
		printf("ERROR: Can't open the input file.\n");
		exit(1);
	}

	locCount = getNumPoints(file);

	if(NULL == (x1 = (double *) malloc (locCount * sizeof(double)))) {
		printf("ERROR: Out of memory at line %d in file %s\n", __LINE__, __FILE__);
		exit(1);
	}
	if(NULL == (y1 = (double *) malloc (locCount * sizeof(double)))) {
		printf("ERROR: Out of memory at line %d in file %s\n", __LINE__, __FILE__);
		exit(1);
	}
	if(NULL == (x2 = (double *) malloc (locCount * sizeof(double)))) {
		printf("ERROR: Out of memory at line %d in file %s\n", __LINE__, __FILE__);
		exit(1);
	}
	if(NULL == (y2 = (double *) malloc (locCount * sizeof(double)))) {
		printf("ERROR: Out of memory at line %d in file %s\n", __LINE__, __FILE__);
		exit(1);
	}
	if(NULL == (nPop = (int *) malloc (locCount * sizeof(int)))) {
		printf("ERROR: Out of memory at line %d in file %s\n", __LINE__, __FILE__);
		exit(1);
	}
	if(NULL == (nEvent = (int *) malloc (locCount * sizeof(int)))) {
		printf("ERROR: Out of memory at line %d in file %s\n", __LINE__, __FILE__);
		exit(1);
	}

	readFile(file, x1, y1, x2, y2, nPop, nEvent, popCount, eventCount);
	
	printf("There is %d locations\n", locCount);
	printf("Total Pop count: \t%d\nTotal Event count:\t%d\n", popCount, eventCount);	

	fclose(file);
	printf("Finish reading input files.\n");

	int * popInW;
	int * eventInW;

	if(NULL == (popInW = (int *) malloc (locCount * wCount * sizeof(int)))) {
		printf("ERROR: Out of memory at line %d in file %s\n", __LINE__, __FILE__);
		exit(1);
	}
	if(NULL == (eventInW = (int *) malloc (locCount * wCount * sizeof(int)))) {
		printf("ERROR: Out of memory at line %d in file %s\n", __LINE__, __FILE__);
		exit(1);
	}

	getPECount(x1, y1, x2, y2, nPop, nEvent, locCount, wSize, wCount, popInW, eventInW, elimIntersectOD);
	
/*	
	int nZero = 0;
	int nMOne = 0;
	for(int i = 0; i < locCount * wCount; i++) {
		if(popInW[i] == 0) {
			nZero ++;
		}
		else {
			nMOne ++;
		}
	}

	printf("%d 0\t\t%d -1\n", nZero, nMOne);	
*/
	double * ll;
	if(NULL == (ll = (double *) malloc (locCount * wCount * sizeof(double)))) {
		printf("ERROR: Out of memory at line %d in file %s\n", __LINE__, __FILE__);
		exit(1);
	}

	loglikelihood(ll, popInW, eventInW, locCount * wCount, popCount, eventCount, highLow);
/*
	for(int i = 0; i < locCount; i++) {
		for(int j = 0; j < wCount; j++) {
			printf("%lf,\t", ll[i * wCount + j]);
		}
		printf("\n");
	}
*/

	int * center;
	int * radius;
	double * cLL;

	if(NULL == (center = (int *) malloc (nClusters * sizeof(int)))) {
		printf("ERROR: Out of memory at line %d in file %s\n", __LINE__, __FILE__);
		exit(1);
	}

	if(NULL == (radius = (int *) malloc (nClusters * sizeof(int)))) {
		printf("ERROR: Out of memory at line %d in file %s\n", __LINE__, __FILE__);
		exit(1);
	}

	if(NULL == (cLL = (double *) malloc (nClusters * sizeof(double)))) {
		printf("ERROR: Out of memory at line %d in file %s\n", __LINE__, __FILE__);
		exit(1);
	}

	findTopNCluster(x1, y1, x2, y2, locCount, ll, wSize, wCount, center, radius, cLL, nClusters);

	int * clusterPop;
	int * clusterEvent;
	double * cRadius;
	bool * highCluster;

	if(NULL == (clusterPop = (int *) malloc (nClusters * sizeof(int)))) {
		printf("ERROR: Out of memory at line %d in file %s\n", __LINE__, __FILE__);
		exit(1);
	}
	if(NULL == (clusterEvent = (int *) malloc (nClusters * sizeof(int)))) {
		printf("ERROR: Out of memory at line %d in file %s\n", __LINE__, __FILE__);
		exit(1);
	}
	if(NULL == (cRadius = (double *) malloc (nClusters * sizeof(double)))) {	
		printf("ERROR: Out of memory at line %d in file %s\n", __LINE__, __FILE__);
		exit(1);
	}
	if(NULL == (highCluster = (bool *) malloc (nClusters * sizeof(bool)))) {
		printf("ERROR: Out of memory at line %d in file %s\n", __LINE__, __FILE__);
		exit(1);
	}

	int aCenter;
	int aRadius;

	for(int i = 0; i < nClusters; i ++) {
		aCenter = center[i];
		aRadius = radius[i];
		if(aCenter == -1) {
			nClusters = i;
			break;
		}
		clusterPop[i] = popInW[aCenter * wCount + aRadius];
		clusterEvent[i] = eventInW[aCenter * wCount + aRadius];
		cRadius[i] = wSize * (aRadius + 1);

		double expEvent = (double)eventCount * clusterPop[i] / popCount;
		if(clusterEvent[i] > expEvent)      //High clusters
			highCluster[i] = true;
		else
			highCluster[i] = false;
	}

//Monte Carlo
	int * nExtreme;

	if(nSim > 0) {

//		nExtreme = monteCarloOld(x1, y1, x2, y2, nPop, locCount, popCount, eventCount, clusterEvent, center, cRadius, highCluster, nClusters, nSim);
		nExtreme = monteCarlo(x1, y1, x2, y2, nPop, popInW, locCount, popCount, eventCount, wSize, wCount, highLow, elimIntersectOD, cLL, nClusters, nSim);
	}

	printf("############### Cluster Info ###############\n");
	printf("ID,HL,X1,Y1,X2,Y2,Radius,Event,ExpEvent");
	if(nSim > 0)
		printf(",LL,P\n");
	else
		printf(",LL\n");
	for(int i = 0; i < nClusters; i ++) {
		aCenter = center[i];
		aRadius = radius[i];

		double expEvent = (double)eventCount * clusterPop[i] / popCount;

		printf("%d", i);
		if(highCluster[i]) 	//High clusters
			printf(",H");
		else				//Low clusters
			printf(",L");
		printf(",%lf,%lf,%lf,%lf,%lf", x1[aCenter], y1[aCenter], x2[aCenter], y2[aCenter], cRadius[i]);
		printf(",%d,%lf", clusterEvent[i], expEvent);
		if(nSim > 0)
			printf(",%lf,%lf\n", cLL[i], (double)(nExtreme[i] + 1) / (nSim + 1));
		else
			printf(",%lf\n", cLL[i]);
	}

	printf("############ Cluster Membership ############\n");

	bool inCluster;
	double distance;		
	double radiusValue;

	//Find the cluster belonging of each location
	for(int i = 0; i < locCount; i++) {
		inCluster = false;
		for(int j = 0; j < nClusters; j++) {
			aCenter = center[j];
			radiusValue = cRadius[j];
			distance = sqrt((x1[i] - x1[aCenter]) * (x1[i] - x1[aCenter]) + (y1[i] - y1[aCenter]) * (y1[i] - y1[aCenter]) + (x2[i] - x2[aCenter]) * (x2[i] - x2[aCenter]) + (y2[i] - y2[aCenter]) * (y2[i] - y2[aCenter]));
			if(distance <= radiusValue) {
				printf("%lf,%lf,%lf,%lf,%d,%d,%d\n", x1[i], y1[i], x2[i], y2[i], nPop[i], nEvent[i], j);
				inCluster = true;
				break;
			}
		}
		if(!inCluster)
			printf("%lf,%lf,%lf,%lf,%d,%d,-1\n", x1[i], y1[i], x2[i], y2[i], nPop[i], nEvent[i]);
	}



	free(clusterPop);
	free(clusterEvent);
	free(cRadius);
	free(highCluster);

	free(center);
	free(radius);
	free(cLL);

	free(ll);

	free(popInW);
	free(eventInW);

	free(x1);
	free(y1);
	free(x2);
	free(y2);
	free(nPop);
	free(nEvent);

	if(nSim > 0)
		free(nExtreme);
	
	return 0;
}
