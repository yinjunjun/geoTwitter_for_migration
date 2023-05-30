import sys

def data_process_FIP(pathIn, pathOut):
	mFile = open(pathIn,"r")
	oFile = open(pathOut,"w")
	for mRow in mFile:
		data = mRow.rstrip().split(',')
		fipFrom = data[0] + data[1]
		fipTo = data[2] + data[3]
		mString = fipFrom + ',' + fipTo + ',' + data[-3] + ',' + data[-2] + '\n'
		oFile.write(mString)
	oFile.close()
	mFile.close()

def data_process_FID(pathIn, pathOut):
	mTable = open("county_fip_coord.csv","r")
	mFile = open(pathIn,"r")
	oFile = open(pathOut,"w")
	table = {}
	for mRow in mTable:
		data = mRow.rstrip().split(',')
		table[data[0]] = data[-1]
	for nRow in mFile:
		fields = nRow.rstrip().split(',')
		if fields[0] in table and fields[1] in table:
			fidFrom = table[fields[0]]
			fidTo = table[fields[1]]
			mString = ','.join(fields) + ',' + fidFrom + ',' + fidTo + '\n'
			oFile.write(mString)
		else:
			print(fields[0])
			print(fields[1])
	oFile.close()
	mFile.close()
	mTable.close()


def correlate(pathIn1,pathIn2,pathOut):
	mFileTwitter = open(pathIn1,"r")
	mFileIRS = open(pathIn2,"r")
	oFile = open(pathOut,"w")
	mTableTwitter = {}
	mTableIRS = {}
	for mRow in mFileTwitter:
		data = mRow.rstrip().split(',')
		mTableTwitter[(data[0],data[1])] = data[2]
	for nRow in mFileIRS:
		fields = nRow.rstrip().split(',')
		#Here fields[2] is a proxy for the number of household migrated
		mTableIRS[(fields[-2],fields[-1])] = [fields[2],fields[3]]
	for ele in mTableTwitter.keys():
		if ele in mTableIRS:
			mString = mTableTwitter[ele] + ',' + ",".join(mTableIRS[ele]) + '\n'
			oFile.write(mString)
		else:
			mString = mTableTwitter[ele] + ',' + '0,0' + '\n'
			oFile.write(mString)
	for ele in mTableIRS.keys():
		if ele in mTableTwitter:
			print(ele)
		else:
			mString = '0' + ',' + ",".join(mTableIRS[ele]) + '\n'
			oFile.write(mString)
	oFile.close()
	mFileTwitter.close()
	mFileIRS.close()



def main():
	print("program starts ...")
	# data_process("migration_outflow_IRS_1314.csv","migration_outflow_IRS_1314_FIP.csv")
	# data_process("migration_outflow_IRS_1415.csv","migration_outflow_IRS_1415_FIP.csv")
	# data_process_FID("migration_outflow_IRS_1314_FIP.csv", "migration_outflow_IRS_1314_FID.csv")
	# data_process_FID("migration_outflow_IRS_1415_FIP.csv", "migration_outflow_IRS_1415_FID.csv")

	correlate("us_flow_14_15_outflow_counts.txt","migration_outflow_IRS_1415_FID.csv","twitter_IRS_1415_exempt_zero.csv")
	# correlate("us_flow_14_15_migrate_counts.txt","migration_outflow_IRS_1415_FID.csv","twitter_IRS_1415.csv")
	# correlate("us_flow_13_14_migrate_counts_all.txt","migration_outflow_IRS_1314_FID.csv","twitter_IRS_1314_all.csv")


if __name__ == '__main__':
	main()