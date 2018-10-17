##Calling as :  ParityCheck.py {\"compare\": {\"source1\":\"target1\", \"source2\":\"target2\"} }
### http://pbpython.com/pandas-pivot-table-explained.html

import json, sys
import random
import pandas as pd
import numpy as np
emp = {}
df = pd.read_excel("Asset_Report.xlsx",sheet_name='Raw Data')
df_subset = df[['Application','Component', 'Environment','Server Operating System','Server OS Version','Power State','# Virtual Disks']]

columns = df_subset.head(0)  ## Getting top row as header

for col in columns:
	print ("Col :", col)

for index, row in df_subset.iterrows():
	print (index, row['Application'], row['Component'])
	emp['app'] = row['Application']
	emp['serv'] = row['Component']


## To display key value pairs
#print('Printing Dict Values:')
#for key, value in emp.items():
#	print('Key : ' , key , ' and Values is :' , value)
print("####################################################################")

table=pd.pivot_table(df_subset,index=["Application","Server Operating System","Server OS Version"], values=["Component"],columns=["Environment"],aggfunc=[len],fill_value=0,margins=True)
#print(table)
table.stack('Environment')
sub_apps = "ABC"
#sub_table = table.query('Application == ["ABC","ART"]')
sub_table = table.query('Application == ["ABC","ART"]')
writer = pd.ExcelWriter('output.xlsx')

sub_table.to_excel(writer)
#for app in table.index.get_level_values(0).unique():
#	temp_df = table.xs(app, level=0)
#	temp_df.to_excel(writer,app)
writer.save()


sys.exit()



pd.pivot_table(df,index=["Manager","Rep"],values=["Price"])
##aggfunc can take a list of functions. Let’s try a mean using the numpy mean function and len to get a count.
pd.pivot_table(df,index=["Manager","Rep"],values=["Price"],aggfunc=[np.mean,len])

#The NaN’s are a bit distracting. If we want to remove them, we could use fill_value to set them to 0.
pd.pivot_table(df,index=["Manager","Rep"],values=["Price"],
               columns=["Product"],aggfunc=[np.sum],fill_value=0)#
pd.pivot_table(df,index=["Manager","Rep"],values=["Price","Quantity"],
               columns=["Product"],aggfunc=[np.sum],fill_value=0)
pd.pivot_table(df,index=["Manager","Rep","Product"],
               values=["Price","Quantity"],
               aggfunc=[np.sum,np.mean],fill_value=0,margins=True)

dct = pd.read_csv('Sample.csv', usecols=['Server_Name','CPU','Memory'], squeeze=True).to_dict()

print(type(dct))
for key, value in dct.items():
	print('Key : ' , key , ' and Values is :' , value)

print ("He")
#print (dct[1]['server8'])
#print (dct[2]['server8'])


ServerNames = dct["Server_Name"]
CPUVales = dct["CPU"]
MemoryValues = dct["Memory"]
for key, value in ServerNames.items():
	print('Key : ' , key , ' and Values is :' , value)


for key, value in CPUVales.items():
	print('Key : ' , key , ' and Values is :' , value)


for key, value in MemoryValues.items():
	print('Key : ' , key , ' and Values is :' , value)



sys.exit()


















SNOW_FileName = 'Sample.xlsx'

df = pd.read_excel(SNOW_FileName, 'Sheet1', na_values=['NA'])
dct = df.to_dict()

# print(dct.keys())  ## print

# for key, value in dct.items():
	# print('Key : ' , key , ' and Values is :' , value)


ServerNames = dct["Server_Name"]
CPUVales = dct["CPU"]
MemoryValues = dct["Memory"]
for key, value in ServerNames.items():
	print('Key : ' , key , ' and Values is :' , value)


for key, value in CPUVales.items():
	print('Key : ' , key , ' and Values is :' , value)


for key, value in MemoryValues.items():
	print('Key : ' , key , ' and Values is :' , value)






output = {}
returnObj = {}

inputString = ' '.join(sys.argv[1:])
# print (inputString);
# print (type(inputString))

inputDict =json.loads(inputString)
#print (type(inputDict))

comparePairs = inputDict["compare"]
for key, value in comparePairs.items():
	#print('Key : ' , key , ' and Values is :' , value)
	if key not in output:
		status = ["Y", "N"]
		random.shuffle(status)
		output[key] = status[0]

# for key, value in output.items():
	# print('Key : ' , key , ' and Values is :' , value)

returnObj["result"] = output
JsonReturnObj = json.dumps(returnObj)

#print(JsonReturnObj)
#return(JsonReturnObj)
sys.exit(JsonReturnObj)




#############################################################################################
for key, value in a.items():
	print('Key : ' , key , ' and Values is :' , value)
	if key not in output:
		output[key] = "Y"
js_Obj = json.dumps(output)
print (type(js_Obj))

# input = ''.join(str(e) for e in input)
# print (input);
# print (type(input))

# a =json.loads(' + input + ')
# print (type(a))
# for key, value in a.items():
	# print('Key : ' , key , ' and Values is :' , value)
	# if key not in output:
		# output[key] = "Y"
# print (dict(output))
sys.exit()

#print (input)

#j = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')

# input = json.loads(sys.argv[1])
# data_str=json.dumps(input)

# print (data_str)

output = {}
json_string = '{"name":"Rupert", "age": 25, "desig":"developer"}'
print (type (json_string))

def func(strng):
	a =json.loads(strng)
	print (type(a))
	array1 = list(a.keys())
	for key in array1:
		print("key and value pair :", key , a[key])

	for key, value in a.items():
		print('Key : ' , key , ' and Values is :' , value)
		if key not in output:
			output[key] = value

	print('now')
	print (dict(a))
	print (dict(output))
	print('dd')
	### below is the output style.. where output is a dictionary
	js_Obj = json.dumps(output)
	print (type(js_Obj))

	a =json.loads(js_Obj)
	print (type(a))
	for key, value in a.items():
		print('Key : ' , key , ' and Values is :' , value)

func(json_string)
