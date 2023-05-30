import sys

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
		if fields[0] in table:
			fid = table[fields[0]]
			mString = ','.join(fields) + ',' + fid + '\n'
			oFile.write(mString)
		else:
			print(fields[0])
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
		mTableTwitter[data[0]] = data[1]
	for nRow in mFileIRS:
		fields = nRow.rstrip().split(',')
		#Here fields[2] is a proxy for the number of household migrated
		mTableIRS[fields[-1]] = [fields[1], fields[2]] 
	for ele in mTableTwitter.keys():
		if ele in mTableIRS:
			mString = ele + ',' + mTableTwitter[ele] + ',' + ','.join(mTableIRS[ele]) + '\n'
			oFile.write(mString)
	oFile.close()
	mFileTwitter.close()
	mFileIRS.close()



def main():
	print("program starts ...")
	# data_process("migration_outflow_IRS_1314.csv","migration_outflow_IRS_1314_FIP.csv")
	# data_process("migration_outflow_IRS_1415.csv","migration_outflow_IRS_1415_FIP.csv")
	# data_process_FID("flow_IRS_net_1314.csv", "flow_IRS_net_1314_FID.csv")
	# data_process_FID("flow_IRS_net_1415.csv", "flow_IRS_net_1415_FID.csv")

	correlate("twitter_flow_net_1314.csv","flow_IRS_net_1314_FID.csv","twitter_IRS_netflow_1314.csv")
	# correlate("twitter_flow_net_1415.csv","flow_IRS_net_1415_FID.csv","twitter_IRS_netflow_1415.csv")
	# correlate("us_flow_13_14_migrate_counts_all.txt","migration_outflow_IRS_1314_FID.csv","twitter_IRS_1314_all.csv")


if __name__ == '__main__':
	main()