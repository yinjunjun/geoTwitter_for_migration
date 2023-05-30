import sys
from collections import Counter

def main():
    print "program starts ..."
    mFile13 = open("/path/us_raw_filtered_traj_13_county_30days.txt","rb")
    mFile14 = open("/path/us_raw_filtered_traj_14_county_30days.txt","rb")
    
    oFile = open("us_flow_13_14.txt","wb")
    mTable13 = {}
    mTable14 = {}
    for mRow in mFile13:
        data = mRow.rstrip().split(',')
        mTable13[data[0]] = data[1]
    #print table
    for nRow in mFile14:
        fields = nRow.rstrip().split(',')
        mTable14[fields[0]] = fields[1]
    for ele in mTable13.keys():
        #print ele
        if ele in mTable14:
            if int(mTable13[ele]) != int(mTable14[ele]):
                mString = mTable13[ele] + ',' + mTable14[ele] + '\n'
                oFile.write(mString)
    oFile.close()
    mFile14.close()
    mFile13.close()
                
def flow_count():
    print "count starts"
    mFile = open("us_flow_13_14.txt","rb")
    oFile = open("us_flow_13_14_outflow_counts.txt","wb")
    moves = []
    for mRow in mFile:
        moves.append(mRow.rstrip())
    freqs = Counter(moves)
    #for ele in freqs.items():
    for ele in freqs.most_common():
        oFile.write(ele[0] + ',' + str(ele[1]) + '\n')
    oFile.close()
    mFile.close()
        
        


if __name__=='__main__':
    main()
    flow_count()
