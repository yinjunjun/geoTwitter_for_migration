"""
Linear regression with marginal distributions
=============================================

_thumb: .5, .6
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import powerlaw
from scipy.stats import spearmanr
from scipy.stats import kendalltau



# sns.set(style="darkgrid", color_codes=True)
# sns.set(style="white", palette="muted", color_codes=True)
sns.set(style="white")

# f, axes = plt.subplots(2, 2, figsize=(9, 9), sharex=True)
f, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 9), sharex=False, sharey=False)

# sns.despine(left=True)

header_list1 = ["county","twitter14", "IRS14"]
header_list2 = ["county","twitter15", "IRS15"]
# tips=pd.read_csv('twitter_IRS_1314_zero.csv', sep=',')
outtrips1314=pd.read_csv('county_twitter_IRS_out_1314_30.csv', sep=',', names=header_list1)
outtrips1415=pd.read_csv('county_twitter_IRS_out_1314_30.csv', sep=',', names=header_list2)


##Normalization min max
xx1 = (outtrips1314['twitter14']-np.min(outtrips1314["twitter14"]))/(np.max(outtrips1314["twitter14"])- np.min(outtrips1314["twitter14"]))
yy1 = (outtrips1314['IRS14']-np.min(outtrips1314["IRS14"]))/(np.max(outtrips1314["IRS14"])- np.min(outtrips1314["IRS14"]))
# slope, intercept, r_value, p_value, std_err = stats.linregress(xx1, yy1)
# print(slope,intercept,r_value,p_value,std_err)

xx2 = (outtrips1415['twitter15']-np.min(outtrips1415["twitter15"]))/(np.max(outtrips1415["twitter15"])- np.min(outtrips1415["twitter15"]))
yy2 = (outtrips1415['IRS15']-np.min(outtrips1415["IRS15"]))/(np.max(outtrips1415["IRS15"])- np.min(outtrips1415["IRS15"]))
# slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(xx2, yy2)
# print(slope2,intercept2,r_value2,p_value2,std_err2)




outtrips1314["x"] = outtrips1314["twitter14"]/np.max(outtrips1314["twitter14"])
outtrips1314["y"] = outtrips1314["IRS14"]/np.max(outtrips1314["IRS14"])

coef1, p1 = spearmanr(outtrips1314['twitter14'], outtrips1314["IRS14"])
coef2, p2 = kendalltau(outtrips1314['twitter14'], outtrips1314["IRS14"])
print(coef1)
print(p1)

print(coef2)
print(p2)

