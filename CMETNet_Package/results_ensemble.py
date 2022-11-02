'''
 (c) Copyright 2022
 All rights reserved
 Programs written by Khalid A. Alobaid
 Department of Computer Science
 New Jersey Institute of Technology
 University Heights, Newark, NJ 07102, USA
 Permission to use, copy, modify, and distribute this
 software and its documentation for any purpose and without
 fee is hereby granted, provided that this copyright
 notice appears in all copies. Programmer(s) makes no
 representations about the suitability of this
 software for any purpose.  It is provided "as is" without
 express or implied warranty.
'''

import numpy as np
import pandas as pd
import datetime
from sklearn.metrics import mean_absolute_error

year=2013
temp_x=0
path = '/results/'

filename = path+'Ensemble_model_'+str(year)+'_All.csv'
All_result = pd.read_csv(filename, header = None)

filename = path+'Ensemble_model_'+str(year)+'_y_test.csv'
y_test = pd.read_csv(filename, header = None)

filename = path+'CMETNet_CNN_'+str(year)
CNN_result = pd.read_csv(filename)


combined_results = pd.DataFrame(index=range(0,len(All_result)),columns = ["all_4_models","CNN",'True TT'])
for row in range(0,len(combined_results)):
    temp_result_list = [All_result[0][row],All_result[1][row],All_result[2][row],All_result[3][row]]
    combined_results.at[row,'all_4_models']= temp_result_list
    combined_results.at[row,'CNN']= CNN_result["results"][row]   
    combined_results.at[row,'True TT']= y_test[0][row]

    combined_results["Predicated TT"]=0.0

for row in range(0,len(combined_results)):
    temp_text = combined_results["CNN"][row]
    if not (temp_text=='0'):
        temp_text = temp_text.replace("[", "").replace("]", "")
        temp_list = list(map(float, temp_text.split(',')))
        combined_results.at[row,'CNN']= temp_list        

for row in range(0,len(combined_results)):
    if (combined_results["CNN"][row]=='0'):
        temp_list = combined_results["all_4_models"][row]
        temp_list = np.array(temp_list)
        temp_list[temp_list != 0]
    else:
        temp_list = combined_results["all_4_models"][row] + combined_results["CNN"][row]
        temp_list = np.array(temp_list)
        temp_list[temp_list != 0]

for x in range(0,len(combined_results)):
    temp_list_of_median = []
    if(combined_results["CNN"][x]=='0'):
        combined_results.at[x,'Predicated TT']= round((np.median(combined_results["all_4_models"][x])),2)
    else:
        for j in range(0,len(combined_results["CNN"][x])):
            temp_list_1 = []
            result_1 = combined_results["CNN"][x][j]
            result_2 = combined_results["True TT"][x]
            result_3 = result_1*(1-temp_x)+result_2*temp_x
            temp_list_1 = combined_results["all_4_models"][x][:]
            temp_list_1.append(result_3)
            median_temp = np.median(temp_list_1)
            temp_list_of_median.append(median_temp)
        median_of_medians = np.median(temp_list_of_median)
        combined_results.at[x,'Predicated TT']= round(median_of_medians,2)     

for row in range(0,len(combined_results)):
    if (combined_results["CNN"][row]=='0'):
        temp_list = combined_results["all_4_models"][row]
        temp_list = np.array(temp_list)
        temp_list[temp_list != 0]
    else:
        temp_list = combined_results["all_4_models"][row] + combined_results["CNN"][row]
        temp_list = np.array(temp_list)
        temp_list[temp_list != 0]
        
for x in range(0,len(combined_results)):
    temp_list_of_median = []
    if(combined_results["CNN"][x]=='0'):
        combined_results.at[x,'Predicated TT']= round((np.median(combined_results["all_4_models"][x])),2)
    else:
        for j in range(0,len(combined_results["CNN"][x])):
            temp_list_1 = []
            result_1 = combined_results["CNN"][x][j]
            result_2 = combined_results["True TT"][x]
            result_3 = result_1*(1-temp_x)+result_2*temp_x
            temp_list_1 = combined_results["all_4_models"][x][:]
            temp_list_1.append(result_3)
            median_temp = np.median(temp_list_1)
            temp_list_of_median.append(median_temp)
        median_of_medians = np.median(temp_list_of_median)
        combined_results.at[x,'Predicated TT']= round(median_of_medians,2)
        
for row in range(0,len(combined_results)):
    if (combined_results["CNN"][row]=='0'):
        temp_list = combined_results["all_4_models"][row]
        temp_list = np.array(temp_list)
        temp_list[temp_list != 0]
    else:
        temp_list = combined_results["all_4_models"][row] + combined_results["CNN"][row]
        temp_list = np.array(temp_list)
        temp_list[temp_list != 0]

for x in range(0,len(combined_results)):
    temp_list_of_median = []
    if(combined_results["CNN"][x]=='0'):
        combined_results.at[x,'Predicated TT']= round((np.median(combined_results["all_4_models"][x])),2)
    else:
        for j in range(0,len(combined_results["CNN"][x])):
            temp_list_1 = []
            result_1 = combined_results["CNN"][x][j]
            result_2 = combined_results["True TT"][x]
            result_3 = result_1*(1-temp_x)+result_2*temp_x
            temp_list_1 = combined_results["all_4_models"][x][:]
            temp_list_1.append(result_3)
            median_temp = np.median(temp_list_1)
            temp_list_of_median.append(median_temp)
        median_of_medians = np.median(temp_list_of_median)
        combined_results.at[x,'Predicated TT']= round(median_of_medians,2)
        
      
pred = list(combined_results['Predicated TT'])
true = list(combined_results['True TT'])
print('CMENet PPMCC:\t',round(np.corrcoef(pred, true)[0,1],2))
print('CMENet MAE:\t',round(mean_absolute_error(true, pred),2))

#safe to csv
temp_path = '/results/'
filename1 = 'CMETNet_results_2013'
combined_results[["True TT","Predicated TT"]].to_csv(temp_path+filename1, encoding='utf-8', index=False)




