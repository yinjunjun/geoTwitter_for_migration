import sys

def total_inflow(pathIn, pathOut):
	mFlow = open(pathIn,"r")
	oFile = open(pathOut,"w")
	mList = []
	nList =[]
	for mRow in mFlow:
		table = {}

		data = mRow.rstrip().split(',')
		fipIn = data[0]
		nList.append(fipIn)
		table[fipIn] = int(data[2])
		mList.append(table)
	data ={}
	for ele in set(nList):
		# data[ele] = [0,0]
		# print(ele)
		
		result = []
		for item in mList:
			# print(item)
			if ele in item:
				result.append(item[ele])
		mX = 0
		for field in result:
			mX += field
		mString = ele + ',' + str(mX) + '\n'
		oFile.write(mString)


	oFile.close()
	mFlow.close()

def total_outflow(pathIn, pathOut):
	mFlow = open(pathIn,"r")
	oFile = open(pathOut,"w")
	mList = []
	nList =[]
	for mRow in mFlow:
		table = {}

		data = mRow.rstrip().split(',')
		fipIn = data[0]
		nList.append(fipIn)
		table[fipIn] = int(data[2])
		mList.append(table)
	data ={}
	for ele in set(nList):
		# data[ele] = [0,0]
		# print(ele)
		result = []
		for item in mList:
			if ele in item:
				# print(item)
				# print(ele)
				# print(item[ele])
				result.append(item[ele])
		mX = 0
		for field in result:
			mX += field
		mString = ele + ',' + str(mX) + '\n'
		oFile.write(mString)


	oFile.close()
	mFlow.close()

def total_flow(pathIn1, pathIn2, pathOut):
	mInFlow = open(pathIn1,"r")
	mOutFlow = open(pathIn2,"r")
	oFile = open(pathOut,"w")

	inTable ={}
	outTable = {}

	for mRow in mInFlow:
		data = mRow.rstrip().split(',')
		inTable[data[0]] = int(data[1])

	for nRow in mOutFlow:
		field = nRow.rstrip().split(',')
		outTable[field[0]] = int(field[1])

	for key in inTable.keys():
		if key in outTable:
			inX = inTable[key]
			outX = outTable[key]
			mString = key + ',' + str(inX - outX) + '\n'
			oFile.write(mString)
	oFile.close()
	mInFlow.close()
	mOutFlow.close()




def main():
	print("program starts ...")
	total_inflow("us_flow_14_15_inflow_counts.txt", "twitter_total_inflow_1415.csv")
	# total_inflow("us_flow_14_15_inflow_counts.txt", "twitter_total_inflow_1415.csv")

	total_outflow("us_flow_14_15_outflow_counts.txt", "twitter_total_outflow_1415.csv")
	# total_outflow("us_flow_14_15_migrate_counts.txt", "twitter_total_outflow_1415.csv")

	total_flow("twitter_total_inflow_1415.csv", "twitter_total_outflow_1415.csv", "twitter_flow_net_1415.csv")
	# total_flow("twitter_total_inflow_1415.csv", "twitter_total_outflow_1415.csv", "twitter_flow_net_1415.csv")


if __name__ == '__main__':
	main()